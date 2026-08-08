
import numpy as np

def visible_tick_rate(a, Delta):
    return 0.5*(1-np.exp(-2*a*Delta))/Delta

def memory(a,gamma,t):
    if gamma==0:
        return 0.5*a*t
    return (0.5*a/gamma)*(1-np.exp(-gamma*t))

for a in [0.1,1,10]:
    print(a, visible_tick_rate(a,0.1), memory(a,0.01,100))
