import numpy as np
import numba
import matplotlib.pyplot as plt
import seaborn as sns

from charge_core import*
from constants import*

class E_field:
    def __init__(self,R):        
        self.content = np.zeros(R,dtype=float)
        self.order = np.ndim(self.content)
        self.shape = np.shape(self.content)

    def display_f(self):
        print(self.content)
        print(self.order)
        print((self.shape)[1])
    
    def hmap_f(self):
        svm = sns.heatmap(self.content, cmap='coolwarm',linecolor='white', linewidths=0.01)
        svm.figure.savefig('svm_conf.png', dpi=400)
