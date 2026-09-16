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
- 2026-09-15: Before publication, the title was changed from "A proof of the
  2020 dominant-eigenvector conjecture for truncated-totient matrices" to
  "The Perron vector of a totient Gram matrix and its harmonic
  approximation", so that the title names the object and the result rather
  than the conjecture's date. The abstract, introduction, and README were
  rewritten for plainness. No mathematical statement changed. Gate A1 was
  reopened for a prose-quality audit.
- 2026-09-15: Before publication, the abstract, introduction, Section 3
  lead-in, Section 4, and README were revised to display the conjectured
  limit and to name Proposition 8 and Corollary 9 of the 2020 paper beside
  the asymptotics that replace them. No mathematical statement changed. An
  annotated tag `v0.1.0` at the earlier commit
  `12cb7a0db8f45d57229a59dcd2f7dca05356fe5a` had been pushed to the private
  repository with no GitHub Release, archive, or DOI; it was retracted before
  any publication and recreated at the revised commit. No public tag has ever
  been moved.
