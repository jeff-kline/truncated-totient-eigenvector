# Attempt to recover cancellation in the residual

Status: coordinator derivation, not separately cold-examined. This follow-up does not change the completed conjecture proof. It produces a transfer inequality but no improved estimate for the harmonic Möbius sum.

Write m(n)=sum_{k<=n} mu(k)/k, M(x)=sum_{k<=x}mu(k), L=log(2n), alpha=v^T h, and F_n(x)=U(n/x)/n for 1<=x<=n. Constants and vectors follow A04–A09.

## The matrix approximation can be summed

A04 gives r=r_1 h-q+e with ||e||_2=O(n^(-3/2)L^3). A05 gives q_k=-F_n(k)+O(L^2/(nk)), uniformly for every k. Consequently

    r^T mu = r_1 m(n) + T_n + O(L^3/n),
    T_n = sum_{k<=n} mu(k) F_n(k).

Here the coordinate errors sum to O(L^3/n), and Cauchy–Schwarz bounds e^T mu by O(L^3/n). Since m(n)=alpha*v_1/lambda+r^T mu and alpha*v_1/lambda=O(n^-3),

    (1-r_1)m(n)=T_n+O(L^3/n).

In particular the approximation error itself is small enough to study quantitative cancellation. We know r_1=O(1/n).

## Explicit variation bound and transfer

U is continuous and piecewise differentiable. For t>=1 away from integers,

    U'(t)=1-(2C/t^3) sum_{a<=t} a^2 g(a).

Since 0<g(a)<=1 and sum_{a<=t}a^2<=t^3, |U'|<=D:=1+2C. Thus F_n is absolutely continuous and |F_n'(x)|<=D/x^2. Also |F_n(x)|<=1/n by the certified scalar bound, and F_n(n)=1/n.

For an integer 1<=K<n, define delta_K=max_{K<=j<=n}|M(j)|/j. Discrete summation by parts gives

    sum_{k=K+1}^n mu(k)F_n(k)
      = M(n)F_n(n)-M(K)F_n(K+1)
        +sum_{j=K+1}^{n-1}M(j)(F_n(j)-F_n(j+1)).

Using j integral_j^{j+1} x^-2 dx=1/(j+1), and bounding the first K summands absolutely, yields

    |T_n| <= K/n + delta_K*(1+K/n+D*log(n/K)).

Hence, for all sufficiently large n,

    |m(n)| <= [K/n + delta_K*(1+K/n+D*log(n/K))
                       + O(L^3/n)]/(1-r_1).

This is a genuine improvement over unsigned Holder when delta_K is small. For fixed T>1, K=floor(n/T), the hypothesis M(x)=o(x) gives limsup |m(n)|<=1/T; letting T grow proves m(n)->0. A hypothetical input |M(x)|/x=O(exp(-a sqrt(log x))) recovers m(n)=O(exp(-b sqrt(log n))) for some b>0 by choosing K approximately n exp(-b_0 sqrt(log n)) with b_0 small. This is a transfer of the input cancellation, not a stronger rate. Moreover the existing proof of profile decay already uses Möbius cancellation, so this is not an independent proof of the prime number theorem.

## Exact obstruction in the profile

Set eta(d)=mu(d)/prod_{p|d}(p+1). The identity g=1*eta implies mu*g=eta (Dirichlet convolution). Expand the finite sum defining U and put b=ak:

    T_n = m(n) - (C/n) sum_{b<=n} eta(b)*(1-b^2/n^2).   (exact)

Because |eta(b)|<=1/b, this gives the elementary bound

    |T_n-m(n)| <= C*(1+log n)/n.

Thus the profile's signed correlation contains m(n) itself to within a small explicit error. Bounding it by a new cancellation argument would be substantive arithmetic progress; replacing the residual by its profile does not alone achieve that progress.

The same obstruction is visible before taking a profile: E mu=e_1-a m(n), a_1=1, and S=||a||_2^2 imply q^T mu=1/S-m(n) exactly.

Conclusion: the trial succeeds in controlling variation and the summed approximation error, but stops at the original arithmetic cancellation problem. No new bound stronger than the supplied Möbius cancellation estimate is established.
