
import numpy as np
import pandas as pd
from scipy.linalg import eigvalsh

def mobility_tensor(displacements,rates):
    return sum(r*np.outer(d,d) for r,d in zip(rates,displacements))

def directional_inertia(M,v):
    v=np.asarray(v,float); v/=np.linalg.norm(v)
    return 1/(v@M@v)

# Example: anisotropic identity
D=np.array([[1,0],[-1,0],[0,1],[0,-1]],float)
rates=np.array([1,1,0.2,0.2])
M=mobility_tensor(D,rates)
print("M=",M)
print("Ix=",directional_inertia(M,[1,0]))
print("Iy=",directional_inertia(M,[0,1]))
