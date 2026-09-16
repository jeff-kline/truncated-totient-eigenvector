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
