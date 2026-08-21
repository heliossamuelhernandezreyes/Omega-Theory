"""Omega Theory Phase 04 — relative mode invariants.
No gauge group, phase, charge, complex amplitudes, or observational constants.
"""
import itertools
from fractions import Fraction


def pair_differences(s):
    return tuple(s[i]-s[j] for i in range(len(s)) for j in range(i+1,len(s)))


def quotient_signature(s):
    return tuple(s[i]-s[0] for i in range(1,len(s)))


def centered_mean(s):
    n=len(s)
    m=Fraction(sum(s),n)
    return tuple(Fraction(x)-m for x in s)


if __name__ == "__main__":
    print("channels vectors quotient_signatures relative_dimension shift_tests invariant_tests")
    for n in range(1,6):
        vecs=list(itertools.product(range(-2,3), repeat=n))
        sigs={quotient_signature(v) for v in vecs}
        tests=ok=0
        for v in vecs:
            for c in range(-3,4):
                w=tuple(x+c for x in v)
                tests+=1
                ok += pair_differences(v)==pair_differences(w)
        print(n,len(vecs),len(sigs),max(n-1,0),tests,ok)
