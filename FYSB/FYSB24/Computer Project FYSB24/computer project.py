# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt
import Radial_functions as Rf
import radial
import radiallog
import pandas as pd

#Density functions, no. of nodes = n-l-1
r = linspace(0,20,1000)
Z = 1
'''
P1s = Rf.P1s(r,Z)
P3s = Rf.P3s(r,Z)
P3p = Rf.P3p(r,Z)
P3d = Rf.P3d(r,Z)
plt.plot(r,P1s**2,label='1s')
plt.plot(r,P3s**2,label='3s')
plt.plot(r,P3p**2,label='3p')
plt.plot(r,P3d**2,label='3d')
legend()

#Potential 
def V(r,Z,l):
    return -(Z/r) + (l*(l+1))/(2*(r**2))

r1 = linspace(0.1,10,1000)
Vs = V(r1,Z,0)
Vp = V(r1,Z,1)
Vd = V(r1,Z,2)
figure()
plt.plot(r1,Vs,label='s')
plt.plot(r1,Vp,label='p')
plt.plot(r1,Vd,label='d')
grid()
ylim(-0.5,0.5)
legend()
'''

N = [1,2,3,6,9]
Enrad = []
Enlog = []
#GPn = []
Pn = []
rn = []
Expn = []

for n in N:
    l = 0
    Z = 1
    r,P,Erad,exprad,gridrad = radial.radial(l,n,Z)
    r,P,Elog,explog,gridlog = radiallog.radiallog(l,n,Z)
    Enrad.append(['Radial',n,Erad,gridrad])
    Enlog.append(['RadialLog',n,Elog,gridlog])
    
    #GPn.append(GP)
    Pn.append(P*sqrt(r))
    rn.append(r)
    Expn.append(exprad)
    
Enlst = Enrad + Enlog
df = pd.DataFrame(Enlst)
df.columns =['Rad/Log', 'Orbital', 'Energy', 'Grid No.']
print (df)
table = df
cell_text = []
for row in range(len(table)):
    cell_text.append(table.iloc[row])
    
plt.table(cellText=cell_text, colLabels=table.columns, loc='center')
plt.axis('off')

'''
figure()
plt.plot(rn[0],Pn[0],label='1s')
plt.plot(rn[1],Pn[1],label='2s')
plt.plot(rn[2],Pn[2],label='3s')
plt.plot(rn[3],Pn[3],label='6s')
plt.plot(rn[4],Pn[4],label='9s')
xlim(0,30)
legend()
'''
plt.figure()
'''
plt.plot(rn[0],Pn[0]**2,label='1s')
vlines(Expn[0],0,1)

plt.plot(rn[1],Pn[1]**2,label='2s')
vlines(Expn[1],0,2)
plt.plot(rn[2],Pn[2]**2,label='3s')
vlines(Expn[2],0,2)
plt.plot(rn[3],Pn[3]**2,label='6s')
vlines(Expn[3],0,2)
plt.plot(rn[4],Pn[4]**2,label='9s')
vlines(Expn[4],0,2)
xlim(0,300)
'''

plt.legend()

def Rie_sums(F):
    N1 = 100000
    X = linspace(0,N1/100,N1)
    h = 0.01
    I = 0
    for x in X:
        I = I + h*x*F(x,Z)**2
    return I

R = Rie_sums(Rf.P2s)

plt.plot(rn[0],Pn[0]**2,label='1s')
plt.vlines(Expn[0],0,1)
plt.vlines(R,0,1)