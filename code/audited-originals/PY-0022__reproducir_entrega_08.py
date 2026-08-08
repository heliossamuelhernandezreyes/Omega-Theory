import numpy as np
def identity(costs,supports,directions):
    c=np.asarray(costs,float)
    s=np.asarray(supports,float)
    D=np.asarray(directions,float)
    r=np.exp(-c)
    Q=np.sum(s*c)
    M=sum(ri*np.outer(d,d) for ri,d in zip(r,D))
    I=np.linalg.pinv(M)
    return Q,M,I
D=np.array([[1,0],[-1,0],[0,1],[0,-1]],float)
Q,M,I=identity([1,1,5,5],[1,1,1,1],D)
print("Q",Q)
print("M",M)
print("I",I)
