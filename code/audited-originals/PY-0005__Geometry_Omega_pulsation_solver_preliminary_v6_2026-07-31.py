import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicSpline
import pandas as pd

kappa=.1

def load_profile(path, a, b, Omega):
    df=pd.read_csv(path)
    x=df.x.values
    return x, {c:CubicSpline(x,df[c].values) for c in ['f','fx','h','N','alpha','Sigma']}, a,b,Omega

def puls_fun(x,y,p,bg):
    # y: H0,H2,ep,dep,em,dem ; p[0]=nu
    spl,a,b,Om=bg
    H0,H2,ep,dep,em,dem=y
    f=spl['f'](x); fx=spl['fx'](x); N=spl['N'](x); al=spl['alpha'](x); Sig=spl['Sigma'](x)
    h=spl['h'](x)
    # derivatives from background identities/splines
    Np=spl['N'](x,1); Sigp=spl['Sigma'](x,1)
    nu=p[0]; Op=Om+nu; Omn=Om-nu
    d=f*f; v1=1-2*a*d+3*b*d*d; mix=d*(-2*a+6*b*d)
    den=Sig*Sig*N # alpha^2
    X=(Om*Om*f*f/den)*H0 - N*fx*fx*H2 + N*fx*(dep+dem) \
      + f*(Om*Op/den+v1)*ep + f*(Om*Omn/den+v1)*em
    Z=X-2*f*v1*(ep+em)
    H2p=kappa*x*X/N - H2/x - (Np/N)*H2
    H0p=-(1/x+Np/N+2*Sigp/Sig)*H2 - kappa*x*Z/N
    common=.5*N*fx*(H0p+H2p)
    Rp=mix*em + common - Om*(Om+Op)*f/(2*den)*(H0+H2) + f*v1*H2
    Rm=mix*ep + common - Om*(Om+Omn)*f/(2*den)*(H0+H2) + f*v1*H2
    Ap=Op*Op/den-(v1+mix)
    Am=Omn*Omn/den-(v1+mix)
    coeff=2/x+Sigp/Sig+Np/N
    epp=(Rp-Ap*ep)/N-coeff*dep
    emm=(Rm-Am*em)/N-coeff*dem
    return np.vstack([H0p,H2p,dep,epp,dem,emm])

def bc(ya,yb,p,bg,xmax):
    spl,a,b,Om=bg; nu=p[0]
    kp=np.sqrt(max(1-(Om+nu)**2,1e-10)); km=np.sqrt(max(1-(Om-nu)**2,1e-10))
    return np.array([
        ya[1], ya[3], ya[5], ya[2]-1.0,
        yb[0], yb[3]+(kp+1/xmax)*yb[2], yb[5]+(km+1/xmax)*yb[4]
    ])

def solve_mode(profile,a,b,Om,nu0=.02):
    df=pd.read_csv(profile); xmin=df.x.iloc[0]; xmax=df.x.iloc[-1]
    x=np.linspace(xmin,xmax,900)
    spl={c:CubicSpline(df.x.values,df[c].values) for c in ['f','fx','h','N']}
    spl['alpha']=CubicSpline(df.x.values,df['alpha_physical'].values if 'alpha_physical' in df else df['alpha'].values)
    spl['Sigma']=CubicSpline(df.x.values,df['Sigma_physical'].values if 'Sigma_physical' in df else df['Sigma'].values)
    bg=(spl,a,b,Om)
    k=np.sqrt(max(1-Om*Om,1e-4))
    ep=np.exp(-k*x); em=.3*np.exp(-k*x)
    dep=-k*ep; dem=-k*em
    H0=.01*np.exp(-2*k*x); H2=np.zeros_like(x)
    y=np.vstack([H0,H2,ep,dep,em,dem])
    sol=solve_bvp(lambda xx,yy,p:puls_fun(xx,yy,p,bg),lambda ya,yb,p:bc(ya,yb,p,bg,xmax),x,y,p=np.array([nu0]),tol=2e-5,max_nodes=30000,verbose=1)
    print('status',sol.status,sol.message,'nu',sol.p,'rms',np.max(sol.rms_residuals))
    # residual algebraic Y
    xx=np.linspace(xmin,xmax,1800); yy=sol.sol(xx)
    H0,H2,ep,dep,em,dem=yy; f=spl['f'](xx); fx=spl['fx'](xx)
    nu=sol.p[0]; Y=fx*((Om+nu)*ep-(Om-nu)*em)-Om*f*(dep-dem)
    res=nu*H2-kappa*xx*Y
    print('constraint max',np.max(np.abs(res)), 'relative',np.max(np.abs(res))/(np.max(np.abs(nu*H2))+1e-12))
    return sol,xx,res

# omega saturated
profile='/mnt/data/Geometry_Omega_saturated_profile_fc_0p9998_2026-07-31.csv'
solve_mode(profile,1.,1.,0.6475019604999585,nu0=.05)
