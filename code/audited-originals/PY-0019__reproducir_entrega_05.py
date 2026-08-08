
import numpy as np
from scipy.integrate import solve_ivp

c=1.0
mu=1.0
soft=0.5

def dlnN_dr(r):
    return mu*r/(r*r+soft*soft)**1.5/c**2

def acceleration(r,v):
    return -c*c*(1-v*v/c**2)*dlnN_dr(r)

def rhs(t,y):
    r,v=y
    return [v,acceleration(r,v)]

sol=solve_ivp(rhs,(0,12),[8,0],rtol=1e-10,atol=1e-12,max_step=0.01)
print("r_final",sol.y[0,-1],"v_final",sol.y[1,-1])
