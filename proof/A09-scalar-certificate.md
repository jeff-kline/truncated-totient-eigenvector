# Scalar inequality: repaired proof and exact finite certificate

Status: complete proof candidate, coordinator-checked, awaiting separate proof audit. Attribution: the summatory-coefficient tail identity and positive convolution below came from the owner-mediated Claude Opus response preserved in review/CLAUDE-01-received.txt. The coordinator verified the source, simplified the tail, and independently implemented the integer certificate. This replaces, rather than validates, Claude's unavailable floating-point scan.

## Claim

Let g(a)=prod_{p|a}p/(p+1), G=prod_p(1-1/[p(p+1)]), C=3/(2G), and

    U(t)=t-C sum_{a<=t}g(a)(1-a²/t²), t>=1.

Then |U(t)|<=1, with equality only at t=1.

## Existing source input

Ramaré, *Explicit estimates on several summatory functions involving the Moebius function*, Mathematics of Computation84 (2015),1359–1387, Theorem1.2, printed p.1361, states

    |m(x)| log x <=1/12 for x>=687,
    m(x)=sum_{d<=x}mu(d)/d.

Author-hosted published offprint: https://ramare-olivier.github.io/Maths/mcom2914.pdf#page=3 . The same page's Corollary1.3 includes |m(x)|<=1 for x>=1. The 2019 corrigendum, https://ramare-olivier.github.io/Maths/mcom3449-corrigendum.pdf , changes later logarithmically weighted results and does not change Theorem1.2. Both source texts were inspected. We do not rely on the recalled 2013 citation in Claude's return.

Since log1000>6, this source implies the deliberately weaker bound

    sup_{x>=1000}|m(x)|<=1/50.                       (1)

For completeness the global |m(x)|<=1 also follows without that corollary: sum_{d<=x}mu(d)floor(x/d)=1, hence x*m(x)=1+sum_{d<=x}mu(d){x/d}. If N=floor(x), the absolute value is at most 1+{x}+sum_{d=2}^N |mu(d)|{x/d}<=1+{x}+N-1=x.

## Tail identity and bounds

Set eta(d)=mu(d)/prod_{p|d}(p+1), P(u)=sum_{d<=u}eta(d), and

    D0(y)=2y/3-sum_{a<=y}(1-a²/y²).

The elementary convolution g=1*eta and sum eta(d)/d=G give

    U(t)=C sum_{d>=1}eta(d)D0(t/d).                  (2)

For theta={y}, exact sum-of-squares algebra yields

    D0(y)=1/2+B2(theta)/y-B3(theta)/(3y²).

For y>=1 write F(y)=B2(theta)-B3(theta)/(3y). The standard explicit polynomials B2(z)=z²-z+1/6 and B3(z)=z³-3z²/2+z/2 satisfy |B2|<=1/6 and |B3|<=sqrt(3)/36 on [0,1]. Therefore

    |F(y)|<=K:=1/6+sqrt(3)/108 <183/1000.            (3)

For d>t the kernel in (2) equals 2t/(3d). Splitting there and partially summing the tail gives

    U(t)/C = -P(t)/6+(2t/3)integral_t^infinity P(u)/u² du
             +(1/t)sum_{d<=t}d*eta(d)*F(t/d).        (4)

The boundary at infinity vanishes: P is bounded by the positive convolution below, so P(u)/u->0. Since |d*eta(d)|=mu(d)²*g(d)<=1, equations (3)--(4) imply

    |U(t)|<=C[(5/6)epsilon(t)+K],
    epsilon(t)=sup_{u>=t}|P(u)|.                     (5)

No estimate for the mean of mu²*g is needed.

As in A07, eta=(mu/id)*beta, where beta is nonnegative multiplicative with beta(p^r)=1/[p^r(p+1)] for r>=1. Thus

    P(u)=sum_{e<=u}beta(e)m(u/e),
    sum beta(e)=zeta(2),
    E:=sum beta(e)*sqrt(e)
       =prod_p(1+1/[(p+1)(sqrt(p)-1)]).

Split at e=u/1000. Using (1) and |m|<=1 gives, for t>=1000,

    epsilon(t)<=zeta(2)/50+sqrt(1000/t)*E.           (6)

The integer certificate below establishes C<213/100 and E<4; also zeta(2)<5/3. For t>=10^6, sqrt(1000/t)<4/125. Substituting these deliberately rounded rational constants in (5)--(6) proves

    |U(t)| < (213/100)[(5/6)((1/50)(5/3)+(4/125)4)+183/1000]
           =202847/300000 <68/100.                   (7)

This is an unconditional tail bound using the checked published estimate, not an extrapolation of finite data.

## Finite certificate, 1<=t<=10^6

The standalone script code/certify_scalar.py uses Python arbitrary-precision integers and fractions; no floating-point operation enters an assertion. Its output is results/scalar-certificate.json. Scale Q=10^30 represents intervals [L/Q,H/Q]. Every multiplication/division rounds outward using integer floor and ceiling.

The sieve computes the smallest prime factor p of every a<=10^6. If p² divides a, g(a)=g(a/p); otherwise g(a)=g(a/p)*p/(p+1). This supplies outward intervals for all g(a). A separate trial-division Fraction implementation checks these enclosures for a<=300.

The constant C is enclosed using

    G=zeta(2)^(-1)*prod_p(1+1/[(p-1)(p+1)²]).

The pi enclosure comes from Machin's identity pi=16 arctan(1/5)-4 arctan(1/239), with rational alternating-series remainder bounds (32 and10 terms). Both truncated products use all primes<=P=10^6. For G's transformed product the sum of omitted local excesses is at most 1/[2(P-1)²], by comparison with all integers and the integral of x^(-3). For E, integer square roots enclose each local factor, and the omitted excesses sum to at most 4/sqrt(P)=1/250. In both cases prod(1+x_j)<=exp(sum x_j)<=1/(1-sum x_j). The certified intervals imply

    2.129344320757238687316827406299 <= C
       <= 2.129344320758303361606554217009,
    E <=3.588756760325859013900248680340 <4.

These decimals are exact rational endpoints with denominator10^30.

Let A_m=sum_{a<=m}g(a), B_m=sum_{a<=m}a²g(a). On [m,m+1],

    U(t)=t-C*A_m+C*B_m/t²,
    U''(t)=6*C*B_m/t^4>0.

The script verifies U(m)<3/4 for every integer 2<=m<=10^6, by enclosing A_m-B_m/m² from below and C from below. It treats U(1)=1 exactly. Convexity then bounds every interval from above, with strict inequality below1 except at t=1.

For a lower bound split every [m,m+1], 1<=m<10^6, into two halves [a,b]. For t in that half,

    U(t)>=a-C*A_m+C*B_m/b².

An outward enclosure uses C_upper*A_upper in the negative term and C_lower*B_lower in the positive term. Multiplying positive denominators converts its comparison with -3/4 into an integer assertion. All 1,999,998 half-interval assertions are strictly positive. Thus U(t)>-3/4 throughout the finite range. This avoids approximate cubic roots or sampled interior minima entirely.

The run completed all 999,999 endpoint checks and 1,999,998 half-interval checks in 5.216 process CPU seconds. It also checks a deliberately false endpoint assertion would fail (U(2)>0). The tested script's SHA256 is recorded inside the output. Finite coverage and (7) together prove the claimed scalar inequality, subject to review of this argument and implementation.

## Review boundary

The pasted Claude response has truncations, and its claimed uscan.py was not supplied. Its numerical constants and roundoff accounting are not accepted as certificates. Equations (2), (4), and the positive convolution credit its useful mechanism. This note supplies the missing source check and a replacement computation. A separate examiner still needs to audit this artifact and the parent reduction; the current coordinator has seen and helped develop the proof, so its checking is INTERNAL-NONINDEPENDENT.
