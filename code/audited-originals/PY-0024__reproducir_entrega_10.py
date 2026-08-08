import numpy as np
def current(delta,A,q,w=1):
    return q*w*np.sin(delta-q*A)
def alpha(q,w,K):
    return q*q*w/(4*np.pi*K)
print(current(.1,.02,1,1))
print(alpha(1,1,10))
