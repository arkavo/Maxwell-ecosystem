from E_field import*
import numpy as np


sp = [100,100]
sample = E_field(sp)
"""
r1 = [20,30]
r2 = [30,20]
r3 = [11,11]
r4 = [40,3]
r5 = [35,23]
v1 = [0,0]
v2 = [0,0]
v3 = [0,0]
v4 = [0,0]
v5 = [0,0]
#sample.display_f()

c1 = charge(25,r1,v1)
c2 = charge(33,r2,v2)
c3 = charge(34,r3,v3)
c4 = charge(12,r4,v4)
c5 = charge(60,r5,v5)

c1.add_field(sample)
c2.add_field(sample)
c3.add_field(sample)
c4.add_field(sample)
c5.add_field(sample)

a = np.array([1,1])
b = np.array([99,99])
c = np.array([1,99])
d = np.array([99,1])
l1 = charge_line(10,a,b)
l2 = charge_line(-10,c,d)
l1.add_line_field(sample)
l2.add_line_field(sample)

sample.hmap_f()
"""
r1 = [20, 10]
r2 = [10, 50]
r3 = [11, 11]
r4 = [40, 3]
r5 = [35, 23]
l1 = charge_line(10, r1, r2)
l2 = charge_line(10,r2,r3)
l3 = charge_line(10,r3,r4)
l4 = charge_line(10, r4, r5)
l5 = charge_line(10,r5,r1)

l1.add_line_field(sample)
l2.add_line_field(sample)
l3.add_line_field(sample)
l4.add_line_field(sample)
l5.add_line_field(sample)
#print(d)
sample.hmap_f()
