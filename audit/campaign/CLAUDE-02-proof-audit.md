STAGE PROOF-AUDIT
VERDICT VERIFIED (subject to the caveats below)
This validates the supplied chain A04 -> A05 -> A06 -> A07 -> A08 -> A09 + certify_scalar.py.
I did not repair anything. I found no mathematical gap; only notational slips, listed under minor findings.
Same-provider audit: the A09 mechanism came from an earlier Claude Opus response, and I am also Claude.
My initial statement-only report (NOT-BROKEN) was saved before this bundle was read.

EXACT CLAIM AND SCOPE
The original limit is lim n*||h_n-(v_n^T h_n)v_n||_inf = 1 (Claim A).
The scalar inequality is |U(t)|<=1 for real t>=1, with equality only at t=1 (Claim B).
This audit covers both, and the reduction of A to B.

LINE OF REASONING CHECKED (by hand unless marked)

A04, matrix linearization:
- |E(j,k)|<=2^omega(j)<=tau(j) and |E|<=j/k. This gives ||E||_F=O(nL^{1/2}), column norms O(n^{1/2}L^{3/2}) and ||Eh||=O(n^{1/2}L^{5/2}).
- Rank-one perturbation: ||hb^T+bh^T+E^TE||=O(n^{5/2}L^{1/2}) against the gap SH^2~n^3.
- Column 1 of E is 0, since R(j,1)=phi(j). That makes the first eigen-equation lambda*v_1=S*t+b^Tv exact.
- The subtracted coordinate identity lambda(v_k-v_1h_k)=t*b_k+(E^TEv)_k is also exact.
- ||d||=O(n^{-3/2}L^3). The projection identity for r_1 is exact.
- r=r_1h-q-d+r_1z, so ||e||_2=O(n^{-3/2}L^3), and n||e||_inf=o(1) uniformly in k.
- k=n: column n is e_n, q_n=phi(n)/S-1/n, and n*r_n->1. This gives the liminf only.

A05, large coordinates:
- Derived sum_{j<=y,(j,a)=1}phi(j) = y^2 g(a)/(2zeta(2)) + O(y tau(a)L), with the Euler product (phi(a)/a)prod_{p∤a}(1-p^-2)=g(a)/zeta(2).
- S=c n^3+O(n^2L^2), with c=(1/3)prod(1-2/p^2+1/p^3). Checked G=3c*zeta(2) factor by factor.
- The count swap and the endpoint cost O(n^2/k) are fine.
- Result: n q_k=-U(n/k)+O(L^2/k), uniformly for 1<=k<=n. The constant works out as 1/(2c zeta(2))=C.

A06, small coordinates:
- Checked E(j,k)=(mu*f_k)(j) with f_k(m)=-{m/k}, and M_k=sum_{s in S_k} M(x/s).
- Checked the moment bounds (6), including the p=2 half-moment case.
- Checked the hyperbola identity (8), the principal-character case (V=1), and the local-factor identity (11) by expanding both sides.
- Checked the eta_chi moment K, the partial summation (14) with its lower range, and the decomposition j=su: both the F_s factorization and the fact that v_chi vanishes automatically on non-units.
- Checked |c_{s,chi}|<=2^omega(k), and the two ranges (18)-(19).
- Losses k^5; target O(log^-A) holds for k<=log^B n.
- The Mertens input is used qualitatively only: classical M(x)=O(x exp(-c sqrt(log x))).

A07, decay and integral:
- Checked g=1*eta, eta=(mu/id)*beta, sum beta=zeta(2), and the kernel representation (1), with absolute convergence of the d>t tail.
- V decay via m(Y)/2 + (partial summation times TV of D0 = O(log T)). U decay via the beta split.
- Mellin (3): checked independently. For Re s>1 the transform is 2zeta(s)/(s(s+2)); subtracting the 2y/3 and 1/2 terms continues it to 0<s<1 and gives -2zeta(s)/(s(s+2)).
- D(s)=B(s)/zeta(s+1). The limit s->0 gives I = C zeta(2)/2 - 1 = 1/(4c) - 1.
- [numeric, float] I computed from U directly: 0.7513115, against the predicted 0.7513155. The 4e-6 gap is the tail beyond 1e7.

A08, integration:
- This is where the user's correction applies, so it was checked with extra care.
- The fixed and small coordinates are NOT treated as o(1/n). The retained term is n r_k=(n r_1)/k-n q_k+o(1).
- n r_1 -> rho=(J-I)/zeta(2) follows from A04's exact r_1 formula, n h^Tq -> -I, and n||q||^2 -> J.
- The Riemann sums near x=0 are justified by a monotone integrable envelope exp(-c sqrt(log 1/x))/x. I checked its monotonicity.
- SCALAR gives 0<=J<1. The bounds 1/8<40/(3pi^4)<c<=5/24<1/4 give 0<I<1, so |rho|<1/zeta(2)<1.
- Coverage of all k is a two-range split with no hole:
  * k<K=ceil(log^3 2n): |n r_k|<=|n r_1|/k+O(log^-A)+o(1), using A06 uniformly.
  * K<=k<=n: n r_k=U(n/k)+O(L^{5/2}/K)+O(L^2/k)+o(1)=U(n/k)+o(1), uniformly.
- The intermediate moving coordinates (k->inf, k/n->0) sit in the second range. The bound there is uniform, not a set of pointwise limits.
- limsup <= max(|rho|,sup|U|)=1. The endpoint k=n supplies only the matching liminf.

A09, scalar certificate:
- D0(y)=1/2+B2(th)/y-B3(th)/(3y^2): proved symbolically (substitute m=y-th, compare the cubics). Also 0 mismatches in 2000 exact rational tests.
- |B2|<=1/6, |B3|<=sqrt3/36, so K<183/1000.
- Tail identity (4): partial summation gives the -P/6 coefficient.
- (5) uses |d eta(d)|=mu^2 g<=1. P(u)=sum beta(e)m(u/e), and |m|<=1 has an elementary proof.
- Split (6) at e=u/1000. The arithmetic in (7) gives 202847/300000<0.68 for t>=1e6.
- Finite range: U is convex on each [m,m+1], so the upper bound follows from the endpoints; U(1)=1 exactly, with strict inequality on (1,2).
- The lower bound uses a<=t<=b on half-intervals. The outward rounding direction is correct in every term: floor for lo, ceil for hi, c0 against the positive tnum, c1 against A.
- G-transform identity (1-1/(p(p+1)))/(1-p^-2)=1+1/((p-1)(p+1)^2): verified.
- E local factor, both tail enclosures, exp(s)<=1/(1-s), and the Machin alternating bounds: all verified.

SPECIFIC GAPS / REPAIRS
No gap affecting the conclusion. Minor findings:
- Notation clash: "C" is E^TE in A04 but 3/(2G) elsewhere. The symbol c is consistent between A05 and A08 (c=G/(3zeta(2))).
- Script comment "eta(1000)<=1/50" should read sup_{x>=1000}|m(x)|<=1/50.
- Steps are terse but correct: A04 "rank-one perturbation" (Weyl/Davis-Kahan, not stated) and A05 "endpoint inclusions".
- A07's displayed finite-N Mellin computation was not re-derived line by line. Its result (3) was verified by the independent route above.

SOURCE CHECKS
- Ramaré, Math. Comp. 84 (2015), no. 293, 1359-1387, offprint p.1361, both read in the PDF.
  * Theorem 1.2: (log x)|m(x)|<=1/12 for x>=687.
  * Corollary 1.3: |m(x)|<=1 for x>=1, and also <=1/100 for x>=694.
- 2019 corrigendum (Math. Comp. 88, 2383-2388): its overview changes Theorems 1.5, 1.7, 1.8 and Lemma 3.2 only, not Theorem 1.2 or Corollary 1.3.
- The needed input is only |m|<=1/50 for x>=1000, which is much weaker than the source.
- [numeric, float] max|m(x)| on [1000,1e7] is 0.01166. max |m|log x on [687,1e7] is 0.0817<1/12.
- The Lee-Leong and Ng references were not checked. Only the classical qualitative Mertens bound is needed, which the packet permits me to accept.

COMPUTATIONAL COVERAGE
- My copy of certify_scalar.py has SHA256 08395c08...9d551587, identical to the recorded hash.
- Rerun: ALL_INTEGER_ASSERTIONS_PASSED, with identical C and E enclosures and the same counts (999,999 endpoint and 1,999,998 half-interval checks).
- Run under venv CPython rather than /usr/bin/python3. Standard library only.
- The algorithm was audited as described above.
- [numeric cross-check, not a proof input] Matrix at n=400-3200:
  * n r_1 = -0.342, -0.333, -0.355, -0.340, against the predicted rho=-0.3566. Consistent with slow o(1) convergence.
  * max over all k of |n r_k-(n r_1/k+U(n/k))|: 0.027, 0.020, 0.011, 0.011.
  * The A04 linearization residual halves as n doubles (2.2e-3 down to 3.2e-4).
  * max|n r_k| over 2<=k<=n-1 is 0.998 at n=3200, below 1.

EXPOSURE
- Tools: WebFetch/PDF read of the two Ramaré offprints, and venv Python (numpy, mpmath, fractions).
- No email, contact, publication, or subagents.
- Rules I followed: no numerical value is used as a proof input; float results are marked.

ACTIVE TIME
About 25 minutes, over the 15-minute allocation. I finished the full chain rather than return INCOMPLETE.
