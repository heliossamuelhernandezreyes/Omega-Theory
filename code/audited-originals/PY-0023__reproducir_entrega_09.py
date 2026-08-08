import numpy as np
r0=np.array([1,.7,.4,.2])
for u in [-1,0,1]:
 r=r0*np.exp(-u); print(u,r/r.sum())
