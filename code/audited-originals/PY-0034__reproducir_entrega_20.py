import numpy as np
E=np.array([0.,1.,2.,4.])
beta=1.
p=np.exp(-beta*E); p/=p.sum()
U=np.sum(p*E)
print(p,U,np.var(E))
