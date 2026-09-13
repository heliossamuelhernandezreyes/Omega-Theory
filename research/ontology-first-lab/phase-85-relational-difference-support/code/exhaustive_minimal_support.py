from itertools import product, combinations
from collections import Counter

# Finite falsification laboratory. A contrast is a bit-vector relative to baseline 0^n.
# Future type is supplied by an explicit structural rule. No probabilities/physics assumed.

def subsets(indices):
    for r in range(len(indices)+1):
        for c in combinations(indices, r):
            yield frozenset(c)

def restrict(x, support):
    return tuple(v if i in support else 0 for i, v in enumerate(x))

def minimal_sufficient_supports(x, future):
    base = (0,) * len(x)
    target = future(x)
    if target == future(base):
        return []
    diff = [i for i,v in enumerate(x) if v != 0]
    sufficient=[]
    for s in subsets(diff):
        if future(restrict(x,s)) == target:
            sufficient.append(s)
    return [s for s in sufficient if not any(t < s for t in sufficient)]

RULES = {
    # one distinguished relation controls future
    'single_0': lambda x: int(x[0]),
    # either of two differences is independently sufficient -> nonunique minima
    'or_01': lambda x: int(x[0] or x[1]),
    # irreducible interaction: both required -> no singleton sufficient
    'and_01': lambda x: int(x[0] and x[1]),
    # parity: several alternative minimal explanations can appear
    'parity': lambda x: sum(x) % 2,
    # silent difference: future never changes
    'silent': lambda x: 0,
}

def run(n=4):
    rows=[]
    summary=Counter()
    for rule_name, future in RULES.items():
        for x in product([0,1], repeat=n):
            if not any(x):
                continue
            mins=minimal_sufficient_supports(x,future)
            if future(x)==future((0,)*n):
                cls='silent'
            elif len(mins)==1 and len(next(iter(mins)))==1:
                cls='unique_singleton'
            elif len(mins)>1:
                cls='multiple_minima'
            elif len(mins)==1 and len(next(iter(mins)))>1:
                cls='interaction_minimum'
            else:
                cls='other'
            summary[(rule_name,cls)] += 1
            rows.append((rule_name,''.join(map(str,x)),cls,';'.join(','.join(map(str,sorted(s))) for s in mins)))
    return rows,summary

if __name__=='__main__':
    rows,summary=run()
    print('rule\tcontrast\tclass\tminimal_supports')
    for row in rows:
        print('\t'.join(row))
    print('\nSUMMARY')
    for (rule,cls),count in sorted(summary.items()):
        print(f'{rule}\t{cls}\t{count}')
