# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
# Parameters
s = 0
ximax = int(s+8)
ximin = -ximax
Nsteps = 100*2*ximax
h = (ximax-ximin)/Nsteps
nu0 = 6.0

xi = np.linspace(ximin, ximax, Nsteps)


def v(xi):
    return -nu0/(np.cosh(xi+s)**2) - nu0/(np.cosh(xi-s)**2)


def phi(N, eps):
    q = np.sqrt(-eps)
    phiarr = np.zeros(N)
    phiarr[0], phiarr[1] = 1, np.exp(q*h)
    for i in np.arange(2, N):
        f = v(xi[i-1]) - eps
        phiarr[i] = (2+h**2*f)*phiarr[i-1] - phiarr[i-2]
    return phiarr


def checknode(eps):
    l = phi(Nsteps, eps)
    a = 0
    for i in range(0, len(l)-1):
        prod = l[i]*l[i+1]
        if prod < 0:
            a += 1
        else:
            pass
    return a


def findeig(n, iter=100000):
    emax = -0.1
    emin = -2*nu0
    for i in range(0, iter):
        epsnew = (emax+emin)/2
        phinew = phi(Nsteps, epsnew)
        x = phinew[-2]*phinew[-1] - phinew[1]*phinew[-1]**2
        if checknode(emax) == n and checknode(emin) == n:
            if x < 0:
                emin = epsnew
            if x > 0:
                emax = epsnew
        if checknode(epsnew) > n:
            emax = epsnew
        else:
            emin = epsnew
        if abs((emin-emax)/(emin+emax)) < 10**(-14):
            break
    return emax


print(findeig(0), findeig(1), findeig(2), findeig(3))
plt.plot(xi, phi(Nsteps, findeig(0)))
plt.xlabel('x/a')
plt.ylabel(r'$\psi$ (x/a)')
plt.text(4.5, 3e9, 'Ground state', fontsize = 8)
plt.text(4.5, 2.8e9, 's='+str(s), fontsize = 8)
