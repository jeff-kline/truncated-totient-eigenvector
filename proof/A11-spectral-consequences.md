# Consequences for Corollary 9 and the spectrum

Owner-requested aside while the full proof is under external examination. These are coordinator-checked consequences; no literature-wide novelty assessment is made. They do not modify the frozen proof bundle.

Write Lambda_n for the largest eigenvalue, v_n for its positive unit eigenvector, mu_n=(mu(1),...,mu(n)), H_n=||h_n||2, S_n=sum_{j<=n}phi(j)^2, and
c=(1/3)prod_p(1-2/p²+1/p³). Thus H_n²->zeta(2) and S_n~c*n³.

## A much stronger version of Corollary 9

The original paper proves Q_n*mu_n=e_1. Symmetry and the eigen-equation give the exact identity

    Lambda_n*(v_n^T mu_n)=v_n^T Q_n mu_n=v_n(1).

Therefore v_n^T mu_n is positive, and the original paper's lower bound Lambda_n>=(c+o(1))*n³ already implies

    0<v_n^T mu_n<=(c^(-1)+o(1))*n^(-3).

This improves the order n^(-3/2) in Corollary9 without using the conjecture at all. Its coarse leading constant is approximately7.005262.

The audited rank-one perturbation component A04 further gives

    v_n(1)->1/sqrt(zeta(2)),
    Lambda_n~c*zeta(2)*n³.

Substitution yields the sharper asymptotic equivalent

    v_n^T mu_n ~ [1/(c*zeta(2)^(3/2))]*n^(-3)
                ~3.32048591124*n^(-3).

No scalar supremum certificate or full conjecture proof is required for these consequences. The source identities and audited perturbation estimates suffice.

## Largest eigenvalue and remainder of the spectrum

With G=prod_p(1-1/[p(p+1)]), we have c*zeta(2)=G/3. Hence

    Lambda_n/n³ -> G/3 ~=0.2348140669998.

This identifies the leading constant between the original Proposition8's lower and upper constants c and pi²/18.

Let the remaining eigenvalues, in increasing order, be lambda_1,...,lambda_{n-1}. Set u=h/H and R=a h^T+E. A04 proves ||E||F²=O(n² log(2n)). Since R(I-uu^T)=E(I-uu^T),

    sum_{i<n}lambda_i
      =trace(Q)-Lambda_n
      <=trace(Q)-u^T Q u
      =||R(I-uu^T)||F²
      <=||E||F²
      =O(n² log(2n)).

In particular lambda_{n-1}=O(n² log n), and Lambda_n/lambda_{n-1} is bounded below by a positive constant times n/log n for sufficiently large n. This states a lower bound on the gap, not an asymptotic equivalent for the second eigenvalue.

## What does not follow for ordinary Mobius sums

Let r=h-(v^T h)v and m(n)=sum_{k<=n}mu(k)/k. Exactly

    m(n)=(v^T h)*(v^T mu)+r^T mu.

The first term is now O(n^-3). But even the full conjecture's ||r||infinity=(1+o(1))/n gives only

    |r^T mu| <=||r||infinity*sum_{k<=n}|mu(k)|
              =1/zeta(2)+o(1).

That triangle-inequality transfer does not even recover m(n)=o(1). A stronger Mobius-sum conclusion needs cancellation in r^T mu, not just a small sup norm. The arithmetic portion of our candidate itself invokes known PNT estimates, so it is not a new elementary proof of PNT.

These are improvements relative to bounds displayed in the2020 paper. Whether any is new in the intervening literature requires a separate source comparison.
