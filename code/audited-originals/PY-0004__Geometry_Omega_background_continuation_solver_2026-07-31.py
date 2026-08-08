import numpy as np, json
from scipy.integrate import solve_ivp, solve_bvp

kappa=.1; a=b=1.; xmin=1e-4; xmax=40.

def rhs_ivp(x,y,Om):
    f,g,h,al=y; N=1-2*h/x
    W=f*f-a*f**4+b*f**6
    eps=Om**2*f*f/al**2+N*g*g+W
    Pr=Om**2*f*f/al**2+N*g*g-W
    hp=.5*kappa*x*x*eps
    ap=al*(h+.5*kappa*x**3*Pr)/(x*x*N)
    Np=-2*hp/x+2*h/x**2
    gp=-(2/x+ap/al+Np/(2*N))*g-(Om**2/al**2-(1-2*a*f*f+3*b*f**4))*f/N
    return np.array([g,gp,hp,ap])

def fun(x,y,p):
    Om=p[0]; f,g,h,al=y; N=1-2*h/x
    W=f*f-a*f**4+b*f**6
    eps=Om**2*f*f/al**2+N*g*g+W
    Pr=Om**2*f*f/al**2+N*g*g-W
    hp=.5*kappa*x*x*eps
    ap=al*(h+.5*kappa*x**3*Pr)/(x*x*N)
    Np=-2*hp/x+2*h/x**2
    gp=-(2/x+ap/al+Np/(2*N))*g-(Om**2/al**2-(1-2*a*f*f+3*b*f**4))*f/N
    return np.vstack((g,gp,hp,ap))

def bc(ya,yb,p,fc):
    Om=p[0]; kval=np.sqrt(max(1-Om*Om,1e-12))
    return np.array([ya[0]-fc, ya[1], ya[2], yb[3]-1, yb[1]+(kval+1/xmax)*yb[0]])

# Seed from validated shooting solution at fc=.1
fc0=.1; Om0=.9883382437756101; ac0=.971593432149837
# simple central start is enough for seed IVP
sol0=solve_ivp(lambda x,y: rhs_ivp(x,y,Om0),(xmin,xmax),[fc0,0,0,ac0],rtol=1e-9,atol=1e-11,max_step=.03,dense_output=True)
x=np.linspace(xmin,xmax,1200); y=sol0.sol(x)

fcs=[.1,.125,.15,.175,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.93,.95,.97,.98,.99,.995,.998,.999,.9995,.9998]
out=[]; p=np.array([Om0])
for fc in fcs:
    # rescale scalar profile to new central amplitude as continuation predictor
    scale=fc/y[0,0]
    yguess=y.copy(); yguess[0]*=scale; yguess[1]*=scale
    sol=solve_bvp(lambda xx,yy,pp: fun(xx,yy,pp),lambda ya,yb,pp: bc(ya,yb,pp,fc),x,yguess,p=p,tol=2e-5,max_nodes=30000,verbose=0)
    if sol.status!=0 or not (0<sol.p[0]<1):
        print('FAIL',fc,sol.status,sol.message,sol.p,flush=True); break
    x=np.linspace(xmin,xmax,1600); y=sol.sol(x); p=sol.p.copy()
    f,g,h,al=y; N=1-2*h/x
    rec=dict(fc=fc,pc=1-fc**2,Omega=float(p[0]),alpha_c=float(al[0]),mass=float(h[-1]),Cmax=float(np.max(2*h/x)),alpha_inf=float(al[-1]),f_end=float(f[-1]),nodes=int(np.sum(f[:-1]*f[1:]<0)),rms=float(np.max(sol.rms_residuals)))
    out.append(rec); print(json.dumps(rec),flush=True)
open('/mnt/data/omega_background_branch.json','w').write(json.dumps(out,indent=2))
# save final profile if reached
if out:
    arr=np.column_stack([x,y[0],y[1],y[2],1-2*y[2]/x,y[3],y[3]/np.sqrt(1-2*y[2]/x)])
    np.savetxt('/mnt/data/omega_background_final_profile.csv',arr,delimiter=',',header='x,f,fx,h,N,alpha,Sigma',comments='')
