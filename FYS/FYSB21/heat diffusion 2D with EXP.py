#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:11:35 2022

@author: adamche
"""
from socketserver import ForkingUDPServer
from matplotlib import pyplot as plt
import numpy as np
from scipy import special
from matplotlib import animation
import matplotlib.colors
from matplotlib import cm

T0 = 10000

rmax = 50

h = 0.01
xlim = 8000 #km
ylim = 8000 #km
n = xlim//10


def Heat(x,y,t,a,lim=rmax): #need modification
    #if np.sqrt(x**2+y**2) > 6500:
     #   a = 0
    #else:
    c=1.e-35
    x0, y0 = 5000, 3930.6
    r = np.sqrt((x-x0)**2 + (y-y0)**2)
    t1 = special.erf((lim-r)/(np.sqrt(4*a*t)))
    t2 = special.erf((-lim-r)/(np.sqrt(4*a*t)))
    return T0*0.5*(t1-t2)*np.exp(-c*t)

fig1 = plt.figure()
ax1 = plt.axes(xlim = [4800,5200],
               ylim = [3800,4200])



xaxis = np.linspace(0,xlim,n)
yaxis = np.linspace(0,ylim,n)
X,Y = np.meshgrid(xaxis,yaxis,indexing='xy')
R = np.sqrt(X**2 + Y**2)


radius = [0,1210, 3470, 6300, 6325, 6360] #km
temperature = [6000, 3800, 3000, 2000, 200] #celsius
alpha = [1.e-11,5.e-12,1.e-12,5.e-13,1.e-13] #alpha in km²s-¹

T = np.zeros([n,n])
A = np.zeros([n,n])

for i in range(0,len(radius)-1):
    T[(R >= radius[i]) * (R <= radius[i+1])] = temperature[i]
    A[(R >= radius[i]) * (R <= radius[i+1])] = alpha[i]

cf = ax1.imshow(np.flipud(Heat(X,Y,0,A)+T),extent=[0,8000,0,8000],cmap='jet')
fig1.colorbar(cf,label='Temperature ($^{\circ}C$)')
cf.set_clim(0,T0)
ax1.set_xlabel('x in kilometres')
ax1.set_ylabel('y in kilometres')
ax1.set_aspect('equal')

def animate(i):
    global cf
    t = 3600*24*365.25*50000*i #time increment 1million yrs;  seconds in a year: 31536000
    T1 = Heat(X,Y,t,A)
    cf = ax1.imshow(np.flipud(T1+T),extent=[0,8000,0,8000],cmap='jet')
    ax1.title.set_text('Time in 50k-Years: %1.1f'  %i)
    cf.set_clim(0,T0)
    return cf

anim = animation.FuncAnimation(fig1, animate,
                            frames = 80,
                            save_count=0,
                            interval = 10,
                            blit = False)
 
anim.save('2DEarth.gif', fps = 5)
