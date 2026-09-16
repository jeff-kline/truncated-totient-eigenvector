# Admission record

**Current verdict: NOT ADMITTED.**

**Release state:** DRAFT

**Version:** 0.1.0 (candidate; no tag, archive, or DOI exists)

Admission is a project-defined release decision under Jeff Kline's
["A Public Standard for This Work"](https://jeff-kline.github.io/posts/research-program/index.html).
It means the claim, evidence, prior-work record, reproducibility materials,
citation, and correction policy passed the gates below against one frozen
commit. **It is not peer review, a correctness certificate, or proof of global
novelty.**

## Gate status

| Gate | Status | Evidence and disposition |
|---|---|---|
| P1 — prior work and credit | **OPEN** | The 2020 paper is the source of the matrices, identities, sandwich, Corollary 9, and conjecture. Ramaré 2015 and Lee–Leong supply the analytic inputs. A bounded release-time prior-art lane is pending. |
| A1 — claim and artifact consistency | **OPEN** | Paper, README, and CFF were rewritten on 2026-09-15 to state the same principal claim. Fresh-context claim/prose, proof, and reproducibility lanes are pending. |
| R1 — release and stewardship | **OPEN** | Reproduction runner passes under the release layout (16 frozen artifacts). Deterministic PDF build, manifest, tag, archive, and DOI are pending. |

## Claim boundary

- **Proved here:** the 2020 conjecture; the coordinatewise limit profile
  `U`; the eigenvalue constant `G/3`; the exact identity
  `Lambda_n v_n^T mu_n = v_n(1)` and the `n^-3` asymptotic; the spectral
  remainder bound; the exact convolution obstruction identity.
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
  the scalar tail proposal and its full-proof audit came from the same
  provider.
- The auditor did not rederive every term of the finite-`N` Mellin formula;
  the adjudication supplies the calculation explicitly.
- Ivić's Theorem 12.7, the textbook source for the effective Mertens bound,
  was not inspected directly; the bound was source-checked against Ng's
  lecture notes and Lee–Leong's explicit theorem.
- The prior-art review is bounded; inaccessible databases are not treated as
  negative evidence.

## Execution boundary

Permission for one action never implies permission for the next.

| Action | Owner | Status |
|---|---|---|
| Local edits, builds, tests | agent | in progress |
| Default-branch candidate push | Jeff Kline | not authorized |
| Public tag `v0.1.0` | Jeff Kline | not authorized |
| GitHub Release | Jeff Kline | not authorized |
| Zenodo portal | Jeff Kline (authenticated portal) | not started |
| Public-site listing | Jeff Kline | not authorized |
| Living-metadata push | Jeff Kline | not authorized |

## Archive route

Zenodo GitHub integration. The repository must be enabled in Zenodo before
the GitHub Release. The GitHub `zipball/v0.1.0` will be downloaded twice and
pinned before the Release; the Zenodo file must equal those bytes.

## State transitions

| State | Condition | Status |
|---|---|---|
| DRAFT → CANDIDATE | P1, A1, and pre-freeze R1 pass; prose and artifacts agree. | pending |
| CANDIDATE → TAGGED | Freeze one clean commit; create one immutable tag. | pending |
| TAGGED → ARCHIVED | Archive the tagged tree; verify the download byte-for-byte. | pending |
| ARCHIVED → ADMITTED | Reconcile living surfaces; commit the verdict; final clean audit. | pending |
