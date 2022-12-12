from logging import raiseExceptions
import numpy as np
import matplotlib.pyplot as plt
# Parameters
ximax=8
ximin=-ximax
Nsteps=100*2*ximax
nu0=6.0

epsilon = -3.999018571 #shooting method: excited state (1 node): -0.99829, ground state: -3.999018571
q = np.sqrt(-epsilon)
h = (ximax-ximin)/Nsteps
xi = np.linspace(ximin,ximax,Nsteps)

philist = [1, np.exp(q*h)]

def v(i):
    return -nu0/(np.cosh(xi[i])**2)

for i in range(2,Nsteps):
    f = v(i-1) - epsilon
    phi_i = (2+h**2*f)*philist[i-1] - philist[i-2]
    philist.append(phi_i)

#Shooting method
'''
plt.plot(xi,philist)
plt.grid()
plt.show()

'''

#====================================================
#Bisection method
emax = -0.1
emin = -nu0



def phi(i,eps=epsilon):
    philist = [1, np.exp(q*h)]
    if i == 0:
        return philist[0]
    elif i == 1:
        return philist[1]
    else:
        for j in range(2,i):
            f = v(j-1) - eps
            phi_j = (2+h**2*f)*philist[j-1] - philist[j-2]
            philist.append(phi_j)
        return philist

phimax = phi(Nsteps,emax)

phimin = phi(Nsteps,emin)

def checknode(l):
    a = 0 
    for i in range(0,len(l)-1):
        diff = abs(l[i]+l[i+1])
        if diff < abs(l[i]) or diff < abs(l[i+1]):
            a += 1 
        else:
            pass
    return a

if checknode(phimax)  == 0 or checknode(phimin) > 0:
    print('solution not in range')
else:
    n = checknode(phimax)

def findeig(n,iter=10000):
    emax = -0.1
    emin = -nu0
    phimax = phi(Nsteps,emax)
    phimin = phi(Nsteps,emin)
    for i in range(0,iter):
        epsnew = (emin+emax)/2.0
        phinew = phi(Nsteps,epsnew)
        if checknode(phinew)  == n or checknode(phimin) > n:
            emin = epsnew
            phimin = phinew
        else:
            emax = epsnew
            phimax = phinew
        if abs((emin-emax)/(emin+emax)) < 1e-8:
            break
        else:
            pass
    return epsnew

def checkphi(n,N=Nsteps):
    eig = findeig(n)
    phis = []
    phis = phi(N,eig)
    x = phis[-2]*phis[-1] - phis[1]*phis[-1]**2
    print(x)
    if x < 0:
        return print('no new nodes')
    if x > 0:
        return print('one more node')

print(findeig(0),findeig(1))
checkphi(0)
plt.plot(xi,phi(Nsteps,findeig(0)))
plt.show()