```text
ORIENTATION
Self-contained mathematical sidecar; no repository, installation, or source access required.

MODEL OWNERSHIP
Use an Opus-tier model to own the original proof and scope decisions. A cheaper model may only reproduce frozen numerical formulas; it must not certify the proof.

BINDING CONSTRAINTS
No email or external contact. No nested agents. Investigate only the scalar problem below. Do not claim that its resolution proves the parent eigenvector conjecture: separate matrix and uniformity gaps remain. Bound this first pass to 15 minutes of active work; return a concise proof, counterexample, or exact obstruction, not a broad literature survey.

STATE
For integers a>=1 define g(a)=product over primes p dividing a of p/(p+1), with g(1)=1. Define the convergent positive Euler product
  G = product over all primes p of (1-1/[p(p+1)]),
  C = 3/(2G).
For real t>=1 define
  U(t)=t-C*sum_{1<=a<=t}g(a)*(1-a^2/t^2).
The target, presently UNPROVED, is |U(t)|<=1 for all real t>=1.

Verified algebra: U(1)=1. On [m,m+1], write
  A_m=sum_{a<=m}g(a), B_m=sum_{a<=m}a^2*g(a).
Then U(t)=t-C*A_m+C*B_m/t^2. It is convex, so its maximum on each interval is at an endpoint, and its only possible interior minimum is at t=(2*C*B_m)^(1/3).

Exploratory arithmetic gives C approximately 2.12934 and values U(2) approximately .403, U(3) approximately .319, U(4) approximately .240. These are orientation only, NOT certified inequalities. A finite prime product for G causes an error amplified by t and is unsafe for large-t claims.

Possible useful identity, to check before relying on it:
  g(a)=sum_{d|a} q(d), q(d)=mu(d)/product_{p|d}(p+1),
  G=sum_{d>=1}q(d)/d (absolutely convergent).
Writing B0(y)=sum_{1<=m<=y}(1-m^2/y^2), and D0(y)=2*y/3-B0(y), one obtains
  U(t)=C*sum_{d>=1}q(d)*D0(t/d).
For y<1, B0(y)=0. Bounds discarding the signs of q may be too weak.

GIT
No checkout or commits are needed or supplied. Return text only; do not modify any repository.

SANITY CHECK
Before attacking the bound, verify by hand U(1)=1 and U(2)=2-3*C/4. These check the endpoint convention and constant. A finite computation alone cannot settle the unbounded interval.

TASK (editable)
Prove or refute |U(t)|<=1 for every real t>=1. A certified finite check plus a proved explicit tail estimate is acceptable. Standard proved number-theoretic results may be used with precise hypotheses and a source. If no proof emerges, give the strongest proved bound and the exact missing estimate. Clearly distinguish established statements from proposals. Keep the return under roughly 2000 words unless a complete proof needs more.

POINTERS
This scalar function arose as a candidate macroscopic error profile for Jeffery Kline's 2020 conjecture in “Unital Sums of the Möbius and Mertens Functions,” Journal of Integer Sequences 23, Article 20.8.1. The scalar problem above is complete and does not require reading that paper.
```

Edit TASK to redirect the sidecar; the mathematical definitions and constraints should remain intact.
