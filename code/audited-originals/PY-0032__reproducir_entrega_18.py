from collections import defaultdict
import numpy as np
seen=defaultdict(set); x=0; h=()
for t in range(1,20):
 x=(x+1)%4; h=h+(t,); seen[x].add(h); print(t,x,np.log(len(seen[x])))
