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

class charge_line:
    def __init__(self,Q,st,en,V=0,T=0):
        self.charge = Q
        self.st_pt = st
        self.en_pt = en
        self.velocity = V
        self.rotate = T
        self.path = draw_line(st,en)


    def add_line_field(self,space):
        for i in range(len(self.path)):
            r = self.path[i]
            q_c = charge(self.charge,r,self.velocity)
            q_c.add_field(space)
            print(str(int(i/len(self.path)*100))+"% done",end="\r")
