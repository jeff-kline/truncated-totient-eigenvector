# Admission record

**Current verdict: ADMITTED.**

**Release state:** ADMITTED

**Version:** 0.1.0

**Admission date:** 16 September 2026

**Immutable release:** `v0.1.0` at commit `0746f6df69cc7c7b551ef47dffbd8436f0c1a1aa`, archived under version
DOI [10.5281/zenodo.22783896](https://doi.org/10.5281/zenodo.22783896). The concept DOI
[10.5281/zenodo.22783895](https://doi.org/10.5281/zenodo.22783895) resolves to the latest archived version.

**Postpublication living-metadata commit:** `7f610bef364b2ab7400cc7ca9a9629fbe7f75289`

Admission is a project-defined release decision under Jeff Kline's
["A Public Standard for This Work"](https://jeff-kline.github.io/posts/research-program/index.html).
It means the claim, evidence, prior-work record, reproducibility materials,
citation, and correction policy passed the gates below against one frozen
commit. **It is not peer review, a correctness certificate, or proof of global
novelty.** The immutable archive completed R1's tag, archive, DOI, metadata,
and byte-identity checks. The living DOI reconciliation was committed
separately from this verdict so the final admitted tree could be checked
cleanly before publication.

## Standard applied

Jeff Kline, ["A Public Standard for This
Work"](https://jeff-kline.github.io/posts/research-program/index.html),
draft 0.4, August 2026.

## Gate status

| Gate | Status | Evidence and disposition |
|---|---|---|
| P1 — prior work and credit | **PASS — BOUNDED** | `audit/PRIOR_ART.md` records the 2026-09-15 search (arXiv API, zbMATH Open API, JIS, web, citation chains of the Redheffer-matrix papers) and the closest work: Barrett–Forcade–Pollington, Barrett–Jarvis, Vaughan, Clément–Steinerberger, all on Redheffer's matrix. No prior resolution or prior constants found. Ramaré's Theorem 1.2 and corrigendum and Lee–Leong's Theorem 1.1 (9) were verified from primary sources. MathSciNet, zbMATH citation counts, and Ivić's Theorem 12.7 remain inaccessible or uninspected and are not counted as negative evidence. The paper and README qualify novelty to the searched corpus. |
| A1 — claim and artifact consistency | **PASS** | Paper, README, and CFF state the same principal claim, hypotheses, and limitations. The proof lane re-derived Lemmas 3.2–3.4, the proof of Theorem 3.1, and Propositions 4.1, 4.2, 6.1, 6.2, enclosed the three leading constants independently to all printed digits, and confirmed the certificate's integer assertions encode the lemma's inequalities with outward rounding: no defect. The prose lane's must-fix items were resolved or dispositioned in `AUDIT_LEDGER.md`. Process-history language is absent from reader-facing prose; AI audits are described as process evidence. Reopened 2026-09-15 for the retitle and prose rewrite; a cold prose-quality lane graded title, abstract, introduction, and README and returned PASS, and its precision fixes were applied. Any further material claim edit reopens A1. |
| R1 — release and stewardship | **PASS** | `code/verify_reproduction.py` reproduces the frozen certificate (16 hashed artifacts, 999,999 endpoint and 1,999,998 half-interval checks); `paper/main.pdf` is a deterministic double build; `MANIFEST.sha256` covers every tracked file; links, CFF mechanics, and hygiene verified. The immutable `v0.1.0` tag points to audited commit `0746f6df69cc7c7b551ef47dffbd8436f0c1a1aa`. Two pre-Release GitHub tag zipballs match at 468,629 bytes, SHA-256 `b0b18e255fff92a03842872af2647daea610cd59a46f1f56ee8c22b86153cd82`. Zenodo published version DOI `10.5281/zenodo.22783896`; its public file has the same size and SHA-256, provider checksum `md5:9a9897afc6286243d560b42e031de45a`, and is byte-identical to the pinned zipball. Record title, creator, version, date, license, resource type, and repository link match. The archived-state audit reported 12 pass, 0 warnings, 0 failures. The public-site listing and the living-metadata push are recorded below. |

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
| Local edits, builds, tests | agent | complete; final clean admitted-state audit gates publication |
| Default-branch candidate push | Jeff Kline | complete at `0746f6df69cc7c7b551ef47dffbd8436f0c1a1aa` |
| Public tag `v0.1.0` | Jeff Kline | complete: immutable `v0.1.0`; three prepublication tags were retracted while the repository was private, see `CORRECTIONS.md` |
| GitHub Release | Jeff Kline | complete: `v0.1.0`, published 2026-09-16 |
| Zenodo portal | Jeff Kline (authenticated portal) | complete: version DOI `10.5281/zenodo.22783896` |
| Public-site listing | Jeff Kline | authorized separately; verified before this verdict was pushed |
| Living-metadata push | Jeff Kline | authorized separately; reconciliation committed at `7f610bef364b2ab7400cc7ca9a9629fbe7f75289`, verdict publication gated on the final clean audit |

## Archive route

**Zenodo GitHub integration.** The repository was enabled before the GitHub
Release. GitHub's canonical `v0.1.0` tag zipball was downloaded twice before
the Release and the two copies matched at 468,629 bytes, SHA-256 `b0b18e255fff92a03842872af2647daea610cd59a46f1f56ee8c22b86153cd82`.
Zenodo's published file, `jeff-kline/truncated-totient-eigenvector-v0.1.0.zip`,
is byte-identical to those pinned bytes and carries provider checksum
`md5:9a9897afc6286243d560b42e031de45a`. The separately generated deterministic
`git archive` is 467,285 bytes with SHA-256 `583d559b21b82a8dfb714f5e800b976ae230382dc1b9a7e2f5a7a3fb5576de6d`; it is a secondary check,
not the provider identity target.

## State transitions

| State | Condition | Status |
|---|---|---|
| DRAFT → CANDIDATE | P1, A1, and pre-freeze R1 pass; prose and artifacts agree. | **reached 2026-09-15** |
| CANDIDATE → TAGGED | Freeze one clean commit; create one immutable tag. | **reached: `v0.1.0` → `0746f6df69cc7c7b551ef47dffbd8436f0c1a1aa`** |
| TAGGED → ARCHIVED | Archive the tagged tree; verify the download byte-for-byte. | **reached: DOI resolves, metadata matches, provider bytes are identical; archived audit 12/0/0** |
| ARCHIVED → ADMITTED | Reconcile living surfaces; commit the verdict; final clean audit. | **reached: reconciliation committed at `7f610bef364b2ab7400cc7ca9a9629fbe7f75289`; final publication gated on the clean admitted-state audit and the verified site listing** |
