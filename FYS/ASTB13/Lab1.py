import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table
import numpy as np
import math

#-------------------------------------------------

v0  = 220
R0 = 8.5e3

vmax=[112.87,60.63,40.03,36.51,28.22]
l = [50,60,70,80,90]
r = []
for i in range(0,len(l)):
    rl = R0*math.sin(math.radians(l[i]))
    r.append(rl)
v= []    
for j in range(0,len(vmax)):
    vl = vmax[j]+v0*math.sin(math.radians(l[j]))
    v.append(vl)
    
plt.plot(r,v)