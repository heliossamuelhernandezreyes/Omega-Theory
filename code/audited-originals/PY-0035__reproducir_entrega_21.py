import numpy as np
def U(t,omega):
    return np.exp(-1j*omega*t)
print(abs(U(.3+.7,2)-U(.3,2)*U(.7,2)))
