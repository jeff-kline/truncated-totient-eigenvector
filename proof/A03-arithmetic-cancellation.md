# A03: fixed-coordinate weighted arithmetic cancellation

**Result.** For every fixed integer k>=3, with the A02 definitions,

\[
 b_k(N)=\sum_{j\le N}\varphi(j)
 \left(R_N(j,k)-\frac{\varphi(j)}k\right)=o(N^2).
\]

The proof below is complete, including integers not coprime to k. In fact the argument applies to any fixed periodic function in place of the fractional-part function. Only the ordinary prime number theorem is used as an external analytic input; no PNT in arithmetic progressions, character zero-free region, or quantitative error term is needed. All limits keep k fixed.

## 1. Exact convolution and the external input

Put f(m)=-{m/k}, where braces denote fractional part. Möbius inversion gives exactly

\[
 R_N(j,k)-\varphi(j)/k
 =\sum_{d\mid j}\mu(d)f(j/d)=(\mu*f)(j).
 \tag{1}
\]

Here * denotes Dirichlet convolution and phi(1)=1. Thus it suffices to show

\[
 \sum_{j\le N}\varphi(j)(\mu*f)(j)=o(N^2).
 \tag{2}
\]

The analytic input is the classical PNT in its equivalent Möbius form

\[
 M(x):=\sum_{n\le x}\mu(n)=o(x).
 \tag{PNT}
\]

For an explicit reference, see Nathan Ng, *The sum of the Möbius function*, UBC/PIMS lecture, 27 February 2023, PDF page 7 (slide “The prime number theorem”), which states this equivalence: [lecture PDF](https://personal.math.ubc.ca/~gerg/teaching/613-Winter2023/Feb27.pdf#page=7). Everything needed beyond this input is proved below or is finite-group character orthogonality.

Let P be the finite set of primes dividing k, let S be the positive integers all of whose prime factors belong to P (including 1), and define

\[
 \mu_k(n)=\mu(n)1_{(n,k)=1},\qquad
 M_k(x)=\sum_{n\le x}\mu_k(n).
\]

The prime-power identities give mu_k=mu*1_S, so

\[
 M_k(x)=\sum_{s\in S,\ s\le x} M(x/s)=o(x).
 \tag{3}
\]

Indeed, after division by x each fixed summand tends to zero by (PNT), its absolute value is at most 1/s, and

\[
 \sum_{s\in S}\frac1s=\prod_{p\mid k}(1-1/p)^{-1}<\infty.
\]

Dominated convergence therefore proves (3).

## 2. Character convolution has zero mean

Let chi be a Dirichlet character modulo k, extended by zero on non-units, and put

\[
 v_\chi=\mu_k*\chi,\qquad
 V_\chi(x)=\sum_{n\le x}v_\chi(n).
\]

If chi is principal, then v_chi is the convolution identity epsilon (epsilon(1)=1, epsilon(n)=0 for n>1), since mu_k inverts 1_{(n,k)=1}. Hence V_chi(x)=1 for x>=1.

If chi is nonprincipal, its periodic partial sums

\[
 S_\chi(y)=\sum_{n\le y}\chi(n)
\]

have absolute value at most k. In particular, directly summing first over the chi factor gives |V_chi(x)|<=kx. To obtain cancellation, fix a positive integer T and apply the exact hyperbola identity with cutoffs x/T and T:

\[
 \begin{aligned}
 V_\chi(x)
 ={}&\sum_{a\le x/T}\mu_k(a)S_\chi(x/a)
 +\sum_{b\le T}\chi(b)M_k(x/b)\\
 &-M_k(x/T)S_\chi(T).
 \end{aligned}
 \tag{4}
\]

For fixed T the second and third terms are o_T(x), by (3). The first has absolute value at most kx/T. Consequently

\[
 \limsup_{x\to\infty}|V_\chi(x)|/x\le k/T.
\]

Letting T tend to infinity proves V_chi(x)=o(x). Together with the principal case, for every character modulo k,

\[
 V_\chi(x)=o(x),\qquad |V_\chi(x)|\le C_k x\quad(x\ge1).
 \tag{5}
\]

This uses only bounded periodic character sums, not prime distribution in residue classes.

## 3. The totient weight: exact Euler and convolution factors

Define

\[
 a_\chi(n)=\frac{\varphi(n)}n v_\chi(n).
\]

These functions vanish on non-units and are multiplicative. For p not dividing k and r>=1, writing c=chi(p),

\[
 v_\chi(p^r)=c^r-c^{r-1},\qquad
 a_\chi(p^r)=(1-1/p)(c^r-c^{r-1}).
\]

Thus, with X=p^{-z}, their local generating functions are

\[
 \sum_{r\ge0}v_\chi(p^r)X^r=\frac{1-X}{1-cX},
\]

\[
 \sum_{r\ge0}a_\chi(p^r)X^r
 =\frac{1-(1-1/p+c/p)X}{1-cX}.
 \tag{6}
\]

Their quotient is

\[
 1+\frac{1-c}{p}\frac{X}{1-X}.
\]

Equivalently, define the multiplicative function eta_chi by

\[
 \eta_\chi(1)=1,\qquad
 \eta_\chi(p^r)=
 \begin{cases}
 (1-\chi(p))/p,&p\nmid k,\ r\ge1,\\
 0,&p\mid k,\ r\ge1.
 \end{cases}
\]

Then the exact coefficient identity is

\[
 a_\chi=v_\chi*\eta_\chi.
 \tag{7}
\]

In Dirichlet-series notation (initially Re z>1), this is the requested factorization

\[
 \sum_{n\ge1}\frac{a_\chi(n)}{n^z}
 =\frac{L(z,\chi)}{\zeta_k(z)}H_\chi(z),\qquad
 \zeta_k(z)=\prod_{p\nmid k}(1-p^{-z})^{-1},
\]

\[
 H_\chi(z)=\prod_{p\nmid k}
 \left(1+\frac{1-\chi(p)}p\frac{p^{-z}}{1-p^{-z}}\right).
 \tag{8}
\]

No analytic continuation is used. Crucially,

\[
 \sum_{d\ge1}\frac{|\eta_\chi(d)|}{d}
 =\prod_{p\nmid k}
 \left(1+\frac{|1-\chi(p)|}{p(p-1)}\right)<\infty.
 \tag{9}
\]

From (7),

\[
 A_\chi(x):=\sum_{n\le x}a_\chi(n)
 =\sum_{d\le x}\eta_\chi(d)V_\chi(x/d)=o(x).
 \tag{10}
\]

To justify the last step, divide by x, use (5) for each fixed d, and dominate by C_k|eta_chi(d)|/d using (9). The same calculation gives |A_chi(x)|=O_k(x). Partial summation now gives

\[
 G_\chi(x):=\sum_{u\le x}\varphi(u)v_\chi(u)
 =x A_\chi(x)-\int_1^x A_\chi(t)\,dt=o(x^2),
 \tag{11}
\]

and |G_chi(x)|<=C'_k x^2 for x>=1. A single constant works for all characters, since their number is finite. In the principal case G_chi(x)=1, consistently with (11).

## 4. Non-units: the prime-power decomposition and summable tail

Every j has a unique factorization j=su, with s in S and (u,k)=1. Splitting each divisor into its P-part and its coprime part in (1) gives

\[
 (\mu*f)(su)=\sum_{e\mid u}\mu(e)F_s(u/e),\qquad
 F_s(v):=\sum_{d\mid s}\mu(d)f((s/d)v).
 \tag{12}
\]

On unit residues v modulo k, F_s is a well-defined function on the finite group (Z/kZ)^*. Its character expansion is

\[
 F_s(v)=\sum_{\chi\bmod k}c_{s,\chi}\chi(v),\qquad
 c_{s,\chi}=\frac1{\varphi(k)}
 \sum_{v\in(\mathbb Z/k\mathbb Z)^*}F_s(v)\overline{\chi(v)}.
 \tag{13}
\]

Only squarefree d contribute to (12), so, uniformly in s,

\[
 |F_s(v)|\le 2^{|P|}\|f\|_\infty,\qquad
 |c_{s,\chi}|\le 2^{|P|}\|f\|_\infty=:B_k.
 \tag{14}
\]

Since u and its divisors are units, (12)--(13) imply exactly

\[
 (\mu*f)(su)=\sum_\chi c_{s,\chi}v_\chi(u).
 \tag{15}
\]

There is no extension of the unit character expansion to non-units here: all non-unit prime powers reside in s, and are retained inside F_s. Because phi(su)=phi(s)phi(u), (15) yields

\[
 b_k(N)=\sum_{s\in S,\ s\le N}\varphi(s)
 \sum_{\chi\bmod k}c_{s,\chi}G_\chi(N/s).
 \tag{16}
\]

For each fixed s, its contribution divided by N^2 tends to zero by (11). By (11) and (14), the absolute value of that normalized contribution is bounded by

\[
 C'_k\varphi(k)B_k\frac{\varphi(s)}{s^2}.
\]

This is summable over S; indeed,

\[
 \sum_{s\in S}\frac{\varphi(s)}{s^2}
 =\prod_{p\mid k}
 \left(1+\sum_{r\ge1}\frac{\varphi(p^r)}{p^{2r}}\right)
 =\prod_{p\mid k}(1+1/p)<\infty.
 \tag{17}
\]

Dominated convergence in (16) proves b_k(N)/N^2 -> 0. This completes the proof.

## Checks and scope

The local factors in (6)--(8) were checked directly at every prime power, including p dividing k. The principal character was handled separately before using bounded character sums. Both infinite summations use explicit summable majorants, (9) and (17); no uniform little-o estimate in the prime-power part s is assumed. The hyperbola argument takes x to infinity with T fixed before sending T to infinity. The argument proves the requested fixed-k cancellation unconditionally using (PNT), with no remaining arithmetic gap and no claim of uniformity as k grows.

Only this note was written during A03. No nested agents, email, numerical experiments, or other workers' notes were used.
