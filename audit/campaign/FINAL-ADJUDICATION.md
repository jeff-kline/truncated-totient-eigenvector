# Final correctness adjudication

Verdict: VERIFIED for the original 2020 limit and the scalar inequality, by the recorded computer-assisted proof. Coordinator accepts the argument, not merely the external verdict. No publication, formal-proof-checker claim, independent-human-validation claim, or literature-wide priority claim is made.

## Exact goal and source match

The original source ref/kline4.tex defines R=D^-1 S D, proves R(j,k)=#{a<=j/k:(a,j)=1}, and defines Q=R^T R. Its final conjecture uses the positive Euclidean-unit dominant eigenvector and h(k)=1/k. These definitions and the exact limit were rechecked directly against the preserved source. No different matrix, eigenvector normalization, or restricted coordinate range has been substituted.

## Review evidence and seals

- R01 initial matrix failure search preceded proof exposure; R02 substantively verified the matrix theorem.
- CLAUDE-02-initial.md was preserved before the full proof bundle was supplied. Its SHA256 is a80d997d19cd7f980d75c11ff48f3cb6971895802f1552ebfba344a16cf75351. Its NOT-BROKEN outcome is not treated as proof.
- The full external audit was read from the actual local report and preserved as CLAUDE-02-proof-audit.md. SHA256:649d56bccce64b55a194e723d13dd6c7a71ece39cce7115c31d8a5712d8e5c89.
- The examined proof bundle remains bf236d513b5c6d6505c0ddd0255b6f20817d5b1c758b9039194b9006510ed0af. All16 entries of candidate-integrity.json were rechecked unchanged at final adjudication.
- The scalar script's recorded hash, exact output, and all deterministic result fields had already been reproduced in a fresh temporary directory. The external audit also reports a matching-script rerun and checks the algorithm and outward rounding. Neither rerunning alone nor the floating-point exploratory plots is used as proof.

The Claude scalar construction and Claude audit share a provider, while much of the derivation and the replacement certificate were developed by the Codex coordinator. These are process-separated model examinations, not fully independent mathematical communities. Exposure is disclosed rather than converted into an unsupported independence claim.

## Requirement-by-requirement completion check

| Requirement | Authoritative evidence and conclusion |
|---|---|
| Correct original statement | Original TeX definitions and final conjecture agree with CHARTER and the examined packet. |
| Well-defined positive unit eigenvector | Entrywise positivity of Q and the sign/normalization argument are established in A04/R02. |
| Uniform matrix error | A04/R02 establish r=r_1 h-q+e with ||e||2=O(n^-3/2 log³n), hence n||e||infinity=o(1). |
| Fixed and slowly growing coordinates | A06 supplies an estimate uniform over k<=log^B n, including non-units and principal characters. External audit checks its convolution, tails, and polynomial dependence on k. |
| Larger and intermediate coordinates | A05 gives n q_k=-U(n/k)+O(log²n/k), uniformly. A08 uses both ranges; every k is covered. |
| Normalization term | A04 retains h^Tq and ||q||². A07/A08 prove the improper integral and Riemann-sum limits, yielding n r_1->rho with |rho|<1. |
| Scalar inequality on an unbounded real interval | A09 supplies the proved tail bound202847/300000<0.68 beyond10^6; the integer certificate encloses all endpoints and every half-interval up to10^6. Convexity supplies continuous upper coverage. |
| Matching lower bound | Exact column R(:,n)=e_n and the uniform remainder give n r_n->1; no upper bound is inferred solely from this endpoint. |
| Existing analytic inputs | Ramaré2015 Theorem1.2 and2019 corrigendum were read by both coordinator and auditor. The classical effective Mertens bound was source-checked by the coordinator against Ng's lecture and Lee–Leong's explicit theorem; no RH or unproved prime hypothesis is assumed. |
| Reproducible evidence | Standard-library integer script, frozen result, source copies, manifest, and non-overwriting reproduction runner are present. All proof arithmetic is exact with outward enclosures. |
| Appropriate proof review | Initial failure searches, actual proof audits, exposure records, source checks, and coordinator adjudication are preserved. Caveats addressed below. |

## Caveats adjudicated

1. The auditor did not rederive every term of A07's finite-N Mellin formula, and its alternative continuation explanation is abbreviated. The submitted finite-N argument remains the adopted proof; it needs no alternate proof. Direct integration gives

   2N^(1-s)/[3(1-s)] -2 sum_{a<=N}a^-s/[s(s+2)]
   +N^(1-s)/s -N^(-s-2) sum_{a<=N}a²/(s+2).

   Substitute sum a²=N³/3+N²/2+N/6 and sum a^-s=N^(1-s)/(1-s)+zeta(s)+O_s(N^-s), for0<s<1. The coefficient of N^(1-s), multiplied by3s(s+2)(1-s), is

   2s(s+2)-6+3(s+2)(1-s)-s(1-s)=0.

   The remaining powers tend to zero and leave -2zeta(s)/[s(s+2)]. Absolute interchange and the s->0 passage follow from the already checked coefficient moments and exponential-in-sqrt-log decay. This explicitly discharges the skipped line-by-line calculation.

2. The classical effective Mertens input is quantitative in shape; no explicit constant is required in A06/A07. Calling it merely qualitative is imprecise. The coordinator's earlier primary-source check discharges this existing-theorem dependency; the auditor was permitted to accept it.

3. C denotes a matrix locally in A04 and a scalar in later notes. Each local definition is explicit. Read the matrix C as E^T E and the scalar C as3/(2G); no equality between them is used. The script's comment eta(1000) denotes the tail supremum of |m|, as its neighboring comment, recorded input, and A09 specify. These are notation issues, not mathematical repairs. Frozen examined files are preserved.

4. The report's numerical cross-checks are not certificates and are excluded from the inference chain. In particular, its quoted0.01166 maximum sits uneasily with the quoted1/100 corollary; neither numerical claim nor that stronger corollary is needed. The adopted input is the independently read Theorem1.2 and the elementary global bound |m|<=1.

5. Intermediate sequences k->infinity with k/n->0 can occur on either side of the log³ cutoff. The two uniform estimates jointly cover them; a phrase in the report locating all such sequences in the second range is unnecessarily restrictive and is not adopted.

6. The external audit's25-minute duration exceeded its15-minute request. This is recorded as a resource overrun, not retroactive authorization or a mathematical defect. No additional native worker turn was launched.

## Completion

The adopted chain yields limsup n||r||infinity<=max(|rho|,sup|U|)=1 and liminf n||r||infinity>=1. Therefore the original limit exists and equals1. No required correctness or reproducibility obligation remains open under the recorded review standard.

A targeted final literature search recovered the original2020 paper and did not identify another resolution of this exact eigenvector conjecture. This bounded search does not establish exhaustive priority. The result may be prepared for publication later if the owner requests it; that is not part of the present authorization. The elliptope question remains deferred.
