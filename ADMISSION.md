# Admission record

**Current verdict: NOT YET ADMITTED.**

**Release state:** CANDIDATE

**Version:** 0.1.0 (candidate; no tag, archive, or DOI exists)

Admission is a project-defined release decision under Jeff Kline's
["A Public Standard for This Work"](https://jeff-kline.github.io/posts/research-program/index.html).
It means the claim, evidence, prior-work record, reproducibility materials,
citation, and correction policy passed the gates below against one frozen
commit. **It is not peer review, a correctness certificate, or proof of global
novelty.**

## Standard applied

Jeff Kline, ["A Public Standard for This
Work"](https://jeff-kline.github.io/posts/research-program/index.html),
draft 0.4, August 2026.

## Gate status

| Gate | Status | Evidence and disposition |
|---|---|---|
| P1 — prior work and credit | **PASS — BOUNDED** | `audit/PRIOR_ART.md` records the 2026-09-15 search (arXiv API, zbMATH Open API, JIS, web, citation chains of the Redheffer-matrix papers) and the closest work: Barrett–Forcade–Pollington, Barrett–Jarvis, Vaughan, Clément–Steinerberger, all on Redheffer's matrix. No prior resolution or prior constants found. Ramaré's Theorem 1.2 and corrigendum and Lee–Leong's Theorem 1.1 (9) were verified from primary sources. MathSciNet, zbMATH citation counts, and Ivić's Theorem 12.7 remain inaccessible or uninspected and are not counted as negative evidence. The paper and README qualify novelty to the searched corpus. |
| A1 — claim and artifact consistency | **PASS** | Paper, README, and CFF state the same principal claim, hypotheses, and limitations. The proof lane re-derived Lemmas 3.2–3.4, the proof of Theorem 3.1, and Propositions 4.1, 4.2, 6.1, 6.2, enclosed the three leading constants independently to all printed digits, and confirmed the certificate's integer assertions encode the lemma's inequalities with outward rounding: no defect. The prose lane's must-fix items were resolved or dispositioned in `AUDIT_LEDGER.md`. Process-history language is absent from reader-facing prose; AI audits are described as process evidence. Any further material claim edit reopens A1. |
| R1 — release and stewardship | **PARTIAL** | Pre-freeze rows pass: `code/verify_reproduction.py` reproduces the frozen certificate (16 hashed artifacts, 999,999 endpoint and 1,999,998 half-interval checks); `paper/main.pdf` is a deterministic double build; `MANIFEST.sha256` covers every tracked file; links, CFF mechanics, and hygiene verified. Tag, archive, DOI, public-record metadata, and byte identity are pending the freeze and admission bundles. |

## Claim boundary

- **Proved here:** the 2020 conjecture; the coordinatewise limit profile
  `U` and the fixed-coordinate limit `rho/k`; the eigenvalue constant `G/3`;
  the exact identity `Lambda_n v_n^T mu_n = v_n(1)` and the `n^-3`
  asymptotic; the spectral remainder bound; the exact convolution obstruction
  identity.
- **Computed, exactly:** `|U(t)| <= 1` on `[1, 10^6]` by integer assertions
  with outward rational enclosures (`code/certify_scalar.py`).
- **Classical and external inputs:** the identities `R_n mu = e_1`,
  `Q_n mu = e_1`; the totient-square asymptotic; an effective Mertens bound
  of PNT strength; Ramaré's Theorem 1.2.
- **Not claimed:** any new estimate for Möbius or Mertens sums or the prime
  number theorem; RH or GRH input; global novelty or priority; human
  refereeing; proof-assistant verification.

## Named residual risks

- Process-separated AI examinations share training data and blind spots;
  the scalar tail proposal and its full-proof audit in the campaign came from
  the same provider, and all four release-time lanes ran on one provider.
- The campaign auditor did not rederive every term of the finite-`N` Mellin
  formula; the adjudication supplies the calculation explicitly. The release
  proof lane checked the Mellin value numerically at one point and the
  `s -> 0` limit.
- Ivić's Theorem 12.7, the textbook source for the effective Mertens bound,
  was not inspected directly; the bound was source-checked against Ng's
  lecture notes and Lee–Leong's explicit theorem. The Lee–Leong locator is
  specific to arXiv version 5, posted six days before this candidate.
- The frozen certificate program carries a historical path and two loose
  comments; they are documented in the paper appendix, not edited.
- The prior-art review is bounded; inaccessible databases are not treated as
  negative evidence, and citation tracking of the 2020 paper is incomplete.

## Execution boundary

Permission for one action never implies permission for the next.

| Action | Owner | Status |
|---|---|---|
| Local edits, builds, tests | agent | candidate frozen |
| Default-branch candidate push | Jeff Kline | not authorized |
| Public tag `v0.1.0` | Jeff Kline | not authorized |
| GitHub Release | Jeff Kline | not authorized |
| Zenodo portal | Jeff Kline (authenticated portal) | not started |
| Public-site listing | Jeff Kline | not authorized |
| Living-metadata push | Jeff Kline | not authorized |

## Archive route

Zenodo GitHub integration. The repository must be enabled in Zenodo before
the GitHub Release. The GitHub `zipball/v0.1.0` will be downloaded twice and
pinned before the Release; the Zenodo file must equal those bytes. A
`git archive v0.1.0` will be generated twice as a secondary determinism
check and recorded separately.

## State transitions

| State | Condition | Status |
|---|---|---|
| DRAFT → CANDIDATE | P1, A1, and pre-freeze R1 pass; prose and artifacts agree. | **reached 2026-09-15** |
| CANDIDATE → TAGGED | Freeze one clean commit; create one immutable tag. | pending |
| TAGGED → ARCHIVED | Archive the tagged tree; verify the download byte-for-byte. | pending |
| ARCHIVED → ADMITTED | Reconcile living surfaces; commit the verdict; final clean audit. | pending |
