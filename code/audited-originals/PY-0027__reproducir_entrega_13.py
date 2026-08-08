import numpy as np
def R(u,s=1):
    return np.exp(-s*u)
for u,v in [(0.2,.5),(-.3,1.2)]:
    print(R(u+v),R(u)*R(v))
