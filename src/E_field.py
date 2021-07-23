import numpy as np
import numba
import matplotlib.pyplot as plt
import seaborn as sns

from charge_core import*
from constants import*

class E_field:
    def __init__(self,R):        
        self.content = np.zeros(R,dtype=float)

    def display_f(self):
        print(self.content)
    
    def hmap_f(self):
        svm = sns.heatmap(self.content, annot=True, cmap='coolwarm',linecolor='white', linewidths=1)
        svm.figure.savefig('svm_conf.png', dpi=400)
