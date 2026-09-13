from itertools import combinations
from collections import Counter


def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for i,j in edges:R[i][j]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]: R[i][j]=True
    return tuple(tuple(r) for r in R)


def enumerate_fixed_order_posets(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    seen=set()
    for mask in range(1<<len(pairs)):
        edges=[pairs[k] for k in range(len(pairs)) if (mask>>k)&1]
        seen.add(closure(n,edges))
    return list(seen)


def covers(R,a,b):
    if not R[a][b]: return False
    return not any(R[a][z] and R[z][b] for z in range(len(R)) if z not in (a,b))


def minimal_common_uppers(R,a,b):
    n=len(R)
    ups=[u for u in range(n) if (u==a or R[a][u]) and (u==b or R[b][u])]
    return [u for u in ups if not any(v!=u and v in ups and R[v][u] for v in ups)]


def sibling_pairs(R):
    out=[]
    for p in range(len(R)):
        kids=[x for x in range(len(R)) if covers(R,p,x)]
        for a,b in combinations(kids,2): out.append((p,a,b))
    return out


def downsets(R):
    n=len(R)
    ans=[]
    for mask in range(1<<n):
        D={i for i in range(n) if (mask>>i)&1}
        ok=True
        for x in D:
            if any(R[y][x] and y not in D for y in range(n)):
                ok=False; break
        if ok: ans.append(D)
    return ans


def maximal_future_extension(R,D):
    n=len(R)
    Q=[[False]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n): Q[i][j]=R[i][j]
    for i in D: Q[i][n]=True
    return tuple(tuple(r) for r in Q)


def run():
    print('POSETS')
    print('n\tposets\tsibling_pairs\tno_recombination\tunique_join\tmultiple_joins\tall_unique_posets')
    all_posets={}
    for n in range(3,6):
        P=enumerate_fixed_order_posets(n); all_posets[n]=P
        cls=Counter(); all_unique=0
        for R in P:
            vals=[]
            for _,a,b in sibling_pairs(R):
                k=len(minimal_common_uppers(R,a,b))
                t='no_recombination' if k==0 else 'unique_join' if k==1 else 'multiple_joins'
                cls[t]+=1; vals.append(t)
            if vals and all(v=='unique_join' for v in vals): all_unique+=1
        total=sum(cls.values())
        print(n,len(P),total,cls['no_recombination'],cls['unique_join'],cls['multiple_joins'],all_unique,sep='\t')

    print('\nFUTURE_EXTENSIONS')
    print('n\tunique_join_pairs\textension_cases\tpreserved\tdestroyed')
    for n in (4,5):
        unique_pairs=cases=preserved=destroyed=0
        for R in all_posets[n]:
            pairs=[]
            for p,a,b in sibling_pairs(R):
                m=minimal_common_uppers(R,a,b)
                if len(m)==1: pairs.append((p,a,b,m[0]))
            unique_pairs += len(pairs)
            for p,a,b,c in pairs:
                for D in downsets(R):
                    Q=maximal_future_extension(R,D)
                    cases+=1
                    if len(minimal_common_uppers(Q,a,b))==1: preserved+=1
                    else: destroyed+=1
        print(n,unique_pairs,cases,preserved,destroyed,sep='\t')

if __name__=='__main__': run()
