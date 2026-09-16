STAGE INITIAL
VERDICT NOT-BROKEN (Claim A and Claim B). Neither attack produced a counterexample. This is not proof verification.

CLAIM A — evidence
- Checked n=1 by hand: R_1=[1], Q_1=[1], v_1=[1], h_1=[1], so the residual is 0 (no conflict; the claim is a limit).
- Dense numerics (numpy eigh), n in {2,3,5,10,20,50,100,200,400,800,1600,2400}. Values of n*||r||_inf:
  0.171, 0.071, 0.223, 0.676, 0.866, 0.945, 0.971, 0.986, 0.9930, 0.99650, 0.99825, 0.99922.
  The deficit 1 - n*||r||_inf falls roughly like 1.9–2.8/n. It approaches 1 from below with no overshoot.
- Fixed vs. growing coordinate: for every n >= 5 the sup-norm sits at the growing coordinate k=n, never at a fixed k.
  Structural reason, which I checked directly from the definition: column n of R_n is e_n, since floor(j/n)>=1 only when j=n.
  So n*r_n = 1 - n(v^T h)v_n(n), and the claim reduces to n*v_n(n) -> 0 together with the fixed coordinates staying o(1/n).
  Numerically both hold. The dominant eigenvector is positive in every case, and the spectral gap lambda1/lambda2 grows roughly like 5n, so the eigenvector is numerically well conditioned.
- Normalization attack: the residual doesn't depend on the sign or scale of v, since it uses the unit v in the projector. No ambiguity.

CLAIM B — evidence
- U(1)=1-C*1*0=1 (checked). U is continuous at integers because the new term carries the factor (1-a^2/t^2)=0 there.
- On [m,m+1), U(t) = t - C*S0(m) + C*S2(m)/t^2. This is convex in t, so each interval's maximum is at an endpoint and its minimum is at an endpoint or at t_c=(2C*S2)^{1/3}.
  I evaluated U exactly in this form for every interval m=1..10^7-1, including every interior critical point.
- Near t=1: U'(1)=1-2C≈-3.26<0, so U drops below 1 immediately. On [1,2) the minimum is 0.302.
- Results (sup U / inf U):
  [1,2): 1 / 0.302;  [2,10): 0.403 / 0.080;  [10,1e2): 0.139 / 0.0091;  [1e2,1e3): 0.0356 / -9.6e-6;
  [1e3,1e4): 0.0067 / -0.00122;  [1e4,1e5): 0.00156 / -0.00066;  [1e5,1e6): 3.9e-4 / -3.3e-4;
  [1e6,2e6): 1.8e-4 / -6.8e-5;  [2e6,5e6): 7.8e-5 / -9.4e-5;  [5e6,1e7): 5.8e-5 / -5.4e-5.
  Global over t in [1,1e7]: max over t>=2 is 0.40299 (at t=2); min is -0.001216 (near t≈3144). |U|=1 only at t=1.
- Precision attack (the unbounded real interval): the prime-product truncation of G matters.
  dU/dG ≈ -t/G, so at t=1e7 an error of 1e-9 in G shifts U by about 0.014.
  A first run with a crude tail estimate (N=2e6, tail ≈ 1/(N log N)) gave a spurious negative drift, with U ≈ -0.004 at t≈2e6.
  I redid it with the tail computed exactly as sum_{p>N} p^-2 = P(2) - partial sum (mpmath primezeta; dropped terms ~1e-16).
  That gives G=0.7044422009991654, which agrees with my recollection of OEIS A065463 (not checked against the source).
  I also rewrote the cumulative sums around the mean G to avoid cancellation. With both changes the drift is gone and U oscillates toward 0.
  Per the SANITY rule, I don't treat the truncation artifact as a counterexample.
- Heuristic, not proof: write g = 1*h with h(p)=-1/(p+1), h(p^k)=0 for k>=2. Then
  U(t) = C(2t/3) sum_{d>t} h(d)/d + (C/2) sum_{d<=t} h(d) + C sum_{d<=t} h(d)E(t/d),
  where E(x) is the O(1/x) Euler–Maclaurin remainder of sum_{m<=x}(1-m^2/x^2). Every term looks o(1)–O(1), consistent with U -> 0.
  So the real content of B is the explicit constant 1 at small and moderate t. The numerics support it, with a large margin for t>=2 (max 0.403).

COVERAGE
- A: n <= 2400 only. The limit statement can't be refuted by finite n. I tested fixed vs. growing coordinates, normalization, positivity, and the n=1 convention.
- B: every real t in [1, 1e7] was checked with the per-interval exact formula in float64 plus the precision safeguards above. Nothing was checked for t > 1e7, so beyond that the claim is untested and rests on the asymptotic heuristic only.
  Float64 error estimate for U at t<=1e7 is about 1e-9, far below the margins.

DEPENDENCIES
- numpy linear algebra (eigh), float64.
- The value of G via the mpmath prime zeta function P(2) plus an explicit prime sieve to 1e7.
- Claim A's trend is extrapolated from n <= 2400.

SOURCES/TOOLS EXPOSED
- Local venv Python (~/.venvs/claude) with numpy and mpmath.
- No web, no email, no proof bundle, no nested agents.
- From memory only (not consulted): the OEIS A065463 value of G.

ACTIVE TIME
About 6–7 minutes including compute. This is slightly over the 5-minute cap; the overrun was the precision re-run for G.
