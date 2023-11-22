import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import interpolate
from uncertainties import ufloat
from uncertainties.umath import *

#-------------------------------------------------
#Data
v0  = ufloat(220,np.sqrt(220))
R0 = ufloat(8.5e3,8.5e3*1/(3.6*3600))

v=[57.68,73.72,84.02,152.50,157.67,132.93,124.60,97.74,
      99.76,91.62,81.22,61.26,48.14,39.84,36.77,37.98,33.49,28.90]
v_std = [17.27,20.30,22.67,24.11,25.92,15.12,30.52,11.74,16.98,15.67,21.59,16.36,13.47,
       12.24,11.94,12.58,12.62,11.23]

vmax=[ufloat(v[i],v_std[i]) for i in range(0,len(v))]
l = list(range(5,95,5))
l=[ufloat(math.radians(x),math.radians(0.2)) for x in l]
r = []
for i in range(0,len(l)):
    rl = R0*sin(l[i])
    r.append(rl)
v= []    
for j in range(0,len(vmax)):
    vl = vmax[j]+v0*sin(l[j])
    v.append(vl)

#seperation of values
r_n = [x.n for x in r] #nominal r
v_n = [x.n for x in v] #nominal v
r_s = [x.s for x in r] #error r
v_s = [x.s for x in v] #error v


#Fitting
r_new = np.linspace(min(r_n), max(r_n), 100)
bspline = interpolate.make_interp_spline(r_n, v_n) #curve fit of points
v_new = bspline(r_new)

fit = np.poly1d(np.polyfit(r_n, v_n, 5)) #polyfit


#Plot
fig, ax1 = plt.subplots()
#ax1.plot(r_n, v_n, '.')
ax1.errorbar(r_n, v_n, xerr=r_s, yerr=v_s, ecolor='k', fmt='o', markersize=2, capsize=5, linewidth = 1, alpha=0.6)
ax1.plot(r_n, fit(r_n),'red', label='Fit')
ax1.plot(r_new,v_new,':', color='green', label='Data')
ax1.set_xlabel('Distances from the Galactic Center (pc)')
ax1.set_ylabel('Maximum radial velocity LSR (km/s))')
title = ax1.set_title("Rotational curve of Milky Way")
title.set_y(1.2)
fig.subplots_adjust(top=0.85)
ax1.legend(loc='upper left')
plt.show()