# Arithmetic route after uniform matrix linearization

Status: coordinator derivations, PROOF-UNEXAMINED. The scalar inequality and small-coordinate uniformity are not proved here.

Use c=(1/3)prod_p(1-2/p²+1/p³), S=sum phi(j)², G=3*c*zeta(2), C=3/(2G). Define g(a)=prod_{p|a}p/(p+1), U(t)=t-C sum_{a<=t}g(a)(1-a²/t²). Let q=E^T a/S as in A04.

## Large-coordinate approximation

Elementary divisor expansion gives, uniformly in a,y>=1,

    sum_{j<=y,(j,a)=1}phi(j)
      = y²*g(a)/(2*zeta(2))+O(y*tau(a)*log(2y)).

To see this, substitute phi(j)=j sum_{d|j}mu(d)/d and use
sum_{m<=z,(m,a)=1}m=(phi(a)/a)z²/2+O(z*tau(a)). The main Euler product is (phi(a)/a)*prod_{p not dividing a}(1-p^-2)=g(a)/zeta(2). Its truncated tail contributes O(y).

Also S=c*n³+O(n²*log²(2n)): write phi(j)²=j² sum_{d|j}f(d), where f is squarefree-supported and f(p)=-2/p+1/p²; use |f(d)|<=2^omega(d)/d and elementary divisor summation.

Swap the count index in B_k=sum_{j<=n}phi(j)R(j,k):

    B_k=sum_{a<=n/k} sum_{ka<=j<=n,(a,j)=1}phi(j).

Endpoint inclusions cost O(n²/k). The preceding estimates and sum_{a<=t}tau(a)=O(t log(2t)) yield

    n*q_k = -U(n/k)+O(log²(2n)/k),  1<=k<=n.       (A)

The error is useful for k>=log³ n. Combined with A04, whose n*r_1=O(log^(5/2)n), it gives n*r_k=U(n/k)+o(1) uniformly in this range.

## Small-coordinate obligation

It suffices to prove, for every fixed A,B>0,

    max_{1<=k<=log^B n} |b_k(n)|/n² = O(log^(-A)n).  (B)

This is stronger than A02's fixed-k target and remains OPEN HERE. Ordinary effective Mobius cancellation and a periodic/character convolution may suffice; do not assume Siegel-Walfisz without checking the exact arithmetic weights. For the eventual integration, B=3 and A>2 suffice. Such a bound makes the harmonic-weighted sum over this small range negligible.

## Candidate decay and integral calculation for U

Extend U(t)=t for 0<t<1. Let eta(d)=mu(d)/prod_{p|d}(p+1) and D0(y)=2y/3-sum_{m<=y}(1-m²/y²). Then

    U(t)=C sum_{d>=1}eta(d)D0(t/d).

The coefficient convolution eta=(mu/id)*beta has nonnegative beta(p^r)=1/[p^r(p+1)] for r>=1. Its sum is zeta(2), and sum beta(d)*d^delta is finite for 0<delta<1.

D0(y)=1/2+O(1/y) for y>=1; D0(y)=2y/3 for y<1; D0 is continuous and integral_0^T |D0'(y)|dy=O(log(2T)). The usual effective PNT estimate m(x)=sum_{d<=x}mu(d)/d=O(exp(-c0 sqrt(log x))) implies the same shape of bound for V(x)=sum mu(d)/d*D0(x/d): split d at x/T, approximate D0 by 1/2 on the first part, and partially sum the tail against m. The resulting bound is O(1/T)+O(exp(-c0 sqrt(log(x/T)))*log(2T)); choose T=exp(c1 sqrt(log x)). Convolving with beta and splitting beta at sqrt(x) gives

    U(t)=O(exp(-c2 sqrt(log t))) as t->infinity.       (C)

This argument needs a written audit, including a precise source for the standard effective PNT input. It uses an existing theorem, not a new prime-number-theorem proof.

For 0<s<1, the proposed Mellin identity is

    integral_0^infinity U(t)t^(-s-1)dt
       = -2*C*zeta(s)*D(s)/(s*(s+2)),
    D(s)=sum eta(d)d^(-s)=B(s)/zeta(s+1),
    B(0)=sum beta(d)=zeta(2).

The kernel Mellin identity is integral D0(y)y^(-s-1)dy=-2*zeta(s)/(s*(s+2)); it can be justified by Euler summation. Absolute coefficient interchange is valid for s>0. Using (C) to let s decrease to zero gives

    I := integral_1^infinity U(t)/t dt = 1/(4c)-1.    (D)

## Conditional completion

If (A)--(D), A04, and the Claude scalar target |U(t)|<=1 are proved, Riemann-sum limits give

    n*h^Tq -> -I,
    n*||q||² -> J := integral_1^infinity U(t)²/t² dt,
    n*r_1 -> rho=(J-I)/zeta(2).

For the first limit use (B) on k<=log³ n, (A) on the complement, and (C) for the integrable tail. The summed error in (A) against 1/k is O(1/log n). Analogous estimates give the squared-norm limit. Riemann sums require explicit uniform tail control; do not replace this step by pointwise convergence alone.

The scalar target implies 0<=J<=1. Moreover 1/8<c<1/4: the upper bound follows already from the p=2 Euler factor; the lower bound follows from c>(10/9)/(3*zeta(2)²)=40/(3*pi^4)>1/8. Hence 0<I<1, and |rho|<1.

For k<=log³ n, (B) and A04 give n*r_k=rho/k+o(1). For larger k, (A) and A04 give n*r_k=U(n/k)+o(1). The scalar bound then gives limsup n||r||infinity<=1; A04 gives the reverse liminf.

This is a conditional proof architecture, not an established resolution. Its load-bearing missing items are (B), the scalar inequality, and review of the decay/Mellin/Riemann-sum steps.
