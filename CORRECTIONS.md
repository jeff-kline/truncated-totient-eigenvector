# Corrections, withdrawals, and supersession

This file records every public version. No public version exists yet.

## Policy

- Minor corrections to living documentation will be dated and described in
  the repository history.
- A material change to a theorem, hypothesis, proof, computation, or claimed
  scope will receive a new semantic version and a new immutable archive.
- A superseded version will remain identifiable and citable. It will not be
  silently replaced.
- If a material error defeats a released principal claim, the living
  repository will mark the claim withdrawn, explain the reason, identify the
  affected versions, and preserve the prior record.
- If earlier or equivalent prior work is found, the claim and credit record
  will be corrected promptly. A narrower novelty statement is treated as a
  successful correction.
- Immutable tags and published archives will never be moved or rewritten. A
  correction will point from the living repository to both the affected
  version and its successor.

## Version history

- 2026-09-14: Proof campaign completed in a local working directory. The
  examined proof bundle, component notes, certificate program, receipt, and
  examination reports were frozen by SHA-256; see `audit/frozen-artifacts.json`.
- 2026-09-15: Release repository `jeff-kline/truncated-totient-eigenvector`
  created (private) and the frozen artifacts relocated into the release layout
  with unchanged bytes. The paper's title, abstract, introduction, and
  appendix were rewritten for readers; no mathematical statement changed.
  This release supersedes the author's unreleased August 2026 working
  repository on the same matrices, which proved the eigenvalue constant and
  the lower bound `liminf >= 1` and left the upper bound open. No push, tag,
  release, archive, or DOI exists.
- 2026-09-15: Four read-only fresh-context release audits (claim and prose;
  proof and parameters; citations and prior art; reproducibility and release
  mechanics) were integrated. The proof lane found no defect. Edits: the
  fixed-coordinate limit was added to the statement of Theorem 3.1 (it was
  already proved in its proof); the Redheffer-matrix spectral literature was
  discussed and cited; bibliographic records were completed; the frozen
  certificate program's historical comments were documented rather than
  edited. State advanced to CANDIDATE. No push, tag, release, archive, or DOI
  exists.
