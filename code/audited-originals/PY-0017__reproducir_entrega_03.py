
import numpy as np
import pandas as pd
from scipy.linalg import eigvals

def generator(a, eps):
    return np.array([[-(a+eps), a], [a, -(a+eps)]], float)

def observables(a, eps):
    vals=np.real_if_close(eigvals(-generator(a,eps))).real
    lam=vals[vals>1e-12].min()
    return {
        "a":a,
        "eps":eps,
        "theta_internal":a,
        "theta_all":a+eps,
        "theta_mobility":4*a,
        "theta_escape":lam,
        "identity_lifetime":1/lam
    }

cases=[(1,0.1),(1,0.001),(100,0.1),(0.01,0.1)]
print(pd.DataFrame([observables(a,e) for a,e in cases]))
