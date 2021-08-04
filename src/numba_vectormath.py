import numpy as np
import numba
from numba import jit

@jit(nopython=True)
def distance(a,b):
    d = 0
    for i in range(max(len(a),len(b))):
        d += (a[i] - b[i])**2
    return d**0.5