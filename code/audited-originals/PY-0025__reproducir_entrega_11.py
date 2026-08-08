import numpy as np
def alpha_ratio(u,a,b):
    return np.exp(-(a-b)*u)
for a,b in [(1,1),(1,0),(0,1)]:
    print(a,b,alpha_ratio(1,a,b))
