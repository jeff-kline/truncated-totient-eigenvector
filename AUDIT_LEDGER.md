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

## Open audits

- Release-time fresh-context lanes: claim and public prose; proof and
  parameters; citations and bounded prior art; reproducibility and release
  mechanics.
- Deterministic PDF build and visual inspection.
- Candidate-state mechanical audit; final clean admitted-state audit.
