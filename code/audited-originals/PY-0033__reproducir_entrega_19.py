import numpy as np
P=np.array([[.7,.3],[.2,.8]])
path=[0,1,1,0]
p=np.prod([P[a,b] for a,b in zip(path[:-1],path[1:])])
print(p,-np.log(p))
