#!/usr/bin/env python3
"""Omega R10: independent audit of Omega-CDM v1.1 and a gauge-scalar bridge.

Only uses published solver formulae as INPUT, plus new explicit phenomenological
hypotheses. It does NOT derive electromagnetic dynamics, dark matter, or dark
energy from the potentiality ontology. Data are synthetic, no observational fit.

Checked source: https://github.com/heliossamuelhernandezreyes/Omega-CDM-A-Late-Time-Scalar-Tensor-Framework-for-Growth-Suppression/blob/main/Omega_solver.py
GitHub source blob SHA-1 on 2026-10-17: 2dab60e5328694b3cb4f45afc72eaa7b78892d5a.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

OMEGA_M0=0.31
SIGMA8_0=0.8
ALPHA=1.
BETA=.25
SOURCE_BLOB_SHA1='2dab60e5328694b3cb4f45afc72eaa7b78892d5a'


def omega_m(a):
    return OMEGA_M0/(OMEGA_M0+(1-OMEGA_M0)*a**3)


def x_proxy(a):
    """Original source's Omega_prime(a) (a preset profile, not field solution)."""
    return .05*np.exp(-5*a)


def geff(a,beta=BETA,alpha=ALPHA):
    x=x_proxy(a)
    return 1-(2*beta**2/alpha)*(x*x/(1+x*x))


def integrate_growth(beta=BETA, n=800, rtol=1e-11, atol=1e-13):
    """Original growth ODE, recomputed with explicit LCDM baseline Geff=1."""
    xmin=math.log(1e-3)
    grid=np.linspace(xmin,0.,n)
    def eq(t,y):
        a=math.exp(t);d,dp=y
        return (dp,-(2-1.5*float(omega_m(a)))*dp+1.5*float(omega_m(a))*float(geff(a,beta))*d)
    sol=solve_ivp(eq,(xmin,0),[1e-3,1e-3],t_eval=grid,dense_output=True,rtol=rtol,atol=atol)
    if not sol.success: raise RuntimeError(sol.message)
    raw,deriv=sol.y
    D=raw/raw[-1]
    f_true=deriv/raw
    f_original=deriv/D  # SOURCE BUG: derivative was not divided by raw[-1]
    true_fs8=f_true*D*SIGMA8_0
    source_fs8=f_original*D*SIGMA8_0
    # SOURCE PROXY: uses modified D and rough Omega_m^0.55 rather than separate LCDM solve
    source_lcdm_proxy=omega_m(np.exp(grid))**.55*D*SIGMA8_0
    return {'_sol':sol,'grid':grid,'a':np.exp(grid),'z':np.exp(-grid)-1,'raw':raw,'D':D,
            'd0':float(raw[-1]),'f_correct':f_true,'f_source':f_original,
            'fs8_correct':true_fs8,'fs8_original':source_fs8,
            'fs8_source_proxy':source_lcdm_proxy}


def get_at_z(data,key,z):
    """linear interpolation in ln(a), not nearest bin"""
    a=1/(1+z)
    if '_sol' in data:
        d,dp=data['_sol'].sol(math.log(a))
        d,dp=float(d),float(dp)
        if key=='fs8_correct':return dp/data['d0']*SIGMA8_0
        if key=='fs8_original':return dp*SIGMA8_0
        if key=='fs8_source_proxy':return float(omega_m(a)**.55)*d/data['d0']*SIGMA8_0
    return float(np.interp(math.log(a),data['grid'],data[key]))


def full_gauge_energy(theta,edges,links,charge=0.8,weights=None,rigidity=1.,coupling=1.):
    """Oriented U(1) square plaquette. links i->j, flux is sum around cycle.

    Physical source model: Δ_ij=theta_j-theta_i-q*A_ij and sum oriented flux.
    An arbitrary positive homogeneous gauge kinetic multiplier 'coupling' is
    separately allowed; invariance does not fix it.
    """
    if len(theta)!=4 or len(edges)!=4 or len(links)!=4:
        raise ValueError('one oriented four-link plaquette expected')
    if weights is None: weights=(.8,1.1,1.3,.9)
    matter=sum(w*(1-math.cos(theta[j]-theta[i]-charge*link))
               for (i,j),link,w in zip(edges,links,weights))
    flux=sum(links)
    field=coupling*rigidity*(1-math.cos(flux))
    return matter+field


def gauge_transform(theta,edges,links,lambda_by_vertex,charge=.8):
    return [p+charge*g for p,g in zip(theta,lambda_by_vertex)], [
        link+lambda_by_vertex[j]-lambda_by_vertex[i]
        for (i,j),link in zip(edges,links)]


def B_photon(a,xi):
    """NEW hypothesis, not in Omega-CDM: B=exp(xi*(X(a)-X(1))).

    X(a) is the original code's Omega_prime(a) function, not an independently
    solved scalar field. xi is a FREE parameter completely unconstrained by
    growth equations. Homogeneous positive B preserves U(1) gauge symmetry.
    """
    return math.exp(xi*(float(x_proxy(a))-float(x_proxy(1.))))


def alpha_ratio(a,xi):
    """Conditional electromagnetic normalization alpha(a)/alpha(today)=1/B."""
    return 1/B_photon(a,xi)


def summary():
    r=integrate_growth(); ref=integrate_growth(beta=0)
    z1=1.
    fa=get_at_z(r,'fs8_correct',z1);fb=get_at_z(ref,'fs8_correct',z1)
    fs0=get_at_z(r,'fs8_correct',0)
    original_a=get_at_z(r,'fs8_original',z1)
    original_proxy=get_at_z(r,'fs8_source_proxy',z1)
    gamma_true=math.log(float(r['f_correct'][-1]))/math.log(OMEGA_M0)
    gamma_original=math.log(float(r['f_source'][-1]))/math.log(OMEGA_M0)
    assert abs(float(r['f_correct'][-1])*SIGMA8_0-fs0)<1e-12
    assert abs(float(r['f_source'][-1])/float(r['f_correct'][-1])-r['d0'])<1e-12
    assert abs(100*(fa/fb-1))<.01
    assert abs(gamma_original-gamma_true)>.1
    assert 100*(original_a/original_proxy-1)<-10
    assert float(geff(.5))>.99999
    edges=[(0,1),(1,2),(2,3),(3,0)]
    theta=[.1,-.3,.4,-.17]; links=[.15,-.4,.09,.5];g=[.5,-.6,.2,.08]
    base=full_gauge_energy(theta,edges,links)
    t2,l2=gauge_transform(theta,edges,links,g)
    after=full_gauge_energy(t2,edges,l2)
    assert abs(base-after)<1e-12
    # Distinct physical electromagnetic predictions share identical CDM growth.
    xis=(0.,1e-5,1e-3,1e-2)
    profiles=[{'xi':xi,'z0_alpha_over_alpha0':alpha_ratio(1.,xi),
               'z1_alpha_over_alpha0':alpha_ratio(.5,xi),
               'z1_fractional_shift':alpha_ratio(.5,xi)-1,
               'G_eff_z1_unchanged':float(geff(.5))} for xi in xis]
    assert profiles[0]['z1_fractional_shift']==0
    assert profiles[1]['z1_fractional_shift']!=profiles[2]['z1_fractional_shift']
    assert all(t['G_eff_z1_unchanged']==profiles[0]['G_eff_z1_unchanged'] for t in profiles)
    # beta=0 removes the gravitational phenomenology, but xi can still be nonzero.
    assert float(geff(.5,beta=0))==1.0 and alpha_ratio(.5,1e-3)!=1
    # Same gauge invariance for different xi, even if field energy changes.
    bfac=B_photon(.5,1e-3)
    assert abs(full_gauge_energy(theta,edges,links,coupling=bfac)-full_gauge_energy(t2,edges,l2,coupling=bfac))<1e-12
    return {
       'status':'PASS: source-code audit and conditional gauge coupling checks; NOT Omega evidence',
       'provenance':{'cdm_repo_source_sha1':SOURCE_BLOB_SHA1,'cdm_version':'Omega_solver.py README v1.1',
                     'theory_reference':'canon/mathematics/MAPA_FORMALISMO.md'},
       'at_z1':{'z':z1,'G_eff':float(geff(.5)),'Omega_prime_function':float(x_proxy(.5)),
                'f_sigma8_source_implementation':original_a,
                'f_sigma8_source_LCDM_proxy':original_proxy,
                'source_implementation_vs_own_proxy_percent':100*(original_a/original_proxy-1),
                'f_sigma8_consistently_normalized':fa,
                'f_sigma8_independent_LCDM_baseline':fb,
                'corrected_relative_growth_percent':100*(fa/fb-1)},
       'at_z0':{'f_source':float(r['f_source'][-1]),'f_correct':float(r['f_correct'][-1]),
                'f_sigma8_correct':fs0,'delta_growth_unscaled_today':r['d0'],
                'gamma_source':gamma_original,'gamma_correct':gamma_true,
                'G_eff':float(geff(1))},
       'gauge':{'links':links,'vertex_phases':theta,'energy_original':base,
                 'energy_after_gauge_relabeling':after,'difference':after-base},
       'toy_photon_scalar_profiles':profiles,
       'necessary_distinctions':[
          'Omega-CDM v1.1 does not evolve a scalar field from an action: Omega_prime(a) is imposed.',
          'Omega-CDM labels a beta term disformal; this numerical ODE alone does not derive a disformal field theory.',
          'An arbitrary photon coupling xi is NOT derived from the CDM growth sector or Omega gauge symmetry.',
          'The chosen B_photon uses Omega_prime as a PROXY, not a solved phi or its dynamical derivative.',
          'Variation of alpha is a conditional model prediction, NOT observationally supported.',
          'A neutral gravitating dark sector is logically possible, but density/background/perturbations are not derived.',
          'The source growth comparison mixes normalized delta with unnormalized derivative and does not independently integrate LCDM.',
          'The solver assumes LCDM background H(a) and Omega_m0, so no dark-energy equation of state was derived.',
          'Gamma_x and r_e/s_e do not yet select alpha, xi, beta, a photon speed, mass spectrum, or dark matter abundance.'
       ]
    }


def write_artifacts(output_dir):
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    result=summary()
    (out/'OMEGA_R10_AUDITORIA_RESULTADOS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    base=integrate_growth();ref=integrate_growth(beta=0)
    with (out/'OMEGA_R10_PERFILES.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.writer(f);w.writerow(['z','G_eff','fs8_correct','fs8_LCDM_independent','growth_diff_percent','alpha_shift_xi_1e_minus3'])
        for z in (0,.25,.5,1.,1.5,2.,2.5):
            aa=1/(1+z); ff=get_at_z(base,'fs8_correct',z);fr=get_at_z(ref,'fs8_correct',z)
            w.writerow([z,float(geff(aa)),ff,fr,100*(ff/fr-1),alpha_ratio(aa,1e-3)-1])
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',default=None)
    args=parser.parse_args();res=write_artifacts(args.out) if args.out else summary()
    print(json.dumps(res,indent=2,ensure_ascii=False))