# Release plan

Working plan for admitting this repository under Jeff Kline's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
This file is a living record; `ADMISSION.md` carries the verdict.

## Principal claim and sources

- **Claim.** The 2020 dominant-eigenvector conjecture is true: for the
  truncated-totient Gram matrix `Q_n = R_n^T R_n`, its positive unit dominant
  eigenvector `v_n`, and `h_n(k) = 1/k`,
  `lim n || h_n - (v_n^T h_n) v_n ||_inf = 1`.
- **Authoritative proof.** `paper/main.tex` (typeset), with the full
  examined argument in `proof/proof-bundle.md` and component notes
  `proof/A0*.md`. The scalar inequality `|U(t)| <= 1` is closed by the exact
  integer certificate `code/certify_scalar.py` for `1 <= t <= 10^6` and by an
  analytic tail bound `202847/300000` for `t >= 10^6`.
- **Computation.** `results/scalar-certificate.json` is the frozen certificate
  receipt; `code/verify_reproduction.py` checks frozen hashes and reruns the
  certificate in a temporary directory without overwriting the receipt.
- **Literature record.** `audit/campaign/LITERATURE.md` (source locators),
  `ref/kline4.tex` (the 2020 paper's TeX source), Ramaré 2015 and its 2019
  corrigendum (URLs and hashes recorded; PDFs not redistributed), Lee–Leong
  (arXiv). The author's private August 2026 working repository proved the
  eigenvalue constant and the lower bound `liminf >= 1` and left the upper
  bound open; it is superseded, not cited.
- **Current public claim surfaces.** None. No push, tag, release, archive,
  DOI, or site listing exists yet.

## State

`CANDIDATE` as of 2026-09-15. Advance only `DRAFT -> CANDIDATE -> TAGGED -> ARCHIVED -> ADMITTED`.

## Gates

### P1 — prior work and credit

| Check | Status | Notes |
|---|---|---|
| Closest work | PASS | Compare with the 2020 paper's Prop. 8 and Cor. 9; Redheffer-type and totient-matrix spectral literature; bounded search for any other resolution of the exact conjecture. |
| Original sources | PASS | Ramaré 2015 Thm 1.2 and corrigendum read during the campaign; Lee–Leong Thm 1.1 (9) cited for the effective Mertens bound; Ivić Thm 12.7 not inspected directly. |
| Contribution type | PASS | New proof of a stated conjecture; new asymptotic constants; one obstruction identity. |
| Novelty | PASS | Qualify to the searched corpus. |
| Residuals | PASS | Name inaccessible databases. |

### A1 — claim and artifact consistency

| Check | Status | Notes |
|---|---|---|
| Principal claim | PASS | Theorem 3.1 in the paper; README; CFF abstract must agree. |
| Scope | PASS | Unconditional; uses PNT-strength Möbius cancellation and Ramaré's explicit bound; no RH. |
| Evidence | PASS | Separate proof, exact certificate, exploratory numerics (`code/probe.py`, `results/A01.*`). |
| Credit | PASS | 2020 paper identities `R_n mu = e_1`, `Q_n mu = e_1` are prior; Gegenbauer-type totient sum is classical. |
| Public prose | PASS | Remove working-draft, coordinator, owner, external-audit, lane language from the paper and README. |
| Metadata | PASS | Title, author, version, date consistent across paper, README, CFF. |
| Adversarial check | PASS | Campaign audits preserved in `audit/campaign/`; fresh release-time lanes pending. |

### R1 — release and stewardship

| Check | Status | Notes |
|---|---|---|
| Reproduction | PASS | `code/verify_reproduction.py` must pass under the release layout. |
| Artifact integrity | PASS | Deterministic double build of `paper/main.pdf`; `MANIFEST.sha256`. |
| Hygiene | PASS | No private paths, placeholders, or campaign-relative paths. |
| Stewardship | PASS | `CORRECTIONS.md`, `CITATION.cff`, `ADMISSION.md`, `AUDIT_LEDGER.md`. |
| Tag | OPEN | `v0.1.0` at the audited commit. |
| Archive | OPEN | Zenodo GitHub integration; pin GitHub `zipball/v0.1.0` twice before the Release. |
| Citation | OPEN | Version DOI after Zenodo mints it. |
| Metadata | OPEN | Verify Zenodo record fields. |

## Archive route

Zenodo GitHub integration. Jeff Kline enables the repository in Zenodo before
the GitHub Release. No manual deposit. `CITATION.cff` carries no DOI and no
`date-released` until publication.

## Ownership

| Action | Owner |
|---|---|
| Local edits, builds, tests, integration of audit findings | agent |
| Review-branch push | Jeff Kline authorizes; agent executes on exact authorization |
| Default-branch update | Jeff Kline authorizes |
| Public tag `v0.1.0` | Jeff Kline authorizes (freeze bundle) |
| GitHub Release | Jeff Kline authorizes (freeze bundle) |
| Zenodo portal | Jeff Kline (authenticated portal; agent never opens it) |
| Public-site listing | Jeff Kline authorizes (admission bundle) |
| Living-metadata push | Jeff Kline authorizes (admission bundle) |

Audit agents are read-only. The root agent integrates findings and applies all
edits.

## Sequence

1. Resolve checkout (done: local release checkout of the private repo `jeff-kline/truncated-totient-eigenvector`).
2. Read standard, campaign, paper, predecessor (done).
3. Rewrite abstract, introduction, README (done 2026-09-15).
4. Bounded read-only audits in parallel (done 2026-09-15: four lanes; see AUDIT_LEDGER.md).
5. Integrate findings; freeze one clean candidate; run candidate audit (done 2026-09-15).
6. Freeze bundle: push, tag, GitHub Release (explicit authorization).
7. Verify Zenodo record, DOI, byte identity; archived-state audit.
8. Admission bundle: site listing, living metadata; admitted-state audit; verdict.
