import numpy as np
from vectors import*

class charge:
    def __init__(self,q,r,v):
        self.charge = q
        self.position = r
        self.velocity = v
    
    def add_field(self,space):
        dim = space.order
        if dim==2:
            for i in range((space.shape)[0]):
                for j in range((space.shape)[1]):
                    if distance(np.array([i,j]),self.position)==0:
                        (space.content)[i][j] += 0
                    else:
                        (space.content)[i][j] += 1 * self.charge / distance(np.array([i,j]),self.position)
