# Statement packet: Kline 2020 eigenvector limit

This packet contains the target and original definitions only. It contains no proposed proof or coordinator verdict.

For each positive integer n, index vectors and matrices by 1,...,n. Define

    R_n(j,k) = #{a in Z : 1 <= a <= floor(j/k), gcd(a,j)=1},
    Q_n = R_n^T R_n,
    h_n(k) = 1/k.

Let v_n denote the positive unit Euclidean-norm eigenvector corresponding to the largest eigenvalue of Q_n. The target is the assertion

    lim_{n -> infinity} n max_{1<=k<=n} |1/k - (v_n^T h_n) v_n(k)| = 1.

Source: Jeffery Kline, Unital Sums of the Möbius and Mertens Functions, Journal of Integer Sequences, 23 (2020), Article 20.8.1. The last displayed conjecture follows Corollary 9, near the end of Section 3. The counting representation of R_n occurs in Lemma 5, and Q_n is defined in Proposition 6. Source copy: ../ref/kline4.tex.

Equivalent matrix definition in the source: D_n(i,j)=1_{j divides i}, S_n(i,j)=1_{j<=i}, R_n=D_n^{-1} S_n D_n. Positivity and uniqueness of the selected eigenvector are part of the setup to check, rather than assumptions about arbitrary dominant eigenspaces.

A large finite value, slow convergence, or an apparent numerical limit does not prove or disprove this asymptotic assertion. A rigorous resolution must control n tending to infinity and the moving coordinate maximum.

No email or email access. No nested delegation. This packet does not itself authorize dispatch or computation; use the established campaign allocation.
