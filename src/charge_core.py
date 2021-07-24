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
    def __init__(self,Q,st,en,V=0,T=0,tol=0.5):
        self.charge = Q
        self.st_pt = st
        self.en_pt = en
        self.velocity = V
        self.rotate = T
        dims = np.shape(st)[0]
        x_ = np.arange(st[0], en[0], abs(en[0]-st[0])/(en[0]-st[0]))
        y_ = np.arange(st[1], en[1], abs(en[1]-st[1])/(en[1]-st[1]))
        self.path = np.array((len(x_),len(y_)))
        for i in range(len(x_)):
            if i*(en[1]-st[1])/(en[0]-st[0])-int(i*(en[1]-st[1])/(en[0]-st[0])) < tol:
                self.path[i] = ([x_[i], y_[0]+int(i*(en[1]-st[1])/(en[0]-st[0]))])

    def add_line_field(self,space):
        for i in range(np.shape(self.path)[1]):
            r = np.array([self.path[0][i],self.path[1][i]])
            q_c = charge(self.charge,r,self.velocity)
            q_c.add_field(space)
            print(str(int(i/np.shape(self.path)[1]*100))+"% done",end="\r")
