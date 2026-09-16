# The Perron vector of a totient Gram matrix and its harmonic approximation

**Release state: CANDIDATE, version 0.1.0.** This repository is being prepared
under the project's [public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
No stable archive, tag, or DOI exists yet. Admission under that standard is a
project release decision, not peer review or a correctness certificate.

## The question

Take the `n`-by-`n` matrix `R_n` whose `(j,k)` entry counts the integers up to
`j/k` that are coprime to `j`. Its first column holds Euler's totient
`phi(1), ..., phi(n)` and its diagonal is all ones. Its Gram matrix
`Q_n = R_n^T R_n` has positive entries, so it has a unique positive unit
eigenvector for its largest eigenvalue, the Perron vector `v_n`.

Kline (2020) introduced these matrices and proved that `Q_n mu_n = e_1` for
the Möbius vector `mu_n`, so `Q_n` has determinant one and the Möbius vector
is the first column of its inverse. The paper noted numerically that `v_n` is
nearly a multiple of the harmonic vector `h_n = (1, 1/2, ..., 1/n)` and
closed with a conjecture about how near:

```text
lim_{n -> infinity}  n * || h_n - (v_n^T h_n) v_n ||_inf  =  1.
```

The vector inside the norm is what is left of `h_n` after projecting it onto
`v_n`. The conjecture says this residual has sup norm exactly `1/n` to first
order.

## The answer

> **Theorem 3.1.** The conjecture is true. Write `r_n` for the residual,
> `g(a) = prod_{p | a} p/(p+1)`, `G = prod_p (1 - 1/(p(p+1)))`, and
>
> ```text
> U(t) = t - (3/(2G)) * sum_{a <= t} g(a) (1 - a^2/t^2)       (t >= 1).
> ```
>
> Then `n r_n(k) -> U(t)` whenever `k/n -> 1/t`, and for each fixed `k`,
> `n r_n(k) -> rho/k` for an explicit constant `rho` with `|rho| < 6/pi^2`.
> Since `U(1) = 1`, the conjecture is the same as `|U(t)| <= 1` for all
> `t >= 1`, and equality holds only at `t = 1`.

The proof is unconditional. It uses the prime number theorem in the effective
form `M(x) = O(x exp(-a sqrt(log x)))` for the Mertens function
`M(x) = sum_{k <= x} mu(k)`, and Ramaré's explicit bound
`|sum_{k <= x} mu(k)/k| <= 1/(12 log x)` for `x >= 687`.

**Three parts.** A matrix part writes `R_n` as the rank-one matrix
`phi_n h_n^T` plus an error small enough for first-order perturbation theory.
An arithmetic part shows the resulting correction to `h_n` has the profile
`U(n/k)`; this is where Möbius cancellation enters. A scalar part proves
`|U(t)| <= 1`: an exact integer program checks it for `1 <= t <= 10^6`, with
every real constant replaced by an outward-rounded rational interval, and
Ramaré's bound gives `|U(t)| <= 202847/300000 < 0.68` beyond `10^6`.

**Also proved, from the matrix part alone.**

- `Lambda_n / n^3 -> G/3 = 0.2348...` for the largest eigenvalue. The 2020
  paper had bounds a factor of four apart.
- `v_n^T mu_n = v_n(1) / Lambda_n` exactly, so
  `v_n^T mu_n ~ 3 sqrt(6) n^(-3) / (pi G) = 3.3205... n^(-3)`. Corollary 9 of
  the 2020 paper had `O(n^(-3/2))`.
- The remaining eigenvalues of `Q_n` sum to `O(n^2 log n)`.

## What is not claimed

One might hope to estimate the harmonic Möbius sum `m(n) = sum mu(k)/k` by
replacing `h_n` with this eigenvector approximation. An exact identity shows
why that fails: the profile correlation `sum_k mu(k) U(n/k) / n` equals
`m(n)` up to `O(log n / n)`. The paper records this obstruction. **No new
estimate for Möbius sums, the Mertens function, or the prime number theorem
is claimed.** No global novelty or priority claim is made. A bounded
literature search, recorded in [audit/PRIOR_ART.md](audit/PRIOR_ART.md),
found no other resolution of the conjecture and no earlier determination of
the constants above.

## Checking the result

Requirements: any Python 3 interpreter, standard library only.

```bash
python3 code/verify_reproduction.py
```

Expected output, with the CPU time varying:

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

This confirms that every frozen file matches its recorded SHA-256 and that
the certificate program, rerun in a temporary directory, asserts exactly what
its frozen receipt says. It does not verify the mathematics that reduces the
conjecture to those assertions. That argument is in the paper and the proof
notes.

## Repository map

- [paper/main.tex](paper/main.tex), the authoritative typeset source, and
  [paper/main.pdf](paper/main.pdf), built twice with
  [scripts/build_paper.py](scripts/build_paper.py) and compared
  byte-for-byte.
- [proof/proof-bundle.md](proof/proof-bundle.md), the complete examined
  argument, with component notes `proof/A*.md`. Status labels inside those
  notes are historical;
  [audit/campaign/FINAL-ADJUDICATION.md](audit/campaign/FINAL-ADJUDICATION.md)
  records their completed review.
- [code/certify_scalar.py](code/certify_scalar.py), the exact integer
  certificate, and [results/scalar-certificate.json](results/scalar-certificate.json),
  its frozen receipt. The program is frozen by the SHA-256 recorded in the
  receipt and the paper, so its docstring still names its interpretation note
  by the historical path `notes/A09-scalar-certificate.md`, now
  [proof/A09-scalar-certificate.md](proof/A09-scalar-certificate.md).
- [code/verify_reproduction.py](code/verify_reproduction.py) and
  [audit/frozen-artifacts.json](audit/frozen-artifacts.json), the
  reproduction runner and the manifest of frozen files it checks.
- [code/probe.py](code/probe.py) and `results/A01.*`, exploratory
  floating-point numerics through `n = 2000`. They show plausibility and
  nothing more; they are not part of the proof.
- [ADMISSION.md](ADMISSION.md), gate status and verdict;
  [AUDIT_LEDGER.md](AUDIT_LEDGER.md), audit history;
  [CORRECTIONS.md](CORRECTIONS.md), correction policy and version history;
  [RELEASE-PLAN.md](RELEASE-PLAN.md), the release plan.

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
assistance under the author's direction. One model first proposed the scalar
tail bound; another re-implemented it in exact integer arithmetic. The matrix
part, the assembled proof, and the certificate were examined by separate
fresh-context model audits; the reports, their SHA-256 seals, and the
author's adjudication are preserved in [audit/campaign/](audit/campaign/).
Further read-only release audits are summarized in
[AUDIT_LEDGER.md](AUDIT_LEDGER.md). These audits are process evidence. They
are not peer review and do not certify correctness.

## Citation and license

No citable version exists yet. When the release is archived, cite the version
DOI recorded in [CITATION.cff](CITATION.cff).

Copyright © 2026 Jeffery Kline. Licensed under the GNU General Public License,
version 3 or, at your option, any later version (`GPL-3.0-or-later`).
