from E_field import*
import numpy as np
sp = [50,50]
sample = E_field(sp)
r = [20,30]
v = [0,0]
#sample.display_f()
c1 = charge(5,r,v)
c1.add_field(sample)
sample.hmap_f()