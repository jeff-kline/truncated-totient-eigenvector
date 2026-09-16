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
