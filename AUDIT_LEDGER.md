# Audit ledger

This append-only ledger records the scope and disposition of audits. AI-assisted
checks are process evidence, not peer review or independent expert validation.
The campaign records themselves are preserved unchanged in `audit/campaign/`;
their SHA-256 values are in `audit/frozen-artifacts.json`.

## 2026-09-14 — campaign: matrix-step failure search and proof audit

- Auditor type: process-separated fresh-context AI (two lanes, R01 then R02).
- Scope: the uniform vector reduction `r = r_1 h - q + e`, the error bound
  `||e||_2 = O(n^-3/2 log^3 n)`, and the lower bound `liminf >= 1`.
- Sealed before proof exposure: `audit/campaign/R01-initial.md`.
- Disposition: R02 VERIFIED the four formal matrix claims. Arithmetic
  profile, normalization integral, and the upper bound were outside scope.
  See `audit/campaign/SEALS.md`.

## 2026-09-14 — campaign: scalar tail proposal received

- Source: process-separated AI proposal, preserved byte-for-byte as
  `audit/campaign/CLAUDE-01-received.txt`.
- Disposition: the source gap was repaired and the unavailable floating-point
  computation replaced by the exact integer certificate
  `code/certify_scalar.py`. See `audit/campaign/CLAUDE-01-adjudication.md`.

## 2026-09-14 — campaign: statement-only failure search, then full proof audit

- Auditor type: process-separated fresh-context AI, same provider as the
  scalar tail proposal (disclosed).
- Sealed before proof exposure: `audit/campaign/CLAUDE-02-initial-report.md`
  (NOT-BROKEN; a failed attack, not verification).
- Full audit: `audit/campaign/CLAUDE-02-proof-audit.md` against the frozen
  packet `proof/proof-bundle.md`.
- Disposition: `audit/campaign/FINAL-ADJUDICATION.md` accepts the argument,
  discharges the skipped finite-`N` Mellin calculation explicitly, and
  records notation, resource, and provider-dependence caveats. Verdict:
  VERIFIED for the original limit and the scalar inequality.

## 2026-09-14 — campaign: reproducibility checkpoint

- Scope: 16 frozen artifact hashes; certificate rerun in a fresh temporary
  directory; all deterministic receipt fields reproduced.
- Disposition: reproducibility established; not a proof audit.

## 2026-09-15 — release: relocation and reproduction under the release layout

- Scope: every frozen artifact relocated with unchanged bytes;
  `audit/frozen-artifacts.json` maps the new paths to the campaign hashes;
  `code/verify_reproduction.py` repointed at that manifest.
- Result: `FROZEN_CERTIFICATE_REPRODUCED`, 16 hashed artifacts, 999,999
  endpoint checks, 1,999,998 half-interval checks.

## 2026-09-15 — release: four read-only fresh-context lanes

All four lanes ran in parallel on the draft commit
`eb1d4bf209079f8897ed893c0816708f32ae1c41` after the abstract, introduction,
and README were stabilized. Auditor type: process-separated AI on one
provider; the proof lane on the frontier tier, the others on lower tiers.
Findings were integrated by the root agent; no auditor edited the tree.

### Proof and parameter lane — PASS

- Re-derived Lemma 3.2 (divisor expansion of `E`, the three norm bounds, the
  two exact coordinate identities, the projection formula, `S = c n^3 +
  O(n^2 L^2)`, `G = 3 c zeta(2)`), Lemma 3.3 (the coprime totient sum, the
  index swap giving `n q_k = -U(n/k) + O(L^2/k)`, the A06 chain, the kernel
  identity, the Mellin evaluation with a numerical check at `s = 1/2`, the
  limit `I = 1/(4c) - 1`), Lemma 3.4 (Bernoulli expansion, `K_0`, the tail
  identity and bound, Ramaré's Theorem 1.2 read from the offprint, the exact
  value `202847/300000`, convexity), the proof of Theorem 3.1, and
  Propositions 4.1, 4.2, 6.1, 6.2.
- Independently enclosed `kappa`, `G/3`, `3 sqrt(6)/(pi G)`, `3/G`, `c`, and
  `E_{1/2}`; all printed digits confirmed. Confirmed the certificate's integer
  assertions encode exactly the lemma's inequalities with outward rounding
  and that endpoint, half-interval, and tail pieces exhaust `t >= 1`.
- Findings (all optional): stale historical path and two loose comment
  wordings inside the hash-frozen certificate program; an implicit
  perturbation-bound citation in Lemma 3.2.
- Disposition: documented the frozen program's comments in the paper
  appendix, README, and `audit/frozen-artifacts.json`; added a clause to the
  Lemma 3.2 proof naming the gap and the companion note. The program was not
  edited.

### Claim and public-prose lane — PARTIAL, resolved

- Verified title, author, and version agreement; theorem numbering; all
  README links; absence of process-history language; separation of evidence
  levels; bounded novelty wording; numerical agreement across surfaces.
- Must-fix items and dispositions: paper date line versus DRAFT status
  (resolved by advancing all surfaces to CANDIDATE together); README claim
  of a completed deterministic build (rejected: the build was performed and
  matched; the stale entries were in this ledger and the plan, now updated);
  stale theorem number and a private path in the plan (fixed); CFF `message`
  (reworded to a timeless form, because Zenodo ingests it verbatim); CFF
  abstract qualifications (the timeless novelty sentence added; draft-status
  wording rejected for the same reason); `M(x)` undefined in README (fixed).
- Optional items: fixed-`k` limit added to the statement of Theorem 3.1;
  component-note glob widened; version number added to the README status
  line; Frobenius norm, `rho`, `e_n`, and outward enclosures defined in the
  README. The AI-disclosure wording and the ledger's literal file names were
  kept.

### Citation and prior-art lane — PARTIAL, resolved

- Verified all four bibliography entries against primary sources: Kline 2020
  (conjecture verbatim at `ref/kline4.tex:798`); Ramaré 2015 Theorem 1.2 on
  printed page 1361; the 2019 corrigendum's modification list; Lee–Leong v5
  Theorem 1.1 (9).
- Searched arXiv API, zbMATH Open API, JIS, web, and Redheffer citation
  chains; no prior resolution or prior constants found. Inaccessible:
  MathSciNet, zbMATH citation counts, Semantic Scholar, OpenAlex.
- Must-fix items and dispositions: closest prior work undiscussed (added a
  Redheffer-matrix paragraph and three references to the paper and README;
  the two arXiv records were re-verified by the root agent through the arXiv
  API); a stale campaign sentence saying no search was performed (the
  campaign file is preserved; the release-time search is recorded in
  `audit/PRIOR_ART.md`); incomplete corrigendum record and unpinned arXiv
  version (fixed; issue number and preprint date added).

### Reproducibility and release-mechanics lane — PARTIAL, resolved

- Ran the reproduction: `FROZEN_CERTIFICATE_REPRODUCED`, 16, 999,999,
  1,999,998; no tracked file modified. Recomputed all 16 frozen hashes: no
  mismatch. Rebuilt the PDF twice in scratch with the pinned environment:
  SHA-256 `4c6a1fe660bc957a93333f86168e8136fd0dac26c6e44f6b3ba6a921f4fea445`,
  311,856 bytes, equal to `paper/main.pdf` at that commit. Verified manifest
  coverage, CFF mechanics, links, absence of private paths and placeholders,
  archive route and owner table, no tags, nothing pushed, and the HEAD
  identity `Jeff Kline <2778446+jeff-kline@users.noreply.github.com>`.
- Must-fix items and dispositions: two frozen entries absent from the
  campaign's integrity manifest (documented in `audit/frozen-artifacts.json`
  as sealed by hash in `SEALS.md` and `FINAL-ADJUDICATION.md`); stale path in
  the certificate docstring (rejected as an edit; documented instead, since
  the program is frozen by the digest cited in the paper and receipt).

## Open audits

- Candidate-state mechanical audit on the clean integrated tree
  (`--require-clean`), then outgoing-identity inspection before the freeze
  bundle.
- Archived-state audit after the Zenodo record exists.
- Final clean admitted-state audit and publication of the living metadata.
