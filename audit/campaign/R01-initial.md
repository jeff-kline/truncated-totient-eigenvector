# R01 isolated failure search

STAGE: INITIAL

VERDICT: NOT-BROKEN

No counterexample to any of the four claims was found. This is a bounded initial failure search, not an audit or validation of the author's unseen proof. Failure to find a counterexample is not confirmation of the theorem.

EVIDENCE:

- **Definitions and degenerate cases.** The last row of R has every entry at least one, so Q has strictly positive entries and the positive unit Perron vector is well defined. At n=1, q=r=d=e=0. The fourth claim is asymptotic and makes no claim that n*r_n is close to one at n=1.
- **Normalization attack on claims 1–3.** The first column of E is zero, hence q_1=0. Write w=v/v_1=h+x, with x_1=0. Exact algebra gives
  `r_1=(h^T x+||x||^2)/(H^2+2 h^T x+||x||^2)` and
  `r=r_1 h-(1-r_1)x`.
  These identities test both the sign of q in claim 2 and the quadratic term in claim 3. Neither sign nor quadratic term produces a contradiction. Replacing the denominator by H^2 does require a small scalar h^T q, rather than merely a small norm of q; the bounds below address that potential obstruction.
- **Remainder-size attack on claim 1.** A crude uniform divisor bound initially loses a logarithm. That loss is a weakness of the crude estimate, not a counterexample or a gap in an unseen proof. Let tau be the divisor-counting function and F=E^T E/S. Inclusion-exclusion and nonnegativity give `|E_jk| <= min(tau(j),j/k)`. Consequently `||E||_F^2=O(n^2 L)`, because summing the square of that minimum over k gives O(j*tau(j)). Also `||(E h)||=O(sqrt(n)*L^(5/2))`, using `|(E h)_j|<=tau(j)*O(L)` and `sum tau(j)^2=O(n L^3)`. Together with S comparable to n^3 these yield
  `||q||=O(n^(-1/2)*L^(1/2))`,
  `|h^T q|=O(L^2/n)`,
  `||F||=O(L/n)`, and
  `||F h||=O(n^(-3/2)*L^3)`.
  The scalar bound uses `sum j*tau(j)=O(n^2 L)`.
  As an internal consistency check, the eigenvector equation and its first coordinate give the exact relation
  `D= lambda/S = (h+q)^T w`,
  `w-h=-(q^T w/D)q+q+F w/D`.
  The normalized matrix tends in operator norm to h h^T, whose nonzero eigenvalue is bounded away from zero; its positive leading eigenvector therefore gives bounded ||w|| and D bounded away from zero. The displayed relation first gives `||w-h||=O(n^(-1/2)*L^(1/2))`, then `|q^T w|=O(L^2/n)` and `||F(w-h)||=O(n^(-3/2)*L^(3/2))`. Thus this attack did not expose a remainder larger than claim 1's stated scale.
- **Claim 2 check.** With x=q+d, its exact error is `e=r_1 q-(1-r_1)d`. The preceding bounds and the exact normalization identity give `r_1=O(L^2/n)`. There is no larger normalization term forcing a failure of the claimed scale.
- **Claim 3 check.** Under those bounds, replacing x=q+d by q in the numerator costs `O(n^(-3/2)*L^3)` plus smaller terms. Replacing the denominator by H^2 costs `O(n^(-2)*L^4)`. Both are o(1/n). This resolves the specific denominator-correction attack within this pass.
- **Moving-coordinate attack on claim 4.** Exactly `q_n=phi(n)/S-1/n`, since column n of R is supported only at row n. Claim 1 therefore gives `w_n=phi(n)/S+d_n`, so `n*w_n -> 0`. Since `(h^T v)*v_n = ((h^T w)/||w||^2)*w_n` and the prefactor is bounded, this is consistent with `n*r_n -> 1`. The infinity-norm consequence follows from `||r||_infinity >= |r_n|`. No cancellation hypothesis on phi(n) is needed for this check.
- **Finite numerical probes.** Constructed R and phi by exact integer gcd counts at n=1,2,3,5,10,20,40,80,160. Applied Q through R and R^T and used floating-point normalized power iteration, stopping at coordinate change below 1e-14. These are exploratory numerical checks, not interval-certified counterexample tests. For n=2,10,40,160 respectively, `n*r_n` was approximately -0.17082039, 0.67647963, 0.92594176, 0.98233089. Small-n negativity is not an asymptotic counterexample. At the same n, `||d||/(n^(-3/2)*L^3)` was approximately 0.12531, 0.010753, 0.0050883, 0.0028373; the analogous error ratio for claim 2 was 0.11870, 0.010782, 0.0047183, 0.0025377. The quantity `n*(r_1-(h^T q+||q||^2)/H^2)` was approximately 0.10557, 0.029496, 0.015149, 0.0076583. No finite probe supplies a universal asymptotic conclusion.

COVERAGE:

Attacked all four claims through definition checks, first-coordinate normalization, quadratic and denominator corrections, logarithmic remainder estimates, and the endpoint k=n. Checked small n numerically. Did not inspect any author's proof, certificates, other reviewers' findings, fixed-coordinate asymptotics, or the unasserted conjecture. The internal consistency derivations above are not a substitute for the coordinator's separate proof-audit stage.

DEPENDENCIES:

Used elementary finite-dimensional symmetric-matrix perturbation and divisor estimates. The divisor estimates can be obtained from `sum_{j<=n} tau(j)<=n*sum_{d<=n}1/d` and `tau(j)^2<=d_4(j)`, followed by a four-factor counting bound `sum_{j<=n}d_4(j)=O(n L^3)`. The latter pointwise inequality follows prime by prime from `(a+1)^2<=binomial(a+3,3)`. For S comparable to n^3, the upper bound follows from phi(j)<=j. For the lower bound, at most `n^2*sum_{d>=2}1/d^2` ordered pairs in [1,n]^2 fail coprimality by a union bound; this sum is strictly below n^2. Thus `sum phi(j)` is bounded below by a positive constant times n^2, and Cauchy–Schwarz gives the lower bound for S. No external source verification was performed or needed for these internal probes. No unresolved source claim is being used to assert REFUTED or VERIFIED.

EXPOSURE:

- Formal packet: `/Users/klinellc/Documents/hm-ai/unital-eigenvector/review/uniform-statement-v1.md`, headed “Statement packet: uniform linearization, version 1.” Read the entire packet once.
- Skill: `/Users/klinellc/.codex/skills/cold-examiner/SKILL.md`. Read the entire skill once.
- Other exposure: the supplied worker assignment, global user instructions, and ordinary session/tool context. No notes, author's proof, other mathematical results, other reports, web sources, or repository files were read.
- Tools: shell `cat` for the two authorized inputs; UTC clock reads; one self-contained Python numerical probe; patch tool to create this report. No nested agents, model overrides, email, or external communication.

RESOURCES:

First observed clock: 2026-09-14 02:48:25 UTC, immediately after reading the two inputs. Last pre-report clock: 02:50:16 UTC. The report was composed immediately afterward within the five-active-minute allocation. The only numerical computation reported 0.093998 process CPU seconds, well below 15 CPU seconds. Power iteration required at most 17 iterations in the tested cases. This is the single authorized initial worker turn; stop after saving, with sealing left to the coordinator. Do not modify this initial report after sealing; any later correction belongs in a separate report.
