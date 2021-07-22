import numpy as np
import numba

from charge_core import*
from constants import*

class E_field:
    def __init__(self,R):        
        self = np.zeros([R],dtype=float)