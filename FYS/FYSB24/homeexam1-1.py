#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:31:01 2023

@author: adamche
"""
from numpy import *
from matplotlib.pyplot import *
import sys

R = 10973732 #m-1
hbar = 1.05457182 * 10**(-34)
c = 3 * 10**8
me = 9.11 * 10**(-31)
a0 = 5.29177210903 * 10**(-11)

a = hbar/(a0*me*c)



def E_n(n):
    return -9*R/(n**2)


def corrf(n,j):
    t1 = 9*a**2/(n**2)
    t2 = 0.75 - n/(j+0.5)
    return -t1*t2*E_n(n)


    
n = [1,2,3]
l = [0,1,2]
j = [[0.5],[0.5,1.5],[1.5,2.5]]

nlj = []
Enj = []
Enlst = []
for i in range(0,3):
    N = n[i]
    for k in range(0,i+1):
        J = j[k]
        L = l[k]
        for m in J:
            E = E_n(N) + corrf(N,m)
            Enj.append(E)
            nljs = (N,L,m)
            nlj.append(nljs)
            Enlst.append([nljs,E])

def get_transition(p):
    T = nlj[p]
    n1,l1,j1 = T[0], T[1], T[2]
    E1 = Enj[p]
    levels = []
    energies = []
    for i in range(0,9):
        n2, l2, j2 = nlj[i][0], nlj[i][1], nlj[i][2]
        if l1 - l2 == 1 and j1 - j2 <= 1:
            '''
            for not allowing same n transitions
            if abs(n1 - n2) == 1: 
                levels.append(nlj[i])
                energies.append(Enj[i])
            else:
                pass
            '''
            levels.append(nlj[i])
            energies.append(Enj[i])
        else:
            pass
    wavelengths = []
    for k in range(0,len(energies)):
        Es = energies[k]
        dE = E1-Es
        if dE == 0:
            wl = 0
        else:
            wl = 1/dE
        wavelengths.append(wl)
    return T, levels, wavelengths


wavedict = {}
for i in range(0,9):
    P = get_transition(i)
    A, B, C = P[0], P[1], P[2]
    for j in range(0,len(B)):
        
        tran = (A) + (B[j])
        wavedict[tran] = abs(C[j])

result = {}    
for key,value in wavedict.items():
    if value not in result.values():
        result[key] = value
        
result = {key:val for key, val in result.items() if val != 0}