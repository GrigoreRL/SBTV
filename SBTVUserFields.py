import numpy as np
from numba import jit,njit
### An example file of how custom user-defined fields should look like in the file.
@njit
def E_func_user(q,t,fparams):
    omega_x = fparams[0]
    E = np.array([np.cos(omega_x*t),0.0,0.0])
    return E
@njit
def B_func_user (q,t,fparams):
    B = np.array([0.0,0.0,0.0])
    return B
