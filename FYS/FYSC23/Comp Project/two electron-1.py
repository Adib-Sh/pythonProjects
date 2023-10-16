#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:05:05 2023

@author: adamche
"""
import numpy as np
import matplotlib.pyplot as plt

L = 6
V = -1
epss = [-15,0,0,0,0,0]  #On-site energies
pots = [0,15,15,15,15,15]  #Interaction energies


indices = [i for i in range(0,L**2)]
basis = []

for i in range(0,L):
    for j in range(0,L):
        basis.append((i,j))


def rho(d,n1,n2,t):    
    H0 = np.zeros([L**2,L**2])
        
    for i in indices:
        for j in indices:
            if (basis[i][0] == basis[j][0]) and (basis[i][1] == basis[j][1] + 1 or basis[i][1] == basis[j][1] - 1):
                H0[i,j] = V
            if (basis[i][1] == basis[j][1]) and (basis[i][0] == basis[j][0] + 1 or basis[i][0] == basis[j][0] - 1):
                H0[i,j] = V
            if i == j:
                m, n = basis[i]
                H0[i,j] = epss[m] + epss[n]
                if m == n:
                    H0[i,j] += pots[m]
                    
    Hp = np.zeros([L**2,L**2])
    epss1 = [-15+d,0,0,0,0,0]
    
    for i in indices:
        for j in indices:
            if (basis[i][0] == basis[j][0]) and (basis[i][1] == basis[j][1] + 1 or basis[i][1] == basis[j][1] - 1):
                Hp[i,j] = V
            if (basis[i][1] == basis[j][1]) and (basis[i][0] == basis[j][0] + 1 or basis[i][0] == basis[j][0] - 1):
                Hp[i,j] = V
            if i == j:
                m, n = basis[i]
                Hp[i,j] = epss1[m] + epss1[n]
                if m == n:
                    Hp[i,j] += pots[m]
    
    phi0c, phi0v = np.linalg.eig(H0)
    phi0v = phi0v.T
    
    Eg = min(phi0c) #ground state energy
    Eg_indices = np.where(phi0c == Eg)[0]
    Eg_index = Eg_indices[0] #Gets index of first appearance
    phi0 = phi0v[Eg_index] #ground state vector
    
    lmbd_c, lmbd_v = np.linalg.eig(Hp)
    lmbd_v = lmbd_v.T
    
    def phinn(n,n1,t):
        S = 0
        for p in range(0,len(lmbd_c)):
            c1 = np.exp(-1j*lmbd_c[p]*t)
            ind = basis.index((n,n1))
            c2 = lmbd_v[p][ind]
            c3 = 0
            for l in indices:
                term = lmbd_v[p][l]*phi0[l]
                c3 += term
            S += c1*c2*c3
        return S
    
    def rho1(n,n1,t):
        phi_n = phinn(n,n1,t)
        return np.real(np.conj(phi_n)*phi_n)
    
    return rho1(n1,n2,t)

''' 
#check
totalprob = 0
for v in basis:
    m,n = v
    totalprob += rho(d,m,n,0)
print(totalprob)

'''

def updens(d,n,t):
    S = 0
    for i in range(0,L):
        S += rho(d,n,i,t)
    return S

def downdens(d,n,t):
    S = 0
    for i in range(0,L):
        S += rho(d,i,n,t)
    return S

d = 5
plt.figure()
tvalues = np.linspace(0,25,100)
plt.subplot(1,2,1)
for i in range(0,L):
    rhovalues = [updens(d,i,t) for t in tvalues]
    plt.plot(tvalues, rhovalues, label = f'site {i+1}')
    plt.title(f'Spin-Up density ($\Delta$ = {d})')
    plt.xlabel('Time')
    plt.ylabel('$p_{nn}(t)$')
    plt.ylim([0,1])
    plt.legend()

plt.subplot(1,2,2)
for i in range(0,L):
    rhovalues = [rho(d,i,i,t) for t in tvalues]
    plt.plot(tvalues, rhovalues, label = f'site {i+1}')
    plt.title(f'Average double occupancy ($\Delta$ = {d})')
    plt.xlabel('Time')
    plt.ylabel('$p_{nn}(t)$')
    plt.ylim([0,1])
    plt.legend()

plt.tight_layout()
plt.show()

    







