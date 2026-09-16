# Claude Opus: full proof and certificate audit packet

Use this only AFTER the initial statement-only report is saved. This is a proof-aware second stage, not a second isolated attack. No email, contact, publication, or nested agents. Opus-tier ownership is required for proof judgment; cheaper execution may only reproduce the fixed integer certificate.

The task is to audit the exact original 2020 limit and the scalar inequality defined in the initial packet. Allocate up to 15 active minutes for a first substantive pass. If coverage cannot fit, return INCOMPLETE with a precise list of unchecked obligations. Do not turn absence of findings into VERIFIED. Read the full proof chain, including the arithmetic uniformity, normalization, and every integer-certificate inequality. Existing published theorems may be accepted after source/hypothesis checks; do not reprove classical PNT. The matrix lemma alone has received a separate same-provider proof audit; no existing verdict is a substitute for your own assigned checks.

Return a concise report with STAGE PROOF-AUDIT; VERDICT VERIFIED, GAP, REFUTED, or INCOMPLETE; exact claim and scope; line of reasoning checked; specific gaps or repairs; source checks; computational coverage; exposure; and active time. Distinguish a repaired proof from validation of an old one. The owner will return your report to the coordinator. Only a complete checked chain earns VERIFIED for the original conjecture.

Everything needed is included below. Local paths name provenance only; you need no checkout. The script uses only standard Python and can be copied to a local code/ directory with a sibling results/ directory. It writes a JSON result there. Its observed output is included, but you must audit the actual algorithm and mathematical coverage; blind rerunning is insufficient. No numerical approximation is a proof input. Time measurements in the JSON are descriptive.

The proposed logical order is: uniform matrix linearization; elementary large-coordinate averaging; uniform small-coordinate cancellation; profile decay and normalization integral; scalar certificate; integration into the original limit. Notation is local to each note: the scalar summatory eta is not the matrix vector q. Reconcile every use.


## Elementary large-coordinate averaging (extracted A05)

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



---

## notes/A04-uniform-linearization.md

SHA256: 2086e36776254025e59e97433fd7c4ca3f7ea3fc85a04b97df25cd05ee8776ca

# Uniform eigenvector linearization — coordinator candidate

Status: PROOF-UNEXAMINED. This strengthens A02 but does not settle the arithmetic supremum. Not a proof of the original conjecture.

Let a_j=phi(j), S=||a||², h_k=1/k, H²=||h||², E=R-ah^T, b=E^T a, C=E^TE. Let v be the positive unit Perron vector, t=h^Tv, and r=h-tv. Put L=log(2n).

The divisor bounds |E(j,k)|<=tau(j) and |E(j,k)|<=j/k imply

    ||E|| <= ||E||F = O(n L^(1/2)),
    max_k ||E(:,k)||2 = O(n^(1/2)L^(3/2)),
    ||Eh||2 = O(n^(1/2)L^(5/2)).

For the third estimate, bound |(Eh)_j| by tau(j) sum_{k<=n}1/k, then use sum tau(j)^2=O(n L^3). Also S=Theta(n³), ||b||2=O(n^(5/2)L^(1/2)), max|b_k|=O(n² L^(3/2)).

Rank-one perturbation gives v=h/H+O_2(n^(-1/2)L^(1/2)), lambda=SH²(1+O(n^(-1/2)L^(1/2))), and t,v_1 bounded away from zero. Consequently

    ||Ev||2 <= ||Eh||2/H+||E|| ||v-h/H||2
             = O(n^(1/2)L^(5/2)),
    |b^Tv| <= ||a||2 ||Ev||2 = O(n² L^(5/2)).

Column 1 of E is zero. The first coordinate eigen-equation is exactly lambda*v_1=S*t+b^Tv. Therefore

    t/(lambda*v_1) = S^(-1)(1+O(L^(5/2)/n)).

Subtracting h_k times the first coordinate equation from coordinate k gives

    lambda*(v_k-v_1*h_k)=t*b_k+(Cv)_k.

It follows, uniformly as a vector, that

    v/v_1 = h + q + d,     q=b/S,
    ||d||2 = O(n^(-3/2)L^3).

Indeed the coefficient error times ||b||2/S has this order; and ||Cv||2 <= ||E|| ||Ev||2 = O(n^(3/2)L^3), divided by lambda*v_1=Theta(n³).

Since q_1=d_1=0, writing z=q+d yields the exact projection identity

    r_1 = (h^Tz+||z||²)/(H²+2h^Tz+||z||²).

Here |h^Tq|=|a^TEh|/S=O(L^(5/2)/n), ||q||²=O(L/n), so r_1=O(L^(5/2)/n). Expanding the denominator and using the bound on d gives

    r_1 = [h^Tq+||q||²]/H² + o(1/n),
    r   = r_1*h - q + e,   ||e||2=O(n^(-3/2)L^3).

In particular the latter error is o(1/n) in every coordinate simultaneously. Thus the unresolved part is arithmetic, not an uncontrolled matrix perturbation:

    n*r_k = (n*r_1)/k - n*b_k/S + o(1), uniformly in k.

At k=n, R(:,n)=e_n and so q_n=phi(n)/S-1/n. Since n*r_1/n=r_1=o(1) and n*phi(n)/S=O(1/n), this proves (subject to review)

    n*r_n -> 1, hence liminf n||r||infinity >=1.

To obtain the matching upper bound, one must control q over all k, including the transition k->infinity with k/n->0, and control n*r_1. Pointwise fixed-k and fixed-k/n limits alone do not suffice.


---

## notes/A06-uniform-small-coordinates.md

SHA256: c3b96f19c20b2b5d359eedd2b48148776100fb2d98dbd41e88af4547dada0ffd

# A06: uniform cancellation for logarithmically growing coordinates

**Proved.** There are effective absolute constants C,c>0 such that

\[
 \frac{|b_k(N)|}{N^2}\le C k^5
 \exp\{-c\sqrt{\log(2N)}\}.                         \tag{U}
\]

Here N,k are positive integers, and b_k uses its arithmetic counting definition (which agrees with the matrix definition when k<=N). Consequently, for every fixed A,B>0,

\[
 \max_{1\le k\le(\log N)^B}\frac{|b_k(N)|}{N^2}
 =O_{A,B}((\log N)^{-A})\qquad(N\longrightarrow\infty).
 \tag{Target}
\]

This note quantitatively extends A03 without changing that file. All constants below are independent of k, characters, and summation arguments, unless indicated. No numerical computation is used.

## 1. Effective input and conventions

Write L(x)=log(2x) and D_a(x)=exp(-a sqrt(L(x))) for x>=1. The only analytic input is the ordinary effective Mertens estimate: for effective absolute C_0,c_0>0,

\[
 |M(x)|:=\left|\sum_{n\le x}\mu(n)\right|
 \le C_0 x D_{c_0}(x)\qquad(x\ge1).                 \tag{1}
\]

A primary source is Ethan Simpson Lee and Nicol Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, [arXiv:2208.06141v5](https://arxiv.org/abs/2208.06141v5), Theorem 1.1, equation (9), PDF page 2. That result supplies an unconditional explicit estimate of the form x(log x)exp(-eta sqrt(log x)) above an explicit threshold. Absorbing log x into a smaller positive exponential constant, replacing log x by log(2x), and using |M(x)|<=x below the threshold gives (1) with effective constants. The source locator was checked; no unresolved citation remains.

We repeatedly use the following elementary inequalities, valid for x>=1:

\[
 y\ge\sqrt{x}\ \Longrightarrow\ L(y)\ge L(x)/2,
 \tag{2}
\]

\[
 x^{-\theta}\ll_{a,\theta}D_a(x)\quad(a,\theta>0),
 \qquad L(x)D_a(x)\ll_a D_{a/2}(x).                 \tag{3}
\]

Both constants in (3) are effective: the ratios are exponentials of a quadratic-dominant expression in sqrt(L(x)). Thus all bounded arguments, including x=1, are covered. All sums over real cutoffs mean sums over integers below those cutoffs; summatory functions are zero below 1.

For clarity we keep the exponential constants

\[
 c_1=c_0/\sqrt2,\quad c_2=c_0/4,\quad
 c_3=c_0/(4\sqrt2),\quad c_4=c_0/8,\quad
 c_5=c_0/(8\sqrt2).                                \tag{4}
\]

## 2. Uniform estimate for the restricted Möbius sum

For k>=2 let S_k be the integers supported on primes dividing k, including 1. Put mu_k(n)=mu(n)1_{(n,k)=1}. The exact convolution mu_k=mu*1_{S_k} gives

\[
 M_k(x)=\sum_{s\in S_k,\ s\le x}M(x/s).
 \tag{5}
\]

The elementary moments needed here are

\[
 \sum_{s\in S_k}s^{-1}
 =\prod_{p\mid k}(1-p^{-1})^{-1}\le k,
 \qquad
 \sum_{s\in S_k}s^{-1/2}
 =\prod_{p\mid k}(1-p^{-1/2})^{-1}\le k^2.          \tag{6}
\]

For the first inequality each local factor is <=p. For the second each is <=p^2: for p>=2, p^{-1/2}<=1/sqrt(2)<3/4<=1-p^{-2}. Multiplication gives at most rad(k) and rad(k)^2, respectively.

Split (5) at s=sqrt(x). By (1)--(2), the first part is at most C_0 k x D_{c_1}(x). Using |M(y)|<=y in the second part gives

\[
 \sum_{\substack{s\in S_k\\s>\sqrt{x}}}\frac{x}{s}
 \le x^{3/4}\sum_{s\in S_k}s^{-1/2}
 \le k^2x^{3/4}.
\]

Absorbing x^{-1/4} by (3), we obtain uniformly for x>=1

\[
 |M_k(x)|\ll k^2xD_{c_1}(x).                       \tag{7}
\]

We also retain the trivial |M_k(x)|<=x.

## 3. Uniform character convolution estimate

For a character chi modulo k, extended by zero on non-units, set

\[
 v_\chi=\mu_k*\chi,\quad
 V_\chi(x)=\sum_{n\le x}v_\chi(n),\quad
 S_\chi(y)=\sum_{n\le y}\chi(n).
\]

If chi is nonprincipal then |S_chi(y)|<=k, by periodicity and zero sum on a full period. The exact hyperbola identity with both real cutoffs sqrt(x) is

\[
 V_\chi(x)=
 \sum_{a\le\sqrt{x}}\mu_k(a)S_\chi(x/a)
 +\sum_{b\le\sqrt{x}}\chi(b)M_k(x/b)
 -M_k(\sqrt{x})S_\chi(\sqrt{x}).                   \tag{8}
\]

The first and last terms have total absolute value <=2k sqrt(x), using the trivial bound for M_k in the last term. In the middle term, x/b>=sqrt(x), so (7) gives

\[
 \left|\sum_{b\le\sqrt{x}}\chi(b)M_k(x/b)\right|
 \ll k^2xD_{c_1/\sqrt2}(x)\sum_{b\le\sqrt{x}}b^{-1}
 \ll k^2xL(x)D_{c_0/2}(x).
\]

By (3), therefore,

\[
 |V_\chi(x)|\ll k^2xD_{c_2}(x).                   \tag{9}
\]

We also need the cruder uniform bound

\[
 |V_\chi(x)|\le kx,                               \tag{10}
\]

which follows directly by summing mu_k(a)S_chi(x/a) over a<=x.

**Principal case.** For the principal character, mu_k*chi is exactly epsilon, the convolution identity. Thus V_chi(x)=1 for x>=1. Bound (10) holds directly, and (9) holds after enlarging its absolute constant, since 1/x is bounded by a constant times D_{c_2}(x) by (3). No zero-sum character bound is used for the principal character. Consequently (9)--(10) hold for every character, with the same absolute constants.

## 4. Uniform control of the totient factor

Retain A03's exact definitions

\[
 a_\chi(n)=\frac{\varphi(n)}n v_\chi(n),\qquad
 a_\chi=v_\chi*\eta_\chi,
\]

where eta_chi is multiplicative, eta_chi(1)=1, and, for r>=1,

\[
 \eta_\chi(p^r)=
 \begin{cases}
 (1-\chi(p))/p,&p\nmid k,\\
 0,&p\mid k.
 \end{cases}                                      \tag{11}
\]

For completeness, the prime-power local factor for a_chi is

\[
 \frac{1-(1-1/p+\chi(p)/p)X}{1-\chi(p)X}
 =\frac{1-X}{1-\chi(p)X}
 \left(1+\frac{1-\chi(p)}p\frac{X}{1-X}\right)
 \quad(p\nmid k).
\]

All three local factors equal 1 for p dividing k. This proves the convolution identity without analytic continuation.

There is a global moment bound, uniform in k and chi:

\[
 \sum_{d\ge1}\frac{|\eta_\chi(d)|}{d^{3/4}}
 \le\prod_p\left(1+\frac{2}{p(p^{3/4}-1)}\right)
 =:K<\infty.                                     \tag{12}
\]

Indeed, summing the local geometric series gives the displayed factor, whose excess over 1 is O(p^{-7/4}). The product is bounded effectively by comparison with the convergent sum over all integers >=2. In particular sum |eta_chi(d)|/d<=K.

Put A_chi(x)=sum_{n<=x}a_chi(n). Split

\[
 A_\chi(x)=\sum_{d\le x}\eta_\chi(d)V_\chi(x/d)
\]

at d=sqrt(x). Equations (9), (2), and (12) bound the first part by C K k^2xD_{c_3}(x). Equations (10) and (12) bound the second by

\[
 kx\sum_{d>\sqrt{x}}\frac{|\eta_\chi(d)|}{d}
 \le Kkx^{7/8}.
\]

Absorbing x^{-1/8} gives, for all x>=1,

\[
 |A_\chi(x)|\ll k^2xD_{c_3}(x),\qquad
 |A_\chi(x)|\le Kkx.                              \tag{13}
\]

The second inequality follows separately from (10) applied to the whole convolution, and is retained for small-argument tails.

## 5. Partial summation, including its lower range

Define

\[
 G_\chi(x)=\sum_{u\le x}\varphi(u)v_\chi(u).
\]

The exact partial summation formula is

\[
 G_\chi(x)=xA_\chi(x)-\int_1^x A_\chi(t)\,dt.
 \tag{14}
\]

On 1<=t<=sqrt(x), the crude bound in (13) makes the integral O(kx). On sqrt(x)<=t<=x, equations (13) and (2) give

\[
 |A_\chi(t)|\ll k^2tD_{c_4}(x),
\]

whose integral is O(k^2x^2D_{c_4}(x)). The endpoint xA_chi(x) has this same bound. The lower-range O(kx) term is absorbed by (3). Thus uniformly for every character and x>=1,

\[
 |G_\chi(x)|\ll k^2x^2D_{c_4}(x),\qquad
 |G_\chi(x)|\ll kx^2.                             \tag{15}
\]

The crude bound follows directly from the crude bound in (13) and (14). For the principal character, a_chi=epsilon and G_chi(x)=1 exactly; both inequalities remain valid. These estimates make no assumption relating k to x, which is essential when x=N/s is small.

## 6. Non-units and the final uniform bound

Let f_k(m)=-{m/k}, so ||f_k||_infinity<=1 and

\[
 b_k(N)=\sum_{j\le N}\varphi(j)(\mu*f_k)(j).
\]

As in A03, write j=su with s in S_k and (u,k)=1. On unit residues v modulo k define

\[
 F_s(v)=\sum_{d\mid s}\mu(d)f_k((s/d)v)
       =\sum_{\chi\bmod k}c_{s,\chi}\chi(v).
\]

Only squarefree divisors contribute, and character orthogonality therefore gives

\[
 |c_{s,\chi}|\le2^{\omega(k)}\le k,
 \qquad \#\{\chi\bmod k\}=\varphi(k)\le k.         \tag{16}
\]

These bounds hold independently of s. Splitting the divisor sum and using phi(su)=phi(s)phi(u) gives the exact identity

\[
 b_k(N)=\sum_{\substack{s\in S_k\\s\le N}}
 \varphi(s)\sum_{\chi\bmod k}c_{s,\chi}G_\chi(N/s).
 \tag{17}
\]

In particular, no character formula on non-unit residues is assumed; their prime-power parts are retained in F_s.

Split (17) at s=sqrt(N). In the first part, apply the decaying bound of (15), and note N/s>=sqrt(N). By (16) and (6), its absolute value divided by N^2 is

\[
 \ll k^4D_{c_5}(N)
 \sum_{s\in S_k}\frac{\varphi(s)}{s^2}
 \le k^4D_{c_5}(N)\sum_{s\in S_k}s^{-1}
 \le k^5D_{c_5}(N).                               \tag{18}
\]

For the second part use the crude bound of (15), not a large-argument estimate. Its absolute value divided by N^2 is at most

\[
 Ck^3\sum_{\substack{s\in S_k\\s>\sqrt N}}
       \frac{\varphi(s)}{s^2}
 \le Ck^3\sum_{\substack{s\in S_k\\s>\sqrt N}}s^{-1}
 \le Ck^5N^{-1/4}.                                \tag{19}
\]

The last step is exactly the half-moment bound in (6). Absorbing N^{-1/4} by (3) proves (U) with c=c_5. For k=1, f_1=0, so b_1(N)=0 identically and (U) also holds. The proof above already includes k=2.

Finally, k<=(log N)^B implies

\[
 k^5D_c(N)\le(\log N)^{5B}e^{-c\sqrt{\log(2N)}}
 \ll_{A,B}(\log N)^{-A},
\]

since t^{A+5B}exp(-c sqrt(t)) is bounded on t>=log(3). This proves (Target), with effective implied constants. For each fixed B the indicated coordinates are <=N for all sufficiently large N, so the conclusion uses actual matrix coordinates in its asymptotic range.

**Status:** complete quantitative proof. The only external analytic input is the sourced ordinary effective Mertens bound. Every auxiliary estimate is uniform for all x>=1 and k>=2; losses are at most k^5. No eigenvector or normalization analysis is included. A03 is preserved, and only this A06 note was written during this turn.


---

## notes/A07-profile-decay-and-integral.md

SHA256: 81e0bf8b085d05144cf194a7f5cb8a5e041954093098db99af9e077191983d07

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


---

## notes/A08-reduction-theorem.md

SHA256: 0c10dadaee4edb87fc2015e19316074a2b6ac2a9059df708a79da919eb8098a4

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


---

## notes/A09-scalar-certificate.md

SHA256: 796ceb3c9d5fc5b814a650c5afd5a70866b4033527923f7d8a5f190e08a44bbb

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


---

## code/certify_scalar.py

SHA256: 08395c08e2be59a5a4e97d234d8af032ffa7f19d9d383e77723721ba9d551587

```python
#!/usr/bin/env python3
"""Integer-only enclosures for the scalar proof. Floats are display-only.

No third-party dependencies. Run: /usr/bin/python3 code/certify_scalar.py
The mathematical interpretation is in notes/A09-scalar-certificate.md.
"""
from array import array
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
import time

SCALE = 10**30
LIMIT = 10**6


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


def atan_bounds(inv, terms):
    s = sum((F((-1)**j, (2*j+1)*inv**(2*j+1))
             for j in range(terms)), F(0))
    nxt = F((-1)**terms, (2*terms+1)*inv**(2*terms+1))
    return min(s, s+nxt), max(s, s+nxt)


def constant_bounds(primes, cutoff, scale):
    a0, a1 = atan_bounds(5, 32)
    b0, b1 = atan_bounds(239, 10)
    pi0, pi1 = 16*a0-4*b1, 16*a1-4*b0
    z0, z1 = pi0*pi0/6, pi1*pi1/6
    assert 1 < z0 <= z1 < F(5, 3)
    prod0 = prod1 = e1 = scale
    for p in primes:
        den = (p-1)*(p+1)**2
        prod0 = prod0*(den+1)//den
        prod1 = ceildiv(prod1*(den+1), den)
        root0 = isqrt(p*scale**2)
        eden = (p+1)*(root0-scale)
        e1 = ceildiv(e1*(eden+scale), eden)
    # Sum over omitted primes bounded by sum over ALL integers > cutoff.
    # G's transformed product has local excess < (p-1)^(-3).
    tailden = 2*(cutoff-1)**2
    prod1 = ceildiv(prod1*tailden, tailden-1)
    # E_(1/2)'s omitted local excess <= 2*p^(-3/2).
    # Its sum is <=4/sqrt(cutoff); exp(s)<=1/(1-s).
    rootcut = isqrt(cutoff)
    assert rootcut > 4
    e1 = ceildiv(e1*rootcut, rootcut-4)
    c0f = F(3*scale**2, 2*prod1)*z0
    c1f = F(3*scale**2, 2*prod0)*z1
    c0 = c0f.numerator//c0f.denominator
    c1 = ceildiv(c1f.numerator, c1f.denominator)
    assert 2*scale < c0 <= c1 < 213*scale//100
    assert e1 < 4*scale
    return c0, c1, e1


def main():
    started = time.process_time()
    q, n = SCALE, LIMIT
    spf = array('I', range(n+1))
    for p in range(2, isqrt(n)+1):
        if spf[p] == p:
            for j in range(p*p, n+1, p):
                if spf[j] == j:
                    spf[j] = p
    primes = [p for p in range(2, n+1) if spf[p] == p]
    c0, c1, e1 = constant_bounds(primes, n, q)
    lo, hi = [0]*(n+1), [0]*(n+1)
    lo[1] = hi[1] = q
    for a in range(2, n+1):
        p = spf[a]
        m = a//p
        if m % p == 0:
            lo[a], hi[a] = lo[m], hi[m]
        else:
            lo[a] = lo[m]*p//(p+1)
            hi[a] = ceildiv(hi[m]*p, p+1)
    # Separate trial-division oracle checks the sieve/recurrence for small a.
    for a in range(1, 301):
        value, rem = F(1), a
        p = 2
        while p*p <= rem:
            if rem % p == 0:
                value *= F(p, p+1)
                while rem % p == 0:
                    rem //= p
            p += 1
        if rem > 1:
            value *= F(rem, rem+1)
        assert F(lo[a], q) <= value <= F(hi[a], q)
    al = ah = bl = bh = 0
    qq = q*q
    endpoint_checks = half_checks = 0
    minimum_endpoint_margin = None
    minimum_half_margin = None
    for m in range(1, n+1):
        mm = m*m
        al += lo[m]
        ah += hi[m]
        bl += mm*lo[m]
        bh += mm*hi[m]
        if m >= 2:
            # U(m) <= 3/4. Lower enclosure of A-B/m² is positive.
            tnum = al*mm-bh
            assert tnum > 0
            margin = 4*c0*tnum-(4*m-3)*qq*mm
            assert margin > 0, ('upper', m)
            endpoint_checks += 1
            if minimum_endpoint_margin is None or margin < minimum_endpoint_margin:
                minimum_endpoint_margin = margin
        if m < n:
            for r in (0, 1):
                # On [m+r/2,m+(r+1)/2], U >= a-C*A+C*B/b².
                # Prove that conservative lower enclosure exceeds -3/4.
                bb = (2*m+r+1)**2
                margin = ((4*m+2*r+3)*qq*bb
                          -4*c1*ah*bb+16*c0*bl)
                assert margin > 0, ('lower', m, r)
                half_checks += 1
                if minimum_half_margin is None or margin < minimum_half_margin:
                    minimum_half_margin = margin
    # Tail uses eta(1000)<=1/50, zeta(2)<5/3, E_(1/2)<4,
    # sqrt(1000/10^6)<4/125, K<183/1000, C<213/100.
    assert F(1, 1000) < F(4, 125)**2
    # K=1/6+sqrt(3)/108 <183/1000 follows from sqrt(3)<7/4.
    assert F(1, 6)+F(7, 432) < F(183, 1000)
    tail = F(213, 100)*(F(5, 6)*(F(1, 50)*F(5, 3)
                                  +F(4, 125)*4)+F(183, 1000))
    assert tail < F(68, 100)
    # Negative control: an intentionally false endpoint claim U(2)<=0 fails.
    assert 2*q*4-c1*3 > 0
    result = {
        'status': 'ALL_INTEGER_ASSERTIONS_PASSED',
        'limit': n, 'scale': str(q), 'prime_count': len(primes),
        'C_lower_numerator': str(c0), 'C_upper_numerator': str(c1),
        'C_denominator': str(q), 'E_half_upper_numerator': str(e1),
        'E_half_denominator': str(q),
        'endpoint_checks': endpoint_checks, 'half_interval_checks': half_checks,
        'endpoint_upper_bound': '3/4 for integer 2<=m<=10^6',
        'interval_lower_bound': '-3/4 on [1,10^6]',
        'tail_upper_bound': str(tail),
        'external_input': 'Ramare 2015 Theorem 1.2: |m(x)| log(x)<=1/12 for x>=687; |m(x)|<=1 for x>=1',
        'process_cpu_seconds': time.process_time()-started,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    dest = Path(__file__).resolve().parents[1]/'results'/'scalar-certificate.json'
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

```


---

## results/scalar-certificate.json

SHA256: 4ed5069772c238a158cc850e91f361fa3fa7e454e40860a70b498ce9fa5b9dc1

```json
{
  "status": "ALL_INTEGER_ASSERTIONS_PASSED",
  "limit": 1000000,
  "scale": "1000000000000000000000000000000",
  "prime_count": 78498,
  "C_lower_numerator": "2129344320757238687316827406299",
  "C_upper_numerator": "2129344320758303361606554217009",
  "C_denominator": "1000000000000000000000000000000",
  "E_half_upper_numerator": "3588756760325859013900248680340",
  "E_half_denominator": "1000000000000000000000000000000",
  "endpoint_checks": 999999,
  "half_interval_checks": 1999998,
  "endpoint_upper_bound": "3/4 for integer 2<=m<=10^6",
  "interval_lower_bound": "-3/4 on [1,10^6]",
  "tail_upper_bound": "202847/300000",
  "external_input": "Ramare 2015 Theorem 1.2: |m(x)| log(x)<=1/12 for x>=687; |m(x)|<=1 for x>=1",
  "process_cpu_seconds": 5.215804,
  "script_sha256": "08395c08e2be59a5a4e97d234d8af032ffa7f19d9d383e77723721ba9d551587"
}

```
