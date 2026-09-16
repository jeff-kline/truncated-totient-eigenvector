# A02: fixed-coordinate residual reduction

Scope: fixed k only. No other workers' notes consulted; no agents or numerical experiments. This is a proved reduction with a remaining arithmetic gap, not a proof of the conjecture.

Write h=(1/k), H²=||h||², a_j=phi(j) (phi(1)=1), A=||a||², E=R-ah^T, b=E^Ta, C=E^TE. Then

    Q=A hh^T+h b^T+b h^T+C.

All estimates below are as n tends to infinity, with fixed k. Constants can depend on k.

## Proved fixed-coordinate lemma

Let t=h^Tv and r=h-tv. Then

    r_k = r_1/k - b_k/A + o(1/n).                         (1)

In particular b_1=0 and b_2=0 for n>=2, so

    r_2=r_1/2+o(1/n).

Thus even proving b_k=o(n²) for every fixed k does NOT show that the fixed-coordinate residual is o(1/n): the scalar r_1 must also be determined.

### Proof and quantitative estimates

Mobius inversion gives, exactly,

    E(j,k)=-sum_{d|j} mu(d) {j/(kd)}.

Consequently |E(j,k)|<=tau(j). Also R(j,k)<=j/k and phi(j)/k<=j/k, so |E(j,k)|<=j/k (both terms are nonnegative). Splitting the k sum at j/tau(j) gives

    sum_k |E(j,k)|² <= O(j tau(j)),
    ||E||_F=O(n sqrt(log(2n))).

The elementary divisor estimates used here are sum_{j<=n}tau(j)=O(n log(2n)) and sum tau(j)²=O(n log(2n)^3); the latter follows from tau(j)²<=d_4(j). For each fixed column,

    ||E(:,k)||_2=O(sqrt(n) log(2n)^(3/2)).

Also A is bounded above and below by positive constants times n³: the upper bound follows from phi(j)<=j; the lower bound follows by Cauchy--Schwarz from sum_{j<=n}phi(j) asymptotic to n²/(2 zeta(2)). The latter follows from phi(j)=sum_{d|j}mu(d)j/d by summing, with error O(n log(2n)). Therefore

    ||Q-Ahh^T||=O(n^(5/2) sqrt(log(2n))),
    lambda=A H²(1+O(sqrt(log(2n)/n))),
    v=h/H+O_2(sqrt(log(2n)/n)),
    t=H+O(sqrt(log(2n)/n)).

These follow directly from the rank-one spectral gap, choosing the positive sign. Positivity/uniqueness need no extra hypothesis: the j=n row of R has all entries at least one, hence every entry of Q is strictly positive, and Perron--Frobenius applies.

Column 1 of E vanishes exactly. Subtracting 1/k times the first eigenvector equation from the kth gives

    lambda(v_k-v_1/k)=t b_k+(Cv)_k.

Now |(Cv)_k|<=||E(:,k)||_2 ||E||=O(n^(3/2) log(2n)^2), whereas |b_k|<=sqrt(A)||E(:,k)||=O(n² log(2n)^(3/2)). Hence

    r_k=r_1/k-(t²/lambda)b_k+O(n^(-3/2)log(2n)^2).

The preceding spectral estimates imply t²/lambda=A^(-1)(1+O(sqrt(log(2n)/n))). Substitution proves (1), with error O(n^(-3/2)log(2n)^2).

For column 2, pairing reduced residues a and j-a shows R(j,2)=phi(j)/2 for j>=3; E(2,2)=1/2 and E(1,2)=-1/2. Their phi weights cancel, so b_2=0 for n>=2. Column 2 of E itself is supported at j=1,2.

## Exact remaining arithmetic problem

For a fixed integer k, set f_k(m)=-{m/k}. Then

    b_k(n)=sum_{dm<=n} mu(d) phi(dm) f_k(m).             (2)

Establishing b_k=o(n²) is a sufficient arithmetic input to obtain r_k=r_1/k+o(1/n). A nonzero limit b_k/n² instead contributes a distinct fixed-coordinate term in (1). Formula (2), including the factor phi(dm), is important: cancellation of mu(d) without this weight is insufficient.

A possible route is to split m into residue/gcd classes modulo k and use Dirichlet characters. On integers coprime to k, character components of the convolution have form

    g_chi(j)=phi(j) chi(j) product_{p|j}(1-conj(chi(p))).

For p not dividing k, the local Dirichlet series for g_chi(j)/j is

    (1-[1-1/p+chi(p)/p]p^(-s))/(1-chi(p)p^(-s)).

It factors as the local factor of L(s,chi)/zeta(s) times a factor whose prime correction is O(p^(-1-Re(s))). This suggests a cancellation proof for nonprincipal characters; the prime powers dividing k and the required summatory bounds must still be supplied. No such bound is claimed proved here.

## Normalization term that must be retained

There is an exact scalar identity useful to the coordinator. Put w=v/v_1=h+z, so z_1=0. Then

    r_1=(h^T z+||z||²)/(H²+2h^Tz+||z||²).               (3)

Thus the quadratic direction correction can contribute at order 1/n when growing coordinates carry squared mass of that order. Dropping it on the grounds that the eigenvector perturbation is small is not justified. Together (1)--(3) isolate the fixed-column arithmetic from the common projection normalization.

If A/n³ tends to alpha, n r_1 tends to rho, and b_k/n² tends to beta_k, (1) gives n r_k tending to rho/k-beta_k/alpha. This is a conditional limit statement, not an assertion that those limits have been established.

Final status: (1) and (3) are proved. The precise outstanding fixed-coordinate gap is a weighted arithmetic cancellation estimate b_k(n)=o(n²) for fixed k>=3 (or computation of a different n² coefficient). No conclusion about the moving-coordinate maximum is asserted.
