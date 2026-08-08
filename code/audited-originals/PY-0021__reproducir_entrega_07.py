import numpy as np
def metrics(costs,supports,n_raw):
    c=np.asarray(costs,float)
    s=np.asarray(supports,float)
    r=np.exp(-c)
    return {
        "p":len(c)/n_raw,
        "Q_deficit":1-len(c)/n_raw,
        "Q_obstruction":np.sum(s*c),
        "Q_spectral":1/np.sum(r)
    }
print(metrics([1,1,1,1],[1,1,1,1],8))
print(metrics([5,5,5,5],[1,1,1,1],8))
