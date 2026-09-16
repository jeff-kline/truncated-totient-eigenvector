# Proposed equivalence with a scalar inequality

Status: integrated proof draft. The matrix component A04 has passed the separate proof audit R02. The arithmetic components A05–A07 and their integration here have only coordinator review; this is not a fully examined theorem or a resolution of the conjecture.

## Statement

With the original matrix definitions in CHARTER.md, define

    g(a)=prod_{p|a}p/(p+1),
    G=prod_p(1-1/[p(p+1)]), C=3/(2G),
    U(t)=t-C sum_{a<=t}g(a)(1-a²/t²), t>=1.

The proposed reduction says the 2020 conjecture is equivalent to

    |U(t)|<=1 for every real t>=1.                    (SCALAR)

No proof of SCALAR is supplied. Numerical evidence is not used in the argument.

## Proof of necessity

Let S=sum phi(j)², q=(R-a h^T)^T a/S, and r=h-(h^Tv)v. From A04,

    n*r_k=(n*r_1)/k-n*q_k+o(1), uniformly in k,
    n*r_1=O(log^(5/2)(2n)).                           (1)

The elementary count calculation in A05 gives

    n*q_k=-U(n/k)+O(log²(2n)/k).                     (2)

Fix t>=1 and choose k_n with k_n/n->1/t. Then (1)--(2) imply n*r_{k_n}->U(t). U is continuous because every summand enters at zero at an integer. Thus the original conjectured limit forces |U(t)|<=1.

## Scalar normalization

A07 establishes, in its internally reviewed draft,

    U(t)=O(exp(-c0 sqrt(log t))),
    I:=integral_1^infinity U(t)/t dt=1/(4c)-1,
    c=G/[3*zeta(2)].                                (3)

In particular U is bounded even without SCALAR. A06 gives, for any fixed A,B>0,

    max_{k<=log^B n}|n*q_k|=O_{A,B}(log^-A n).        (4)

This follows from A06's b bound and S asymptotic to c*n³.

Let K=ceil(log³(2n)). From (4) with A>2, sum_{k<K}(n*q_k)/k=o(1). On k>=K, the error in (2) summed against 1/k is O(log²n/K)=o(1). Therefore

    n*h^Tq = -sum_{k>=K}U(n/k)/k+o(1) -> -I.         (5)

Here is the needed justification for this improper Riemann sum. The integrand f(x)=U(1/x)/x is continuous on (0,1]. Near zero, its absolute value is bounded by a constant times exp(-c0 sqrt(log(1/x)))/x. This envelope is integrable; for sufficiently small x it is decreasing as x increases. Its right-endpoint Riemann sum over k/n<=epsilon is bounded by its integral over (0,epsilon). This uniformly controls the omitted endpoint and permits ordinary Riemann convergence on every [epsilon,1]. The resulting integral is I by t=1/x.

Similarly,

    n*||q||² -> J:=integral_1^infinity U(t)²/t² dt.  (6)

For detail, on k<K equation (4) makes (1/n)sum(n*q_k)² tend to zero. On k>=K, the error in (2) is uniformly O(1/log n), while U is bounded, so its effect on the averaged squares is o(1). The function U(1/x)² extends continuously to zero with value zero by (3); ordinary Riemann sums apply.

The audited scalar projection formula A04 now yields

    n*r_1 -> rho=(J-I)/zeta(2).                     (7)

## Proof of sufficiency

Assume SCALAR. Then 0<=J<=1. We also have 1/8<c<1/4. For the upper bound on c, the p=2 factor already gives c<=5/24. For the lower bound, every factor 1-2/p²+1/p³ is greater than (1-1/p²)², and the ratio at p=2 is 10/9. Consequently

    c > 10/[27*zeta(2)²] = 40/(3*pi^4) > 1/8.

Thus 0<I<1. Equations (6)--(7) imply |rho|<1, since |J-I|<1 and zeta(2)>1.

For k<K, (1), (4), and (7) give n*r_k=rho/k+o(1), uniformly. For k>=K, equations (1)--(2) and n*r_1=O(log^(5/2)n) give n*r_k=U(n/k)+o(1), uniformly. Therefore SCALAR gives limsup n||r||infinity<=1. The audited endpoint result in A04 gives the opposite liminf, proving the desired limit.

## Exact remaining work

1. Prove or refute SCALAR on the entire unbounded real interval. A finite prime product without a rigorous tail enclosure is insufficient.
2. Examine the arithmetic estimates A05–A07 and this integration independently. A04 alone is the scope of the completed R02 verification.
3. Only after both are done, adjudicate the original conjecture and perform novelty/source comparison. No publication is authorized.
