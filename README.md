# A proof of the 2020 dominant-eigenvector conjecture for truncated-totient matrices

**Release state: CANDIDATE, version 0.1.0.** This repository is being prepared
under the project's [public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
Claims are frozen. No stable archive, tag, or DOI exists yet. Admission under
that standard will be a project release decision, not peer review or a
correctness certificate.

## The claim

For `1 <= j, k <= n` let `R_n(j,k)` count the integers `a <= j/k` that are
coprime to `j`. This is a truncated totient: `R_n(j,1) = phi(j)` and
`R_n(j,j) = 1`. Put `Q_n = R_n^T R_n`. Kline (2020) introduced these
matrices, proved that `Q_n mu_n = e_1` for the Möbius vector `mu_n` and the
first standard basis vector `e_1`, so that `det Q_n = 1`, and conjectured that
the positive unit dominant eigenvector `v_n` of `Q_n` satisfies

```text
lim_{n -> infinity}  n * || h_n - (v_n^T h_n) v_n ||_inf  =  1,      h_n(k) = 1/k.
```

The vector inside the norm is what remains of `h_n` after projecting onto
`v_n`. The conjecture says this residual has sup norm exactly `1/n` to first
order.

> **Main result (Theorem 3.1 of the paper).** The conjecture is true.
> More precisely, with `r_n = h_n - (v_n^T h_n) v_n`, the scaled coordinate
> `n r_n(k)` converges to `U(t)` whenever `k/n -> 1/t`, where
>
> ```text
> U(t) = t - (3/(2G)) * sum_{a <= t} g(a) (1 - a^2/t^2),
> g(a) = prod_{p | a} p/(p+1),   G = prod_p (1 - 1/(p(p+1))),
> ```
>
> and for each fixed `k` it converges to `rho/k`, where `rho` is an explicit
> constant with `|rho| < 6/pi^2`. The conjecture is equivalent to
> `|U(t)| <= 1` for all real `t >= 1`, which holds with equality only at
> `t = 1`.

The proof is unconditional. It uses the prime number theorem in the effective
form `M(x) = O(x exp(-a sqrt(log x)))` for the Mertens function
`M(x) = sum_{k <= x} mu(k)`, and Ramaré's explicit bound
`|sum_{k <= x} mu(k)/k| <= 1/(12 log x)` for `x >= 687`. No unproved
hypothesis is assumed.

## How the proof goes

1. **Matrix step.** `R_n = phi_n h_n^T + E_n`, where `phi_n` lists the
   totient values. The error `E_n` has Frobenius norm (the square root of the
   sum of squared entries) `O(n log^(1/2) n)`, against order `n^(3/2)` for
   the rank-one main term. Rank-one perturbation gives `v_n`, the dominant
   eigenvalue `Lambda_n`, and `r_n` in terms of the correction vector
   `q = E_n^T phi_n / ||phi_n||^2`, up to Euclidean error `O(n^(-3/2) log^3 n)`.
2. **Arithmetic step.** `n q_k = -U(n/k) + O(log^2 n / k)` uniformly in `k`,
   with a separate estimate showing `n q_k` is smaller than any power of
   `log n` when `k <= log^B n`. This is where Möbius cancellation enters.
3. **Scalar step.** `U` is convex on each `[m, m+1]` and given by a closed
   formula in two partial sums. An exact integer program verifies
   `U(m) < 3/4` at all `999,999` integer endpoints `2 <= m <= 10^6` and a lower
   enclosure `U > -3/4` on all `1,999,998` half-integer intervals. Every real
   constant is replaced by a rational interval that provably contains it,
   rounded outward, with denominator `10^30`. For `t >= 10^6`, Ramaré's bound
   gives `|U(t)| <= 202847/300000 < 0.68`.

The last column of `R_n` is the last standard basis vector `e_n`, which gives
`n r_n(n) -> 1` and the matching lower bound.

## Consequences

Using only the matrix step:

- `Lambda_n / n^3 -> G/3 = 0.2348...`. The 2020 paper had only the two-sided
  bounds `0.1427 n^3 <~ Lambda_n <= 0.5483 n^3`.
- `v_n^T mu_n = v_n(1) / Lambda_n` exactly, hence
  `v_n^T mu_n ~ 3 sqrt(6) n^(-3) / (pi G) = 3.3205... n^(-3)`, replacing the
  `O(n^(-3/2))` bound of Corollary 9 in the 2020 paper.
- All other eigenvalues of `Q_n` sum to `O(n^2 log n)`.

## What is not claimed

The natural attempt to estimate the harmonic Möbius sum `m(n) = sum mu(k)/k`
through this eigenvector approximation fails for an exact reason: the profile
correlation `sum_k mu(k) U(n/k) / n` equals `m(n)` up to `O(log n / n)`.
The paper records this obstruction. **No new estimate for Möbius sums, the
Mertens function, or the prime number theorem is claimed.** No global novelty
or priority claim is made. A bounded literature search, recorded in
[audit/PRIOR_ART.md](audit/PRIOR_ART.md), found no other resolution of the
conjecture and no earlier determination of the constants above.

## Evidence and reproduction

- [paper/main.tex](paper/main.tex) is the authoritative typeset source and
  [paper/main.pdf](paper/main.pdf) the reading copy, built twice with
  [scripts/build_paper.py](scripts/build_paper.py) and compared byte-for-byte.
- [proof/proof-bundle.md](proof/proof-bundle.md) is the complete examined
  argument; `proof/A*.md` are its component notes. Status labels inside those
  notes are historical; [audit/campaign/FINAL-ADJUDICATION.md](audit/campaign/FINAL-ADJUDICATION.md)
  records their completed review.
- [code/certify_scalar.py](code/certify_scalar.py) is the exact integer
  certificate for the scalar inequality;
  [results/scalar-certificate.json](results/scalar-certificate.json) is its
  frozen receipt. The program is frozen by the SHA-256 recorded in the receipt
  and the paper, so its docstring still names its interpretation note by the
  historical path `notes/A09-scalar-certificate.md`, now
  [proof/A09-scalar-certificate.md](proof/A09-scalar-certificate.md).
- [code/verify_reproduction.py](code/verify_reproduction.py) checks the
  SHA-256 of every frozen artifact listed in
  [audit/frozen-artifacts.json](audit/frozen-artifacts.json), then reruns the
  certificate in a temporary directory and compares every deterministic field
  with the receipt. It does not overwrite the receipt.
- [code/probe.py](code/probe.py) and `results/A01.*` are exploratory
  floating-point numerics through `n = 2000`. They are evidence of nothing
  beyond plausibility and are not part of the proof.

Requirements: any Python 3 interpreter; standard library only.

```bash
python3 code/verify_reproduction.py
```

Expected output (the CPU time will vary):

```json
{
  "status": "FROZEN_CERTIFICATE_REPRODUCED",
  "hashed_artifacts": 16,
  "endpoint_checks": 999999,
  "half_interval_checks": 1999998,
  "process_cpu_seconds": 7.16,
  "scope": "integrity and reproducibility of the frozen certificate; not a proof of correctness"
}
```

Reproducing the certificate confirms that the program asserts what the paper
says it asserts. It does not by itself verify the mathematics that reduces the
conjecture to those assertions; that argument is in the paper and proof notes.

## Prior work and sources

- J. Kline, *Unital sums of the Möbius and Mertens functions*, J. Integer
  Seq. 23 (2020), Article 20.8.1. Source of the matrices, the identities
  `R_n mu_n = e_1` and `Q_n mu_n = e_1`, the eigenvalue bounds, Corollary 9,
  and the conjecture. Its TeX source is preserved at [ref/kline4.tex](ref/kline4.tex).
- O. Ramaré, *Explicit estimates on several summatory functions involving the
  Moebius function*, Math. Comp. 84 (2015), no. 293, 1359–1387, Theorem 1.2,
  and its corrigendum, Math. Comp. 88 (2019), no. 319, 2383–2388, which does
  not alter that theorem. The PDFs are not redistributed; their URLs and
  SHA-256 are recorded in `audit/frozen-artifacts.json`.
- E. S. Lee and N. Leong, arXiv:2208.06141v5 (preprint, 9 September 2026),
  Theorem 1.1, equation (9), for an explicit effective Mertens bound. The
  locator is specific to version 5.
- The nearest spectral literature concerns Redheffer's matrix, a different
  `(0,1)` divisibility matrix with spectral radius of order `sqrt(n)`:
  Barrett, Forcade and Pollington (1988), Vaughan (1993, 1996), and Clément
  and Steinerberger (arXiv:2502.09489, 2025) on its dominant singular vector.
  None addresses `R_n` or `Q_n`.
- An unreleased August 2026 working repository by the author proved the
  eigenvalue constant and the lower bound `liminf >= 1` and left the upper
  bound open. This release supersedes it.

Source locators from the proof campaign are in
[audit/campaign/LITERATURE.md](audit/campaign/LITERATURE.md); the release-time
search is in [audit/PRIOR_ART.md](audit/PRIOR_ART.md).

## AI assistance

The argument, certificate program, and exposition were developed with AI
assistance under the author's direction. The scalar tail bound was first
proposed by one model and re-implemented in exact integer arithmetic by
another. The matrix step, the assembled proof, and the certificate were
examined by separate fresh-context model audits; the reports, their SHA-256
seals, and the author's adjudication are preserved in
[audit/campaign/](audit/campaign/). Four further read-only release audits are
summarized in [AUDIT_LEDGER.md](AUDIT_LEDGER.md). Those audits are process
evidence. They are not peer review and do not certify correctness.

## Release records

[ADMISSION.md](ADMISSION.md) carries the gate status and verdict,
[AUDIT_LEDGER.md](AUDIT_LEDGER.md) the audit history, and
[CORRECTIONS.md](CORRECTIONS.md) the correction policy and version history.
[RELEASE-PLAN.md](RELEASE-PLAN.md) is the release plan.

## Citation and license

No citable version exists yet. When the release is archived, cite the version
DOI recorded in [CITATION.cff](CITATION.cff).

Copyright © 2026 Jeffery Kline. Licensed under the GNU General Public License,
version 3 or, at your option, any later version (`GPL-3.0-or-later`).
