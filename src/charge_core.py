import numpy as np
from vectors import*

class charge:
    def __init__(self,q,r,v):
        self.charge = q
        self.position = r
        self.velocity = v
    
    def add_field(self,space):
        x,y,z = np.shape(space)
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    space[i][j][k] += 1 * self.charge