import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import interpolate
from uncertainties import ufloat
from uncertainties.umath import *

#-------------------------------------------------
#Data
v0  = ufloat(220,np.sqrt(220))
R0 = ufloat(8.5e3,np.sqrt(8.5e3))

vmax=[57.68,73.72,84.02,139.9,157.67,132.93,124.58,97.74,
      99.76,91.62,91.22,61.26,48.14,39.84,36.77,37.98,33.49,29.35]
vmax=[ufloat(x,np.sqrt(x)) for x in vmax]
l = list(range(5,95,5))
l=[ufloat(math.radians(x),0.2) for x in l]
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
ax1.errorbar(r_n, v_n, yerr=v_s, xerr=r_s, ecolor='k', fmt='o', capthick=2)
ax1.plot(r_n, fit(r_n),'red', label='Fit')
ax1.plot(r_new,v_new,':', color='gray', label='Data')
ax1.set_xlabel('Distances from the Galactic Center (kpc)')
ax1.set_ylabel('Maximum radial velocity (km/s))')
title = ax1.set_title("Rotational curve of Milky Way")
title.set_y(1.2)
fig.subplots_adjust(top=0.85)
ax1.legend(loc='upper left')