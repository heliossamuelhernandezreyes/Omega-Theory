"""
Verificador simbólico de las componentes lineales usadas en
Geometry_Omega_Operador_Cargado_Completo_v13_2026-07-31.md.

Requiere sympy. Imprime las variaciones de T^mu_nu para el campo polar y el
campo electromagnético radial. Las fórmulas geométricas fueron verificadas con
una construcción independiente de Christoffel, Ricci y Einstein.
"""
import sympy as s

eps=s.symbols("eps")
alpha,N,F=s.symbols("alpha N F", positive=True, nonzero=True)
f,eta,fp,etap,w,u,v,nu=s.symbols(
    "f eta fp etap w u v nu", real=True
)
H0,H2=s.symbols("H0 H2", real=True)
E,e1=s.symbols("E e1", real=True)
U0,Uf=s.symbols("U0 Uf", real=True)
I=s.I

gtt=-alpha**2*(1+eps*H0)
grr=(1+eps*H2)/N
gUtt=s.series(1/gtt,eps,0,2).removeO()
gUrr=s.series(1/grr,eps,0,2).removeO()

rho=f+eps*eta
dr_t=eps*(-I*nu*eta)
dr_r=fp+eps*etap
Xt=-w+eps*u
Xr=eps*v

kin=s.expand(gUtt*dr_t**2+gUrr*dr_r**2)
x2=s.expand(gUtt*Xt**2+gUrr*Xr**2)
U=U0+eps*Uf*eta
K=F**2*(kin+rho**2*x2)+U

Ttt=2*F**2*dr_t**2+2*F**2*rho**2*Xt**2-gtt*K
Trr=2*F**2*dr_r**2+2*F**2*rho**2*Xr**2-grr*K
Ttr=2*F**2*dr_t*dr_r+2*F**2*rho**2*Xt*Xr

mixed = {
    "dTt_t_scalar": s.expand(gUtt*Ttt),
    "dTr_r_scalar": s.expand(gUrr*Trr),
    "dTt_r_scalar": s.expand(gUtt*Ttr),
    "dTtheta_theta_scalar": -K,
}

Ftr=E+eps*e1
F2=2*gUtt*gUrr*Ftr**2
EMtt=Ftr*gUrr*Ftr-s.Rational(1,4)*gtt*F2
EMrr=(-Ftr)*(gUtt*(-Ftr))-s.Rational(1,4)*grr*F2

mixed.update({
    "dTt_t_EM": s.expand(gUtt*EMtt),
    "dTr_r_EM": s.expand(gUrr*EMrr),
    "dTtheta_theta_EM": s.expand(-s.Rational(1,4)*F2),
})

for name, expr in mixed.items():
    coefficient=s.factor(s.expand(expr).coeff(eps,1))
    print(name, "=", coefficient)
