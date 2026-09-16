# R02 substantive proof audit

STAGE: PROOF-AUDIT

VERDICT: VERIFIED

CLAIM:

All four claims in `review/uniform-statement-v1.md`, with absolute asymptotic constants, the stated phi(1)=1 convention, positive Euclidean-unit Perron vector, and no arithmetic cancellation assumptions.

| Claim | Status | Basis |
|---|---|---|
| 1: uniform vector linearization with l2 error O(n^(-3/2)L^3) | VERIFIED | Sections 1–4 below establish every size bound and the exact first-coordinate subtraction. |
| 2: projection linearization with the same l2 error | VERIFIED | Exact projection identity and the product bound in section 5. |
| 3: scalar expansion with remainder o(1/n) | VERIFIED | Explicit numerator and denominator error bounds in section 5. |
| 4: n*r_n tends to 1 and the stated liminf lower bound | VERIFIED | Exact final column and a uniform coordinate error, section 6. |

The candidate proof's argument is valid. This report supplies details for its abbreviated elementary estimates and perturbation step; it does not replace its argument. The prior NOT-BROKEN verdict is not used as evidence of correctness.

EVIDENCE:

## 1. Definitions, divisor bounds, and S

All norms below are Euclidean vector norms or their induced operator norms unless marked Frobenius. Let T_j=tau(j), and let K_n=sum_{k<=n}1/k=O(L). Inclusion-exclusion gives

`R(j,k)=sum_{d|j} mu(d)*floor(j/(dk))`,

`phi(j)/k=sum_{d|j} mu(d)*j/(dk)`.

Both identities include j=1. Subtraction yields `|E(j,k)|<=T_j`. Also both R(j,k) and phi(j)/k lie in [0,j/k], so `|E(j,k)|<=j/k`; this is a bound on their difference, without an extra factor of two.

The elementary estimates needed below are

`sum_{j<=n}T_j <= n*K_n = O(nL)`,

`sum_{j<=n}j*T_j = O(n^2 L)`,

`sum_{j<=n}T_j^2 = O(n L^3)`.

The first follows by counting factorizations j=ab, and the second follows by j<=n. For the third, T_j^2<=d_4(j) prime by prime: for an exponent a>=0, `(a+1)^2<=binomial(a+3,3)`, since the difference is `(a+1)*a*(a-1)/6>=0`. Counting four-factor products then gives

`sum_{j<=n}d_4(j) <= n*sum_{a,b,c<=n}1/(abc) = n*K_n^3`.

Here and below these estimates have numerical absolute constants.

For completeness, S comparable to n^3 needs no unverified totient asymptotic. Let A count ordered coprime pairs in [1,n]^2. A noncoprime pair is divisible in both coordinates by at least one integer d>=2. A union bound gives

`n^2-A <= sum_{d=2}^n floor(n/d)^2 <= n^2*sum_{d=2}^infinity d^(-2) <= 3n^2/4`.

The last bound uses 1/4 plus the integral of x^(-2) from 2 to infinity. Since `A=2*sum_{j<=n}phi(j)-1`, we have `sum phi(j)>=n^2/8`. Cauchy–Schwarz implies `S>=n^3/64`. Conversely `S<=sum j^2<=n^3`. Also `1<=H^2<=2`.

Every entry in row n of R is at least one, hence every entry of Q is positive. The positive unit Perron vector exists and is unique, and its sign in the subsequent perturbation estimate is unambiguous. At n=1 all relevant errors vanish; the asymptotic arguments only require sufficiently large n.

## 2. Matrix and vector estimates

For each row, split the sum at m=j/T_j>=1. The terms with k<=m contribute at most j*T_j. Extending the remaining sum to infinity and using `sum_{k>m}k^(-2)<=2/m` bounds the tail by 2j*T_j. Therefore

`sum_{k<=n}|E(j,k)|^2 <= 3j*T_j`,

`||E|| <= ||E||_F = O(n L^(1/2))`.

The separate column bound follows from the uniform divisor bound:

`max_k ||E(:,k)|| <= (sum T_j^2)^(1/2) = O(n^(1/2)L^(3/2))`.

For the weighted product, `|(Eh)_j|<=T_j*K_n`. Thus

`||Eh|| = O(n^(1/2)L^(5/2))`.

Since ||a||=sqrt(S)=Theta(n^(3/2)), these estimates yield precisely the candidate's bounds

`||b|| = ||E^T a|| = O(n^(5/2)L^(1/2))`,

`max_k |b_k| = O(n^2 L^(3/2))`.

The columnwise bound is valid, although it is not needed for the four conclusions. With q=b/S and F=C/S, the bounds needed in the perturbation step are

`||q||=O(n^(-1/2)L^(1/2))`,

`||F||=O(L/n)`.

## 3. Rank-one perturbation, with the spectral step justified

Expanding R^T R exactly gives

`Q/S = h h^T + h q^T + q h^T + F = h h^T + Delta`,

where `||Delta||=O(epsilon)` for `epsilon=n^(-1/2)L^(1/2)`. This follows from bounded H and the estimates above, since epsilon tends to zero and L/n=epsilon^2.

Let rho=lambda/S be the largest eigenvalue. Maximizing the Rayleigh quotient gives `|rho-H^2|<=||Delta||`, so rho is bounded away from zero and `lambda=SH^2*(1+O(epsilon))`.

Set u=h/H and let P be orthogonal projection onto its orthogonal complement. Applying P to the eigen-equation gives `rho*Pv=P*Delta*v`, and therefore `||Pv||=O(epsilon)`. The positivity of u and v gives u^T v>0. Unit normalization then gives `u^T v=sqrt(1-||Pv||^2)`, and hence `||v-u||=O(epsilon)`. This proves the candidate's vector estimate without an unexamined perturbation theorem. It also proves that both t=h^T v and v_1 are bounded above and away from zero; in particular `lambda*v_1=Theta(n^3)`.

Consequently

`||Ev|| <= ||Eh||/H + ||E||*||v-h/H||`

`          = O(n^(1/2)L^(5/2)) + O(n^(1/2)L)`

`          = O(n^(1/2)L^(5/2))`.

It follows that `|b^T v|=|a^T Ev|=O(n^2 L^(5/2))`. All constants here remain independent of n.

## 4. First-coordinate subtraction and claim 1

Since R(j,1)=phi(j), column 1 of E is exactly zero. Thus b_1=0 and row 1 of C=E^T E is zero. The eigen-equation and its first coordinate read

`lambda*v = S*h*t + h*(b^T v) + b*t + C*v`,

`lambda*v_1 = S*t + b^T v`.

Let beta=(b^T v)/(S*t). The preceding estimates imply `beta=O(L^(5/2)/n)=o(1)`. Therefore the coefficient in the candidate proof is exactly

`t/(lambda*v_1) = (1/S)*(1+beta)^(-1)`.

Subtracting h times the first-coordinate equation and dividing by lambda*v_1 gives

`v/v_1 = h + q + d`,

`d = ((1+beta)^(-1)-1)*q + C*v/(lambda*v_1)`.

The first term is `O((L^(5/2)/n)*n^(-1/2)L^(1/2))=O(n^(-3/2)L^3)`. For the second,

`||Cv|| <= ||E||*||Ev|| = O(n^(3/2)L^3)`,

and its denominator is Theta(n^3). Thus `||d||=O(n^(-3/2)L^3)`, proving claim 1 at its stated logarithmic scale. The exact first-coordinate identity also gives d_1=0.

## 5. Projection identities and claims 2–3

Write w=v/v_1=h+z with z=q+d and z_1=0. Since v=w/||w|| and w_1=1,

`r = h - ((h^T w)/||w||^2)*w`,

`r_1 = (h^T z+||z||^2)/(H^2+2h^T z+||z||^2)`.

These are exact and agree with the candidate's normalization convention. By Cauchy–Schwarz and section 2,

`|h^T q|=|a^T Eh|/S=O(L^(5/2)/n)`.

Also `||q||^2=O(L/n)` and `||d||=O(n^(-3/2)L^3)`. Define s=h^T z and u=||z||^2. Then

`s=O(L^(5/2)/n)`, `u=O(L/n)`,

so the denominator is H^2+o(1), bounded away from zero, and `r_1=O(L^(5/2)/n)`.

To check the small-o assertion quantitatively, set N0=h^T q+||q||^2. The numerator error is

`s+u-N0 = h^T d + 2q^T d + ||d||^2`

`= O(n^(-3/2)L^3 + n^(-2)L^(7/2) + n^(-3)L^6)`.

The denominator correction contributes at most `O(n^(-2)L^5)`, since both s+u and 2s+u are `O(L^(5/2)/n)` and H^2 is bounded away from zero. Thus, in particular,

`r_1 - N0/H^2 = O(n^(-3/2)L^3 + n^(-2)L^5) = o(1/n)`.

This proves claim 3, including the retained ||q||^2 term; discarding that term would not be justified by the available norm bound.

The exact vector projection identity also gives

`r = r_1*h -(1-r_1)(q+d) = r_1*h -q +e`,

`e = r_1*q -(1-r_1)d`.

Here `|r_1|*||q||=O(n^(-3/2)L^3)` and `|1-r_1|*||d||` has the same bound. This proves claim 2. Since the l-infinity norm is at most the l2 norm, `sup_{k<=n} n*|e_k|=O(n^(-1/2)L^3)=o(1)`; the uniformity used in the final step is valid.

## 6. Endpoint and claim 4

Exactly R(:,n)=e_n, including the n=1 convention. Hence

`b_n=phi(n)-S/n`, `q_n=phi(n)/S-1/n`.

Taking coordinate n in claim 2 and multiplying by n yields

`n*r_n = r_1 + 1 - n*phi(n)/S + n*e_n`.

The three terms other than 1 tend to zero: `r_1=O(L^(5/2)/n)`, `n*phi(n)/S=O(1/n)` by phi(n)<=n and section 1, and `n*e_n=O(n^(-1/2)L^3)`. Therefore n*r_n tends to 1. Finally `n*||r||_infinity>=|n*r_n|` proves the stated liminf lower bound. No matching upper bound is asserted or verified.

COVERAGE:

Audited the entire candidate note against all four formal claims. Established the entrywise divisor estimates, divisor moments, S bounds, Frobenius and column bounds, weighted matrix product, rank-one perturbation with sign and normalization, coefficient expansion, vector remainder, scalar denominator expansion, uniform coordinate error, and moving endpoint. Checked positivity and the phi(1) convention. The note mentions other work and the arithmetic supremum; no referenced note was opened, and those subjects are outside this verdict. No numerical experiments were used as proof evidence.

DEPENDENCIES:

Discharged within this report: inclusion-exclusion for coprimality, elementary divisor counting, a coprime-pair union bound, Cauchy–Schwarz, induced/Frobenius norm inequalities, and the symmetric-matrix Rayleigh quotient and eigenvector projection identities. Perron positivity applies because Q is entrywise strictly positive. No unresolved arithmetic estimates, cited papers, external sources, or previously reviewed results are required. All limits use only fixed powers of log(2n) divided by positive powers of n.

ERRATA:

None required for the four formal claims. The candidate's short references to divisor estimates and rank-one perturbation are correct; the details above discharge them. No replacement argument is needed or proposed. Verification is limited to correctness of this statement and proof, not novelty, significance, a matching upper bound, or the original conjecture.

EXPOSURE:

- Audited actual proof: `/Users/klinellc/Documents/hm-ai/unital-eigenvector/notes/A04-uniform-linearization.md`; SHA256 verified as `2086e36776254025e59e97433fd7c4ca3f7ea3fc85a04b97df25cd05ee8776ca`.
- Formal packet reread: `/Users/klinellc/Documents/hm-ai/unital-eigenvector/review/uniform-statement-v1.md`; SHA256 `f2d2909b8ffb97f46bf9606166502aa0b1f19da0b7e233c371ed3474cf74deed`.
- Prior initial report: `/Users/klinellc/Documents/hm-ai/unital-eigenvector/review/R01-initial.md`, retained in this same conversation from the preceding isolated pass. Its bytes were hashed, not edited; SHA256 matches the user-supplied seal `473478306181197f3dabee600f8062b51b5805b9a635d85e1e5f82c4fd1aa94e`. The coordinator's `review/SEALS.md` itself was not opened.
- Skill: `/Users/klinellc/.codex/skills/cold-examiner/SKILL.md`, already read during the preceding turn and retained in context. This is a proof-aware continuation, not a newly isolated or independently instantiated examiner despite the R02 report label.
- No other notes, results, reviews, repository files, web sources, or author's material were inspected. Tools used: UTC clock, shell reads and SHA256 hashing, and patch creation of this new report. No nested agents, model overrides, email, or external communication.

RESOURCES:

Audit start observed at 2026-09-14 02:53:29 UTC; intermediate clock at 02:54:15 UTC; substantive audit and report save completed at 02:56:47 UTC, 3 minutes 18 seconds after the start. This was one reserved substantive worker turn, within the ten-active-minute limit. No numerical computation, search, or test workload was launched; computation was limited to short file hashing and tool/file operations. Shell CPU usage was not separately instrumented. The earlier initial turn's numerical probe was not rerun and is not evidence for this verdict. Only this timing entry and final file verification followed completion.
