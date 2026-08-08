import numpy as np
mu=np.array([1.,2.,3.])
w=np.array([.5,1.,2.])
k=np.array([2.,1.,.5])
u=1.; s=1.
mus=mu*np.exp(-s*u)
W=np.sum(mus*w); K=np.sum(mus*k)
W0=np.sum(mu*w); K0=np.sum(mu*k)
print(W/W0,K/K0,(W/K)/(W0/K0))
