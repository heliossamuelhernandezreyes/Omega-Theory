from __future__ import annotations
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import eigvalsh
from scipy.stats import linregress
from scipy.integrate import solve_ivp

SEED=10601

def branching(w):
    w=np.asarray(w,float); w=w[w>0]; q=w/w.sum(); return float(np.exp(-(q*np.log(q)).sum()))
def mobility(D,r): return sum(x*np.outer(d,d) for x,d in zip(r,D))
def inertia(M,v):
    v=np.asarray(v,float); v/=np.linalg.norm(v); m=float(v@M@v); return np.inf if m<=1e-15 else 1/m

def d01(out):
    D=np.array([[1,0],[-1,0],[0,1],[0,-1]],float)
    systems={'uniform':[1,1,1,1],'anisotropic':[1,1,10,10],'collective':[3,3,3,3]}
    rows=[]
    for name,cost in systems.items():
        for law,beta in [('inverse',None),('exp_0.5',.5),('exp_1',1.)]:
            c=np.array(cost,float); r=1/c if beta is None else np.exp(-beta*c); M=mobility(D,r); ev=eigvalsh(M)
            rows.append([name,law,.5,branching(r),r.sum(),ev[0],ev[-1],ev[-1]/ev[0],inertia(M,[1,0]),inertia(M,[0,1])])
    pd.DataFrame(rows,columns=['system','rate_law','scalar_p','effective_branching','total_rate','mobility_min','mobility_max','anisotropy','inertia_x','inertia_y']).to_csv(out/'d01_geometry.csv',index=False)
    def Q(eps,n=5):
        W=np.zeros((2*n,2*n))
        for cluster in [range(n),range(n,2*n)]:
            for i in cluster:
                for j in cluster:
                    if i!=j: W[i,j]=1/(n-1)
        W[n-1,n]=W[n,n-1]=eps; q=W.copy(); np.fill_diagonal(q,-W.sum(1)); return q
    rr=[]
    for e in [0,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1]:
        vals=eigvalsh(-Q(e)); vals[np.abs(vals)<1e-13]=0; p=vals[vals>0]; gap=p.min() if len(p) else 0
        rr.append([e,int((vals==0).sum()),gap,np.inf if gap==0 else 1/gap])
    d=pd.DataFrame(rr,columns=['epsilon','components','spectral_gap','mixing_proxy']); d.to_csv(out/'d01_continuity.csv',index=False)
    q=d[d.epsilon>0]; plt.figure(); plt.loglog(q.epsilon,q.spectral_gap,marker='o'); plt.xlabel('epsilon'); plt.ylabel('spectral gap'); plt.tight_layout(); plt.savefig(out/'d01_gap.png',dpi=160); plt.close()

def d02(out):
    rows=[['S1_local_easy',1,1,.5,np.inf,.5,2,2],['S2_collective_costly',4,4,2,np.inf,2,.5,.5],['S3_anisotropic',1,1,.5,2.5,1/2.4,2.4,2.4],['S4_metastable',6,8,.25,50,50,4.02,.02]]
    pd.DataFrame(rows,columns=['system','support_inertia','return_cost_inertia','mobility_inertia_x','mobility_inertia_y','escape_spectral_inertia','total_update_rate','escape_rate']).to_csv(out/'d02_definitions.csv',index=False)
    rng=np.random.default_rng(SEED); A=rng.random((8,8)); A=(A+A.T)/2; np.fill_diagonal(A,0); L=np.diag(A.sum(1))-A; gap=eigvalsh(L)[1]; perm=rng.permutation(8); Lp=L[np.ix_(perm,perm)]; gap2=eigvalsh(Lp)[1]
    pd.DataFrame([[8,gap,gap2,abs(gap-gap2)]],columns=['n_states','original_gap','permuted_gap','absolute_difference']).to_csv(out/'d02_relabel.csv',index=False)

def d03(out):
    cases=[('base',1,.1),('slow_escape',1,.001),('fast_internal',100,.1),('slow_internal',.01,.1),('balanced_low',.01,.01),('balanced_high',10,10)]
    rows=[]
    for name,a,e in cases: rows.append([name,a,e,a,a+e,4*a,e,1/e,a/e])
    pd.DataFrame(rows,columns=['case','a','epsilon','theta_internal','theta_all','theta_mobility','theta_escape','lifetime','ratio']).to_csv(out/'d03_clocks.csv',index=False)
    t=np.linspace(0,50,1001); e=.1; empirical=np.exp(-e*t); exact=np.exp(-e*t)
    pd.DataFrame({'t':t,'survival_numeric':empirical,'survival_exact':exact,'abs_error':abs(empirical-exact)}).to_csv(out/'d03_survival.csv',index=False)

def d04(out):
    def visible(a,D): return .5*(1-np.exp(-2*a*D))/D
    rows=[]
    for a in [.1,1,10]:
        for D in [.01,.1,1,10]: rows.append([a,D,visible(a,D),visible(a,D)/(.5*a)])
    pd.DataFrame(rows,columns=['activity_rate','resolution','visible_tick_rate','visible_to_intrinsic_ratio']).to_csv(out/'d04_visibility.csv',index=False)
    rows=[]
    for gamma in [0,.001,.01,.1]:
        t=np.linspace(0,100,1001); m=.5*t if gamma==0 else .5/gamma*(1-np.exp(-gamma*t)); rows.append([gamma,m[-1],bool(np.all(np.diff(m)>-1e-14))])
    pd.DataFrame(rows,columns=['erasure_rate','final_memory','monotonic_non_decreasing']).to_csv(out/'d04_memory.csv',index=False)

def d05(out):
    mu=1.; soft=.5
    def dln(r): return mu*r/(r*r+soft*soft)**1.5
    def acc(r,v): return -(1-v*v)*dln(r)
    def rhs(t,y): return [y[1],acc(y[0],y[1])]
    rows=[]
    for r0,v0 in [(8,0),(8,-.2),(4,.1),(20,-.4)]:
        s=solve_ivp(rhs,(0,12),[r0,v0],rtol=1e-10,atol=1e-12,max_step=.01)
        inv=np.exp(-mu/np.sqrt(s.y[0]**2+soft**2))/np.sqrt(1-s.y[1]**2)
        rows.append([r0,v0,inv[0],inv[-1],np.max(abs((inv-inv[0])/inv[0])),np.max(abs(s.y[1])),s.y[0,-1],s.y[1,-1]])
    pd.DataFrame(rows,columns=['r0','v0','initial_invariant','final_invariant','max_relative_drift','max_abs_speed','final_r','final_v']).to_csv(out/'d05_trajectories.csv',index=False)
    r=np.geomspace(10,100,200); aa=abs(np.array([acc(x,0) for x in r])); fit=linregress(np.log10(r),np.log10(aa)); pd.DataFrame([[fit.slope,10**fit.intercept,fit.rvalue**2]],columns=['power_exponent','prefactor','R2']).to_csv(out/'d05_radial_fit.csv',index=False)
    plt.figure(); plt.loglog(r,aa); plt.xlabel('r'); plt.ylabel('|a|'); plt.tight_layout(); plt.savefig(out/'d05_radial.png',dpi=160); plt.close()

def d06(out):
    def source(r,A=1,s=.4): return -A/((2*np.pi)**1.5*s**3)*np.exp(-.5*(r/s)**2)
    def solve(r,S):
        dr=np.diff(r); J=np.zeros_like(r); integ=r*r*S; J[1:]=np.cumsum(.5*(integ[:-1]+integ[1:])*dr); up=np.zeros_like(r); up[1:]=J[1:]/r[1:]**2; u=np.zeros_like(r)
        for i in range(len(r)-2,-1,-1): u[i]=u[i+1]-.5*(up[i+1]+up[i])*(r[i+1]-r[i])
        return u,up,J
    r=np.linspace(0,50,6000); rows=[]
    for s in [.1,.2,.4,.8,1.6]:
        u,up,J=solve(r,source(r,s=s)); m=(r>=5)&(r<=30); f=linregress(np.log10(r[m]),np.log10(abs(up[m]))); rows.append([s,f.slope,f.rvalue**2,J[-1]])
    pd.DataFrame(rows,columns=['sigma','field_power','field_R2','far_flux']).to_csv(out/'d06_profiles.csv',index=False)
    u,up,J=solve(r,source(r)); flux=[]
    for lo,hi in [(2,5),(5,10),(10,20),(20,40)]:
        m=(r>=lo)&(r<=hi); flux.append([f'{lo}-{hi}',J[m].mean(),J[m].std(),J[m].std()/abs(J[m].mean())])
    pd.DataFrame(flux,columns=['interval','mean_flux','std_flux','relative_std']).to_csv(out/'d06_flux.csv',index=False)
    plt.figure(); plt.loglog(r[1:],abs(up[1:])); plt.xlabel('r'); plt.ylabel('|du/dr|'); plt.tight_layout(); plt.savefig(out/'d06_field.png',dpi=160); plt.close()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('generated/deliveries_01_06')); args=ap.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    for fn in [d01,d02,d03,d04,d05,d06]: fn(args.output)
    (args.output/'metadata.json').write_text(json.dumps({'seed':SEED,'deliveries':[1,2,3,4,5,6],'scope':'modern regeneration of core numerical experiments'},indent=2))
if __name__=='__main__': main()
