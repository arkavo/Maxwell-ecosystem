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
    

        