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
