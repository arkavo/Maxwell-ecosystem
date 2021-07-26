import numpy as np
import math
class vector2:
    def __init__(self,x,y):
        self = np.array([x,y])
    

class vector3:
    def __init__(self,x,y,z):
        self = np.array([x,y,z])


def distance(a,b):
    s = max(np.shape(a)[0],np.shape(b)[0])
    dist2 = 0.0
    for i in range(2):
        dist2 += (a[i] - b[i])**2
    
    return dist2**0.5

def draw_line(st,en,tol = 0.6):
    x0 = st[0]
    y0 = st[1]
    
    x1 = en[0]
    y1 = en[1]

    if x0==x1 and y0==y1:
        print("point")
        return st
    #case1 Line = horizontal
    if y0==y1:
        x_ = np.arange(x0, x1, (x0-x1)/abs(x0-x1))
        y_ = np.full((abs(x1-x0)), y0)

        path = np.array([x_,y_])
        return path
    #case2 Line = vertical
    if x0==x1:
        y_ = np.arange(y0, y1, (y0-y1)/abs(y0-y1))
        x_ = np.full((abs(y1-y0)), x0)

        path = np.array([x_,y_])
        return path
    
    else:
        s = max(abs(x0-x1),abs(y0-y1))
        x_ = np.arange(x0, x1, (x1-x0)/s)
        y_ = np.arange(y0, y1, (y1-y0)/s)
        round_index = []
        for i in range(s):
            if abs(x_[i] - int(x_[i])) <=tol and abs(y_[i] - int(y_[i])) <=tol:
                round_index.append(i)
        path = []
        for i in round_index:
            add = np.array([int(x_[i]), int(y_[i])])
            path.append(add)
        
        return path

    

    
