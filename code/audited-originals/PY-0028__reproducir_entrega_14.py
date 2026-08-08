import numpy as np
r0=np.array([1.,.8,.4,.2]); s0=1.; d=np.array([.1,-.1,0,0]); u=.5
r=np.exp(-s0*u)*r0*np.exp(-d*u)
print(r/r.sum())
