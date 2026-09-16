#!/usr/bin/python3
"""A01 independent counting probe; run with /usr/bin/python3 code/probe.py."""
import os

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"

import json
import math
from pathlib import Path
import resource
import sys
import time
import numpy as np

START_CPU = time.process_time()
START_WALL = time.monotonic()
OUT = Path(__file__).resolve().parents[1] / "results"
CPU_LIMIT = 120.0
MEM_LIMIT = 1024**3


def peak_bytes():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def counting_matrix(n, dtype=np.float64):
    """Directly count coprimes, without divisor/Mobius identities."""
    r = np.zeros((n, n), dtype=dtype)
    for j in range(1, n + 1):
        a = np.arange(1, j + 1, dtype=np.int64)
        counts = np.concatenate(([0], np.cumsum(np.gcd(a, j) == 1)))
        r[j - 1, :j] = counts[j // a]
    return r


def exact_check(n):
    # Build D and its integer inverse by forward substitution, independently
    # of the coprime-counting construction above.
    d = np.array([[int(i % j == 0) for j in range(1, n + 1)]
                  for i in range(1, n + 1)], dtype=np.int64)
    dinv = np.eye(n, dtype=np.int64)
    for i in range(n):
        for j in range(i):
            if d[i, j]:
                dinv[i] -= dinv[j]
    s = np.tril(np.ones((n, n), dtype=np.int64))
    r = counting_matrix(n, np.int64)
    assert np.array_equal(d @ dinv, np.eye(n, dtype=np.int64))
    assert np.array_equal(r, dinv @ s @ d), n
    # For these small cases only, cross-check power iteration against eigh.
    q = r.T @ r
    assert np.all(q > 0)
    w, v = np.linalg.eigh(q.astype(float))
    top = v[:, -1]
    if top.sum() < 0:
        top = -top
    assert np.all(top > 0)
    return {"n": n, "exact_identity": True,
            "dense_lambda": float(w[-1]),
            "dense_gap": float(w[-1] - w[-2]) if n > 1 else None,
            "dense_vector": top}


def probe(n):
    begin = time.process_time()
    r = counting_matrix(n)
    # Its last row is strictly positive, so all entries of R.T @ R are
    # strictly positive. This is also directly checked in the exact tests.
    assert np.all(r[-1] > 0)
    h = 1.0 / np.arange(1, n + 1)
    v = np.ones(n) / math.sqrt(n)  # Start independently of the target h.
    previous_error = None
    for iterations in range(1, 1001):
        if time.process_time() - START_CPU > CPU_LIMIT - 2:
            raise RuntimeError("CPU ceiling reached")
        z = r.T @ (r @ v)
        v = z / np.linalg.norm(z)
        qv = r.T @ (r @ v)
        lam = float(v @ qv)
        residual = float(np.linalg.norm(qv - lam * v))
        error = n * (h - float(v @ h) * v)
        change = (float(np.max(np.abs(error - previous_error)))
                  if previous_error is not None else None)
        if residual / lam < 2e-15 and change is not None and change < 2e-11:
            break
        previous_error = error.copy()
    else:
        raise RuntimeError(f"Power iteration failed to converge at n={n}")
    assert np.all(v > 0)
    k = int(np.argmax(np.abs(error))) + 1
    fixed = {str(k): float(error[k - 1]) for k in (1, 2, 3, 5, 10, 20)
             if k <= n}
    proportional = {}
    for alpha in (.1, .25, .5, .75, 1.):
        j = max(1, int(math.ceil(alpha * n)))
        proportional[str(alpha)] = {"k": j, "n_signed_error": float(error[j - 1])}
    result = {
        "n": n, "n_infinity_error": float(np.max(np.abs(error))),
        "maximizing_k": k, "maximizing_k_over_n": k / n,
        "n_signed_error_at_max": float(error[k - 1]),
        "fixed_coordinates": fixed, "proportional_coordinates": proportional,
        "lambda": lam, "lambda_over_n_cubed": lam / n**3,
        "residual_l2": residual, "relative_residual_l2": residual / lam,
        "last_scaled_error_change": change, "iterations": iterations,
        "v_norm": float(np.linalg.norm(v)), "v_min": float(v.min()),
        "cpu_seconds": time.process_time() - begin,
        "peak_rss_bytes": peak_bytes(),
    }
    return result, v


def main():
    OUT.mkdir(exist_ok=True)
    checks = []
    for n in range(1, 33):
        check = exact_check(n)
        row, v = probe(n)
        check["power_lambda_relative_difference"] = abs(
            row["lambda"] - check["dense_lambda"]) / check["dense_lambda"]
        check["power_vector_max_difference"] = float(np.max(
            np.abs(v - check.pop("dense_vector"))))
        assert check["power_lambda_relative_difference"] < 1e-13
        assert check["power_vector_max_difference"] < 1e-12
        checks.append(check)
    rows = []
    for n in (64, 128, 256, 500):
        row, _ = probe(n)
        rows.append(row)
    pilot = rows[-1]
    # Conservatively allow four times quadratic pilot scaling, plus 128 MiB
    # overhead and eight dense float64 matrices (only R is actually stored).
    predicted_cpu = 4 * pilot["cpu_seconds"] * sum((n / 500)**2
                                                       for n in (1000, 1500, 2000))
    predicted_memory = peak_bytes() + 128 * 1024**2 + 8 * 8 * 2000**2
    allowed = (predicted_cpu + time.process_time() - START_CPU < 110
               and predicted_memory < MEM_LIMIT)
    if allowed:
        for n in (1000, 1500, 2000):
            row, _ = probe(n)
            rows.append(row)
            assert peak_bytes() < MEM_LIMIT
    payload = {
        "python": sys.version, "numpy": np.__version__,
        "blas_threads_requested": 1,
        "method": "direct coprime counts; positive-start power iteration using R and R.T",
        "exact_checks": checks,
        "pilot_gate": {"n": 500, "projected_remaining_cpu_seconds": predicted_cpu,
                       "projected_peak_bytes": predicted_memory, "allow_2000": allowed},
        "rows": rows, "cpu_seconds": time.process_time() - START_CPU,
        "wall_seconds": time.monotonic() - START_WALL, "peak_rss_bytes": peak_bytes(),
        "limits": "Finite floating-point evidence only: no asymptotic verdict; no certified eigenvector error bound.",
    }
    (OUT / "A01.json").write_text(json.dumps(payload, indent=2) + "\n")
    lines = ["# A01 numerical probe", "",
             "Independent exact integer checks R = D^-1 S D pass for every n=1,...,32.",
             "Small-n eigenpairs also agree with numpy.linalg.eigh to the recorded tolerances.",
             "All entries of Q are positive because the last row of R is positive;",
             "Perron-Frobenius therefore selects a unique positive unit top eigenvector.", "",
             "| n | n infinity error | maximizing k | lambda/n^3 | relative residual | iterations |",
             "|---:|---:|---:|---:|---:|---:|"]
    for row in rows:
        lines.append(f'| {row["n"]} | {row["n_infinity_error"]:.12g} | '
                     f'{row["maximizing_k"]} | {row["lambda_over_n_cubed"]:.12g} | '
                     f'{row["relative_residual_l2"]:.3g} | {row["iterations"]} |')
    lines += ["", "Coordinate errors below are signed n*(h_k - (v^T h)*v_k).",
              "Full fixed/proportional coordinates, absolute residuals and timings are in A01.json.", "",
              "| n | k=1 | k=2 | k=5 | k=10 | k=ceil(n/4) | k=ceil(n/2) | k=n |",
              "|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for row in rows:
        vals = [row["fixed_coordinates"][str(k)] for k in (1, 2, 5, 10)]
        vals += [row["proportional_coordinates"][str(a)]["n_signed_error"]
                 for a in (.25, .5, 1.)]
        lines.append("| " + str(row["n"]) + " | " + " | ".join(f"{v:.9g}" for v in vals) + " |")
    lines += ["", f'CPU: {payload["cpu_seconds"]:.3f} s; wall: {payload["wall_seconds"]:.3f} s; '
              f'peak RSS: {payload["peak_rss_bytes"] / 1024**2:.1f} MiB.',
              f'Pilot projected remaining CPU: {predicted_cpu:.3f} s; '
              f'conservative memory estimate: {predicted_memory / 1024**2:.1f} MiB; gate passed: {allowed}.',
              "", "Reproduce: `/usr/bin/python3 code/probe.py` (NumPy; BLAS thread environment set to 1 before import).",
              "", "Finite-evidence limits: this sample cannot establish or refute the asserted limit.",
              "A small residual is a numerical consistency check, not a certified eigenvector error bound.",
              "Neither a finite maximizing coordinate nor its apparent trend controls the moving maximum as n tends to infinity."]
    report = "\n".join(lines) + "\n"
    (OUT / "A01.md").write_text(report)
    print(report)


if __name__ == "__main__":
    main()
