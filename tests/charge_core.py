import numpy as np
import numba
from numba import cuda

from vectors import*

@cuda.jit
def add_field(r,q,space):
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bw = cuda.blockDim.x
    pos = int(tx + ty*bw)
    dist2 = 0.0
    for i in range(2):
        dist2 += (r[i] - (tx*i+ty*(1-i)))**2
    dist2 = dist2**0.5
    if pos < space.size:
        if dist2 == 0:
            space[tx,ty] += 0.0
        else:
            space[tx,ty] += 1 * q /(dist2)**2
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
                    if int(distance(np.array([i,j]),np.array(self.position)))==0:
                        (space.content)[i][j] += 0
                    else:
                        (space.content)[i][j] += 1 * self.charge / (distance(np.array([i,j]),self.position)**2)

    
    def add_potential(self,space):
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

class charge_circle:
    def __init__(self,Q,pt,r,en_=1,st_=0,V=0,T=0):
        self.charge = Q
        self.center = pt
        self.radius = r
        self.velocity = V
        self.rotate = T
        self.path = draw_circle(pt,r,en=en_,st=st_)
    def add_circle_field(self,space):
        for i in prange(self.path):
            q_c = charge(self.charge,i,self.velocity)
            q_c.add_field(space)
