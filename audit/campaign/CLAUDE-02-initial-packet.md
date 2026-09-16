```text
ORIENTATION
Self-contained mathematics; no checkout, installation, or email access required.

MODEL OWNERSHIP
An Opus-tier model owns this adversarial mathematical examination. Cheaper models may reproduce frozen arithmetic only; do not delegate proof judgment.

READ FIRST / BINDING RULES
Use a FRESH chat. No email, contact, publication, or nested agents. Do not read the companion proof bundle yet. Spend at most 5 active minutes trying to find a concrete failure in either exact claim below. Failure to derive a proof is not a counterexample. Preserve your initial report before any proof is supplied. The owner will relay it to the coordinator.

STATE / FORMAL CLAIMS
Claim A. For integer n>=1, define R_n(j,k)=#{integers a:1<=a<=floor(j/k), gcd(a,j)=1}, for 1<=j,k<=n. Let Q_n=R_n^T R_n, v_n its positive Euclidean-unit dominant eigenvector, and h_n(k)=1/k. Then
  lim_{n->infinity} n*||h_n-(v_n^T h_n)v_n||_infinity = 1.
Every entry of Q_n is positive because the last row of R_n is positive. The convention is phi(1)=1.

Claim B. For integer a>=1 let g(a)=product_{p prime,p|a}p/(p+1), with g(1)=1. Define
  G=product_{p prime}(1-1/[p(p+1)]), C=3/(2G),
  U(t)=t-C*sum_{1<=a<=t}g(a)*(1-a^2/t^2), t>=1 real.
Then |U(t)|<=1 for every t>=1, with equality only at t=1.

No proof or computational certificate is included in this initial packet. These are the claims to attack, not premises you must accept. The original matrix conjecture is the final conjecture of Jeffery Kline, Unital Sums of the Möbius and Mertens Functions, Journal of Integer Sequences23 (2020), Article20.8.1: https://cs.uwaterloo.ca/journals/JIS/VOL23/Kline/kline4.html . The exact statement above is sufficient for this task.

GIT
No repository is required or supplied. Return text only; no changes or publication.

SANITY CHECK
Check n=1 conventions and U(1)=1. A finite matrix value different from 1 is not a refutation of an asymptotic limit. An unbounded prime-product truncation error is not a valid counterexample.

TASK (editable)
Attack definitions, normalizations, fixed versus growing coordinates, and the unbounded real interval. Return at most 1000 words with: STAGE INITIAL; VERDICT REFUTED, UNRESOLVED, or NOT-BROKEN; concrete evidence; coverage; dependencies; sources/tools exposed; active time. REFUTED requires a verified counterexample or contradiction. Do not claim proof verification from a failed attack. Stop and preserve this report before receiving the proof bundle.
```

After the initial report is preserved, the separate CLAUDE-02-proof-bundle.md supplies the actual argument for proof-aware auditing. TASK is the editable section.
