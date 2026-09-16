# Scalar profile: decay and an exact integral

Status: complete coordinator argument, INTERNAL-NONINDEPENDENT review only. No external proof audit yet. This does not establish |U|<=1.

Let g(a)=prod_{p|a}p/(p+1), G=prod_p(1-1/[p(p+1)]), C=3/(2G), and

    U(t)=t-C sum_{a<=t}g(a)(1-a²/t²), t>0.

Thus U(t)=t on (0,1). We prove U(t)=O(exp(-c sqrt(log t))) for large t, and

    integral_1^infinity U(t)/t dt = C*zeta(2)/2-1.

The positive constants implicit in the decay need not be explicit. This is insufficient for a certified finite-to-infinite supremum check.

## Existing analytic input

Use the standard unconditional estimate M(x)=sum_{d<=x}mu(d)=O(x exp(-c0 sqrt(log x))). A stronger bound is stated in Nathan Ng's UBC/PIMS lecture *The sum of the Möbius function*, 27 February 2023, PDF page10, https://personal.math.ubc.ca/~gerg/teaching/613-Winter2023/Feb27.pdf#page=10 ; its locator for the original textbook treatment is Ivić, Theorem12.7, pp.309–315. The source statement, not Ivić's proof, was checked.

Partial summation gives convergence of sum mu(d)/d. Its sum is zero, by Abel's theorem and sum mu(d)/d^(1+s)=1/zeta(1+s)->0 as s decreases to zero. Consequently

    m(x)=sum_{d<=x}mu(d)/d
        =M(x)/x-integral_x^infinity M(y)/y² dy
        =O(exp(-c1 sqrt(log x))).

In the last estimate the integral costs only a factor O(1+sqrt(log x)), absorbed by decreasing c1.

## Kernel and coefficient identities

Define

    D0(y)=2y/3-sum_{m<=y}(1-m²/y²),
    eta(d)=mu(d)/prod_{p|d}(p+1).

Then g=1*eta and sum eta(d)/d=G, the latter absolutely. Hence

    U(t)=C sum_{d>=1}eta(d)D0(t/d).                    (1)

The tail d>t is absolutely convergent because D0(t/d)=2t/(3d).

Define the nonnegative multiplicative beta by beta(p^r)=1/[p^r(p+1)] for r>=1. Its local generating function multiplied by 1-X/p is 1-X/(p+1); therefore eta=(mu/id)*beta. Also

    sum beta(e)=prod_p(1+1/(p²-1))=zeta(2),
    sum beta(e)e^delta<infinity for every 0<delta<1.

The second assertion follows from the local tail 1/[(p+1)(p^(1-delta)-1)]=O(p^(-2+delta)).

Writing m=floor(y), exact sum-of-squares algebra shows

    D0(y)=1/2+O(1/y) for y>=1,
    D0(y)=2y/3 for y<1.

D0 is continuous at the integers, since the new summand is zero there. Away from integers, D0'(y)=2/3-2(sum_{a<=y}a²)/y³=O(1/y) for y>=1, and D0'=2/3 for y<1. Thus its total variation on (0,T) is O(log(2T)); D0 is bounded on (0,infinity).

## Decay

Put V(x)=sum_{d>=1}mu(d)/d*D0(x/d). For 1<T<x let Y=x/T. For d<=Y, the kernel expansion gives

    sum_{d<=Y}mu(d)/d*D0(x/d)=m(Y)/2+O(1/T).

For d>Y, partial summation against m and the kernel variation bound give absolute value

    O(sup_{y>=Y}|m(y)| * log(2T)).

Indeed the boundary at infinity vanishes, and under z=x/y the derivative's absolute integral becomes the variation of D0 on (0,T). Choose T=exp(c2 sqrt(log x)) for any fixed c2>0. Then log(x/T) is comparable to log x, and both terms are O(exp(-c3 sqrt(log x))) after adjusting positive constants.

For 0<x<1, V(x)=2x/(3*zeta(2)); on every bounded interval V is bounded by its defining series. Thus V is bounded globally. From eta=(mu/id)*beta, absolute convergence of the relevant tails permits

    U(t)=C sum_{e>=1}beta(e)V(t/e).

Split e at sqrt(t). The first part inherits the exponential-in-sqrt-log bound; the second is O(t^(-delta/2)) by the beta moment and global boundedness of V. Therefore

    U(t)=O(exp(-c4 sqrt(log t))).                     (2)

## Mellin evaluation

For real 0<s<1 the kernel Mellin integral converges absolutely, and

    integral_0^infinity D0(y)y^(-s-1)dy
        =-2*zeta(s)/(s*(s+2)).                       (3)

For a direct check, integrate the finite sum to an integer N. The result is

    2N^(1-s)/[3(1-s)]
    -2/[s(s+2)] sum_{a<=N}a^(-s)
    +N^(1-s)/s
    -N^(-s-2)/[s+2] sum_{a<=N}a².

Substitute sum a²=N³/3+N²/2+N/6 and the elementary Euler-summation formula
sum_{a<=N}a^(-s)=N^(1-s)/(1-s)+zeta(s)+O_s(N^(-s)). All coefficients of N^(1-s) cancel; remaining powers vanish. This proves (3).

Since sum |eta(d)|/d^s<infinity for s>0, absolute interchange in (1) is valid. Set B(s)=sum beta(e)e^(-s), which is analytic near s=0 and B(0)=zeta(2). The coefficient identity gives D(s):=sum eta(d)d^(-s)=B(s)/zeta(s+1), for s>0. Hence

    integral_0^infinity U(t)t^(-s-1)dt
       =-2C*zeta(s)*B(s)/[s*(s+2)*zeta(s+1)].        (4)

By (2), dominated convergence applies as s decreases to zero; near t=0 use U(t)=t. Since zeta(0)=-1/2 and s*zeta(1+s)->1, (4) tends to C*zeta(2)/2. Subtract integral_0^1 U(t)/t dt=1. This proves the asserted exact integral.

## Audit boundary

Coefficient identities, kernel continuity, tail convergence, integral interchange, and the s->0 passage are written explicitly above. The only substantive external analytic input is the known effective Mertens estimate. This note has not received the campaign's separate cold-examiner process and must not be represented as independently verified.
