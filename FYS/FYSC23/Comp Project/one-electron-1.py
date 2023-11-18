#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:16:26 2023

"""
import numpy as np
import matplotlib.pyplot as plt
import sys

#One-electron

L = 6
V = -1
epsilon_1 = -2
indices = [i for i in range(0,L)]

def rho(eps,n,t):

    H0 = np.zeros([L,L])
    
    for i in indices:
        for j in indices:
            if (i+1) == j:
                H0[i,j] = V
            elif i == (j+1):
                H0[i,j] = V
    
    Hp = np.zeros([L,L])
    
    H_1 = np.zeros([L,L])
    H_1[0,0] = eps
    
    Hp = H0 + H_1
    
    #Finding initial state
    
    phi0c, phi0v = np.linalg.eig(H0)
    phi0v = phi0v.T
    Eg = min(phi0c) #ground state energy
    Eg_indices = np.where(phi0c == Eg)[0]
    Eg_index = Eg_indices[0] #Gets index of first appearance
    phi0 = phi0v[Eg_index] #ground state vector
    
    lmbd_c, lmbd_v = np.linalg.eig(Hp)
    lmbd_v = lmbd_v.T
    
    def phin(n,t):
        S = 0
        for p in range(0,len(lmbd_c)):
            c1 = np.exp(-1j*lmbd_c[p]*t)
            c2 = lmbd_v[p][n]
            c3 = 0
            for m in indices:
                term = lmbd_v[p][m]*phi0[m]
                c3 += term
            S += c1*c2*c3
        return S
    
    def rho1(n,t):
        phi_n = phin(n,t)
        return np.real(np.conj(phi_n)*phi_n)
    
    return rho1(n,t)

'''
#check
totalprob = 0
for i in indices:
    totalprob += rho(i,1)
print(totalprob)
'''

'''
#site 1  (have 0 - 5 as site numbers)
n = 1
tvalues = np.linspace(0,20,100)
rhovalues1 = [rho(-2,n,t) for t in tvalues]
rhovalues2 = [rho(2,n,t) for t in tvalues]

plt.plot(tvalues, rhovalues1, label = '$\epsilon_1 = $ -2')
plt.plot(tvalues, rhovalues2, label = '$\epsilon_1 = $ 2')
plt.title(f'densities at site {n+1}')
plt.ylim(0,1)
plt.legend()
'''
d = 2
tvalues = np.linspace(0,20,100)
for n in indices:
    rhovalues1 = [rho(d,n,t) for t in tvalues]
    plt.plot(tvalues, rhovalues1, label = f'site {n+1}')
    plt.title(f'Probability at different sites when perturbation is {d}')
    plt.xlabel('Time')
    plt.ylabel('$p_n(t)$')
    plt.ylim(0,1)
    plt.legend()


'''
t = 0
sites = [i+1 for i in range(0,L)]
prob = [rho(0.1,i-1,t) for i in sites ]


plt.plot(sites,prob,'x')
plt.title(f'time {t}')
'''
























