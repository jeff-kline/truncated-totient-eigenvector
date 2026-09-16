# The Perron vector of a totient Gram matrix and its harmonic approximation

**Release state: CANDIDATE, version 0.1.0.** This repository is being prepared
under the project's [public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
No stable archive, tag, or DOI exists yet. Admission under that standard is a
project release decision, not peer review or a correctness certificate.

## The question

Take the $n\times n$ matrix $R_n$ whose $(j,k)$ entry counts the integers up
to $j/k$ that are coprime to $j$:

```math
R_n(j,k)=\#\{1\le a\le\lfloor j/k\rfloor:\gcd(a,j)=1\}.
```

Its first column holds Euler's totient $\varphi(1),\ldots,\varphi(n)$ and its
diagonal is all ones. Its Gram matrix $Q_n=R_n^{\top}R_n$ has positive
entries, so it has a unique positive unit eigenvector for its largest
eigenvalue $\Lambda_n$, the Perron vector $v_n$.

Kline (2020) introduced these matrices and proved that $Q_n\mu_n=e_1$ for
the Möbius vector $\mu_n=(\mu(1),\ldots,\mu(n))^{\top}$, so $Q_n$ has
determinant one and the Möbius vector is the first column of its inverse.
The paper noted numerically that $v_n$ is nearly a multiple of the harmonic
vector $h_n=(1,\tfrac12,\ldots,\tfrac1n)^{\top}$ and closed with a conjecture
about how near:

```math
\lim_{n\to\infty} n\,\bigl\lVert h_n-(v_n^{\top}h_n)\,v_n\bigr\rVert_\infty=1 .
```

The vector inside the norm is what is left of $h_n$ after projecting it onto
$v_n$. The conjecture says this residual has sup norm exactly $1/n$ to first
order.

## The answer

> **Theorem 3.1.** The conjecture is true. Write $r_n=h_n-(v_n^{\top}h_n)v_n$
> for the residual, $g(a)=\prod_{p\mid a}p/(p+1)$,
> $G=\prod_p\bigl(1-\tfrac{1}{p(p+1)}\bigr)$, and, for real $t\ge1$,
>
> ```math
> U(t)=t-\frac{3}{2G}\sum_{a\le t} g(a)\Bigl(1-\frac{a^2}{t^2}\Bigr).
> ```
>
> Then $n\,r_n(k)\to U(t)$ whenever $k/n\to1/t$, and for each fixed $k$,
> $n\,r_n(k)\to\rho/k$ for an explicit constant $\rho$ with
> $|\rho|<6/\pi^2$. Since $U(1)=1$, the conjecture is the same as
> $|U(t)|\le1$ for all $t\ge1$, and equality holds only at $t=1$.

The proof is unconditional. It uses the prime number theorem in the effective
form $M(x)=O\bigl(x\exp(-a\sqrt{\log x})\bigr)$ for the Mertens function
$M(x)=\sum_{k\le x}\mu(k)$, and Ramaré's explicit bound
$\bigl|\sum_{k\le x}\mu(k)/k\bigr|\le 1/(12\log x)$ for $x\ge687$.

**Three parts.** A matrix part writes $R_n$ as the rank-one matrix
$\varphi_nh_n^{\top}$ plus an error small enough for first-order perturbation
theory. An arithmetic part shows the resulting correction to $h_n$ has the
profile $U(n/k)$; this is where Möbius cancellation enters. A scalar part
proves $|U(t)|\le1$: an exact integer program checks it for $1\le t\le10^6$,
using convexity and monotone enclosures on each unit interval, with every
real constant replaced by an outward-rounded rational interval, and Ramaré's
bound gives $|U(t)|\le 202847/300000<0.68$ beyond $10^6$.

**What the 2020 paper had, and what this release proves.** Here
$c=\tfrac13\prod_p\bigl(1-\tfrac{2}{p^2}+\tfrac{1}{p^3}\bigr)=0.1427\ldots$,
the constant of the 2020 paper, and $c\,\zeta(2)=G/3$.

| Statement in Kline (2020) | There | Here |
|---|---|---|
| Conjecture after Corollary 9 | $\lim n\lVert h_n-(v_n^{\top}h_n)v_n\rVert_\infty=1$, open | proved, with the residual profile $U$ (Theorem 3.1) |
| Proposition 8, largest eigenvalue | $(c+o(1))n^3\le\Lambda_n\le\tfrac{\pi^2}{18}n^3+O(n^2)$ | $\Lambda_n\sim c\,\zeta(2)\,n^3=0.2348\ldots n^3$ (Proposition 4.1) |
| Corollary 9, Möbius correlation | $\lvert v_n^{\top}\mu_n\rvert\le(c^{-1/2}+o(1))\,n^{-3/2}$ | $v_n^{\top}\mu_n=v_n(1)/\Lambda_n\sim n^{-3}/(c\,\zeta(2)^{3/2})=3.3205\ldots n^{-3}$ (Proposition 4.1) |

The two improvements use only the matrix part. Also from that part: the
remaining eigenvalues of $Q_n$ sum to $O(n^2\log n)$ (Proposition 4.2).

## What is not claimed

Since $m(n)=\sum_{k\le n}\mu(k)/k=h_n^{\top}\mu_n$, one might hope to estimate
$m(n)$ by replacing $h_n$ with its projection onto $v_n$. An exact identity
shows why that fails: the profile correlation
$\tfrac1n\sum_{k\le n}\mu(k)\,U(n/k)$ equals $m(n)$ up to $O(\log n/n)$. The
paper records this obstruction. **No new estimate for Möbius sums, the
Mertens function, or the prime number theorem is claimed.** No priority claim
is made. A bounded literature search, recorded in
[audit/PRIOR_ART.md](audit/PRIOR_ART.md), found no other resolution of the
conjecture and no earlier determination of the constants above.

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
  its frozen receipt. Its docstring names the interpretation note by its old
  path `notes/A09-scalar-certificate.md`; the note now lives at
  [proof/A09-scalar-certificate.md](proof/A09-scalar-certificate.md). The
  program is frozen by hash, so the path was left as is.
- [code/verify_reproduction.py](code/verify_reproduction.py) and
  [audit/frozen-artifacts.json](audit/frozen-artifacts.json), the
  reproduction runner and the manifest of frozen files it checks.
- [code/probe.py](code/probe.py) and `results/A01.*`, exploratory
  floating-point numerics through $n=2000$. They show plausibility and
  nothing more; they are not part of the proof.
- [ADMISSION.md](ADMISSION.md), gate status and verdict;
  [AUDIT_LEDGER.md](AUDIT_LEDGER.md), audit history;
  [CORRECTIONS.md](CORRECTIONS.md), correction policy and version history;
  [RELEASE-PLAN.md](RELEASE-PLAN.md), the release plan.

## Prior work and sources

- J. Kline, *Unital sums of the Möbius and Mertens functions*, J. Integer
  Seq. 23 (2020), Article 20.8.1. Source of the matrices, the identities
  $R_n\mu_n=e_1$ and $Q_n\mu_n=e_1$, Proposition 8, Corollary 9, and the
  conjecture. Its TeX source is preserved at [ref/kline4.tex](ref/kline4.tex).
- O. Ramaré, *Explicit estimates on several summatory functions involving the
  Moebius function*, Math. Comp. 84 (2015), no. 293, 1359–1387, Theorem 1.2,
  and its corrigendum, Math. Comp. 88 (2019), no. 319, 2383–2388, which does
  not alter that theorem. The PDFs are not redistributed; their URLs and
  SHA-256 are recorded in `audit/frozen-artifacts.json`.
- E. S. Lee and N. Leong, arXiv:2208.06141v5 (preprint, 9 September 2026),
  Theorem 1.1, equation (9), for an explicit effective Mertens bound. The
  locator is specific to version 5.
- The nearest spectral literature concerns Redheffer's matrix, a different
  $(0,1)$ divisibility matrix with spectral radius of order $\sqrt n$:
  Barrett, Forcade and Pollington (1988), Vaughan (1993, 1996), and Clément
  and Steinerberger (arXiv:2502.09489, 2025) on its dominant singular vector.
  None addresses $R_n$ or $Q_n$.
- An unreleased August 2026 working repository by the author proved the
  eigenvalue constant and the lower bound $\liminf\ge1$ and left the upper
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
