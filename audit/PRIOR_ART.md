# Bounded prior-art record

This file records the release-time literature search. It is bounded; it does
not establish global novelty or priority. Inaccessible sources are named and
not counted as negative evidence.

## Question

Has the concluding conjecture of Kline, *Unital sums of the Möbius and
Mertens functions*, J. Integer Seq. 23 (2020), Art. 20.8.1, been resolved
elsewhere, and have the leading constant of `Lambda_max(Q_n)` or the
asymptotic of `v_n^T mu_n` for these matrices been determined before?

## Corpus and date

Searched 2026-09-15 by a process-separated AI auditor, unrestricted date
range: the arXiv API (queries on "Redheffer matrix", "totient matrix",
"unital sums", Mertens with Perron, Kline with Mertens, totient with
eigenvector); zbMATH Open (record Zbl 1468.11015 for the 2020 paper, MSC
11A25, 11C20, 15B36) through its API; the Journal of Integer Sequences site;
general web search; and the citation chains of the Redheffer-matrix papers
below. The campaign's own targeted search on 2026-09-14 recovered only the
2020 paper.

## Result

No published or preprint resolution of the conjecture was found. No prior
determination of the eigenvalue constant `G/3` or of the `n^-3` asymptotic of
`v_n^T mu_n` for `Q_n` was found. arXiv returned no hits for "totient matrix"
or "unital sums" in this sense.

## Closest related work

All of the following concern Redheffer's matrix, the `(0,1)` matrix with
`(i,j)` entry one exactly when `j = 1` or `i | j`, whose determinant is the
Mertens function. Its spectral radius is of order `sqrt(n)`, against `n^3`
for `Q_n`; none addresses `R_n`, `Q_n`, or a sup-norm residual limit.

- W. W. Barrett, R. W. Forcade, A. D. Pollington, *On the spectral radius of a
  (0,1) matrix related to Mertens' function*, Linear Algebra Appl. 107
  (1988), 151–159. All but `floor(log_2 n) + 1` eigenvalues equal one;
  spectral radius asymptotic to `sqrt(n)`.
- W. W. Barrett, T. J. Jarvis, *Spectral properties of a matrix of Redheffer*,
  Linear Algebra Appl. 162–164 (1992), 673–683.
- R. C. Vaughan, *On the eigenvalues of Redheffer's matrix I*, Lecture Notes
  in Pure and Appl. Math. 147 (1993), 283–296; *II*, J. Austral. Math. Soc.
  Ser. A 60 (1996), 260–273.
- F. Clément, S. Steinerberger, *On the largest singular vector of the
  Redheffer matrix*, arXiv:2502.09489 (13 February 2025). Closest in
  mechanism: the dominant singular vector is shown close to the explicit
  vector `k -> sum_{d | k} 1/d`. Different matrix, singular rather than
  eigen-vector, and closeness rather than a sharp residual constant.
- H. S. Wilf, *The Redheffer matrix of a partially ordered set*, Electron. J.
  Combin. 11(2) (2004). Determinant, not spectrum.

## Sources verified for the analytic inputs

- Ramaré, Math. Comp. 84 (2015), no. 293, 1359–1387: Theorem 1.2 on printed
  page 1361 states `(log x) |sum_{n <= x} mu(n)/n| <= 1/12` for `x >= 687`
  among other bounds. Read from the author-hosted offprint.
- Ramaré, Corrigendum, Math. Comp. 88 (2019), no. 319, 2383–2388,
  doi:10.1090/mcom/3449: its overview of modifications lists Theorems 1.5,
  1.7, 1.8 and several lemmas; Theorem 1.2 and Corollary 1.3 are not
  modified.
- Lee and Leong, arXiv:2208.06141v5 (9 September 2026): Theorem 1.1,
  equation (9), gives `|M(x)| < 33.56 x (log x) exp(-sqrt(log x / 5.56))` for
  large `x`, of the form used after absorbing the logarithm. The locator is
  version-specific; version 4 numbers the statements differently.

## Inaccessible or incomplete

- MathSciNet: no subscription.
- zbMATH citation counts for Zbl 1468.11015: web interface returned HTTP 403;
  the API exposes references, not citing works.
- Semantic Scholar and OpenAlex: rate-limited.
- Google Scholar: returned a mismatched record; treated as unreliable.
- Ivić, *The Riemann Zeta-Function*, Theorem 12.7, the textbook source for
  the effective Mertens bound: not inspected directly.

Citation tracking of the 2020 paper is therefore incomplete.
