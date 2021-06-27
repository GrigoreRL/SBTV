import numpy as np
from numba import jit,njit
@njit
def E_func_user(q,t,fparams):
    E = np.array([0.0,0.0,0.0])
    return E
@njit
def B_func_user (q,t,fparams):
    B = np.array([0.0,0.0,0.0])
    return B