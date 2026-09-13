from itertools import combinations
from collections import Counter

# Exhaustive labeled DAG/poset laboratory for n<=5.
# We orient candidate edges i<j, compute transitive closure, and deduplicate closures.

def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for i,j in edges:R[i][j]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    R[i][j] = R[i][j] or R[k][j]
    return tuple(tuple(row) for row in R)

def covers(R,a,b):
    if not R[a][b]: return False
    n=len(R)
    return not any(R[a][z] and R[z][b] for z in range(n) if z not in (a,b))

def minimal_common_uppers(R,a,b):
    n=len(R)
    ups=[u for u in range(n) if (u==a or R[a][u]) and (u==b or R[b][u])]
    mins=[]
    for u in ups:
        if not any(v!=u and v in ups and R[v][u] for v in ups): mins.append(u)
    return mins

def classify(R):
    n=len(R); c=Counter()
    for p in range(n):
        kids=[x for x in range(n) if covers(R,p,x)]
        for a,b in combinations(kids,2):
            mins=minimal_common_uppers(R,a,b)
            if not mins:c['no_recombination']+=1
            elif len(mins)==1:c['unique_minimal_join']+=1
            else:c['multiple_minimal_joins']+=1
    return c

def enumerate_closures(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    seen=set()
    for mask in range(1<<len(pairs)):
        edges=[pairs[k] for k in range(len(pairs)) if mask>>k & 1]
        R=closure(n,edges)
        seen.add(R)
    return seen

if __name__=='__main__':
    print('n\tunique_labeled_posets_fixed_order\tsibling_pairs\tno_recombination\tunique_minimal_join\tmultiple_minimal_joins')
    for n in range(2,6):
        posets=enumerate_closures(n)
        total=Counter()
        for R in posets: total.update(classify(R))
        sibling=sum(total.values())
        print(n,len(posets),sibling,total['no_recombination'],total['unique_minimal_join'],total['multiple_minimal_joins'],sep='\t')
