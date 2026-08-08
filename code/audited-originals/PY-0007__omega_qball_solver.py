"""
Solver adimensional de candidatos Q-ball para Geometría Omega.

Phi(t,r) = F y(mr) exp(-i omega t)
U(Phi) = V_sat tanh^2(|Phi|/F)
m^2 = 2 V_sat/F^2

Ecuación:
y'' + 2 y'/x = tanh(y) sech^2(y) - (omega/m)^2 y
"""
import numpy as np
from scipy.integrate import solve_bvp

X0, XMAX = 1e-4, 40.0
x = np.linspace(X0, XMAX, 1400)

def sech2(y):
    z = np.clip(y, -40, 40)
    return 1.0 / np.cosh(z)**2

def ode(x, Y, Om):
    y, yp = Y
    return np.vstack((yp, -2*yp/x + np.tanh(y)*sech2(y) - Om**2*y))

def bc(Ya, Yb):
    return np.array([Ya[1], Yb[0]])

def guess(amplitude=2.0, width=5.0):
    y = amplitude/(1+np.exp((x-width)/0.7))
    return np.vstack((y, np.gradient(y, x)))

Om = 0.7
sol = solve_bvp(lambda xx, YY: ode(xx, YY, Om), bc, x, guess(),
                tol=2e-5, max_nodes=35000)
print(sol.status, sol.message, sol.sol(X0)[0])
