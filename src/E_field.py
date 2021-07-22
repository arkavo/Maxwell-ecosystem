import numpy as np
import numba
import matplotlib.pyplot as plt
import seaborn as sns

from charge_core import*
from constants import*

class E_field:
    def __init__(self,R):        
        self = np.zeros([R],dtype=float)

    def display_f(self):
        sns.heatmap(self)
        plt.show()