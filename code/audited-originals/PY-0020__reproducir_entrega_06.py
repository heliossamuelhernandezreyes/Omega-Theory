import numpy as np
from scipy.stats import linregress
def source(r,A=1,s=.4):
    return -A/((2*np.pi)**1.5*s**3)*np.exp(-.5*(r/s)**2)
def solve(r,S):
    dr=np.diff(r); J=np.zeros_like(r); integ=r*r*S
    J[1:]=np.cumsum(.5*(integ[:-1]+integ[1:])*dr)
    up=np.zeros_like(r); up[1:]=J[1:]/r[1:]**2
    u=np.zeros_like(r)
    for i in range(len(r)-2,-1,-1):
        u[i]=u[i+1]-.5*(up[i+1]+up[i])*(r[i+1]-r[i])
    return u,up
r=np.linspace(0,50,6000); u,up=solve(r,source(r))
m=(r>=5)&(r<=30)
fit=linregress(np.log10(r[m]),np.log10(np.abs(up[m])))
print(fit.slope,fit.rvalue**2)
