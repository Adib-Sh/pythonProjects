# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 32    
alpha = 0.25
delta = np.sqrt(1/8)

# Matrix A
A = np.zeros((N-1, N-1))
for i in range(N-1):
    A[i,i] = 2
    if i > 0:
        A[i,i-1] = -1
    if i < N-2:
        A[i,i+1] = -1

# Eigens
eigvals, eigvecs = np.linalg.eig(A)

# Sorting
sort_indices = np.argsort(eigvals)
eigvals = eigvals[sort_indices]
eigvecs = eigvecs[:,sort_indices]


eigvallst = []
w_nlst= []

# Compare numerical & analytical values
for n in range(1, N):
    w_n = 2*np.sin(n*np.pi/(2*N))
    eigvallst.append(eigvals[n-1])
    w_nlst.append(w_n**2)
    assert np.isclose(round(eigvals[n-1],5), round(w_n**2,5))
    v_n = np.sqrt(2/N) * np.sin(n*np.pi*np.arange(1,N)/(N))
    assert np.allclose(abs(eigvecs[:,n-1]), abs(v_n))


def f(alpha,u):
    F = np.zeros(N-1)
    F[0] = u[1] - 2*u[0] + alpha*(u[1] - u[0])**2 - alpha*u[0]**2
    for i in range(1, N-2):
        F[i] = u[i+1] - 2*u[i] + u[i-1] + alpha*(u[i+1] - u[i])**2 - alpha*(u[i] - u[i-1])**2
    F[N-2] = -2*u[N-2] + u[N-3] + alpha*u[N-2]**2 - alpha*(u[N-2] - u[N-3])**2
    return F

def E(u, v, eigenvalues, eigenvectors):
    En = []
    for i in range(0,4):
        e = np.dot(eigenvectors[:,i],v)**2 + eigenvalues[i]*np.dot(eigenvectors[:,i],u)**2
        En.append(0.5*e)
    return np.array(En,dtype=np.double)

#Initial conditions
n = 1
eigvecs, eigvals = eigvecs.astype(np.double), eigvals.astype(np.double)
u = 4*eigvecs[:,n-1]
v = np.zeros(N-1)
N_t = 50000

#Recurring relations for u & v
xvalues = []
Evalues = []
for m in range(0,N_t):
  F0 = f(alpha,u)
  u = u + v*delta + 0.5*F0*delta**2
  F1 = f(alpha,u)
  v = v + 0.5*delta*(F1 + F0)
  t = np.sqrt(eigvals[n-1])*m*delta/(2*np.pi)
  xvalues.append(t)
  Ek = [100*e for e in E(u,v,eigvals,eigvecs)]
  Evalues.append(Ek)

#Plotting
plt.plot(xvalues, [e[0] for e in Evalues], label = 'k=1')
plt.plot(xvalues, [e[1] for e in Evalues], label = 'k=2')
plt.plot(xvalues, [e[2] for e in Evalues], label = 'k=3')
plt.plot(xvalues, [e[3] for e in Evalues], label = 'k=4')

plt.xlabel('$\omega_1 t/2\pi$ ')
plt.ylabel(r'$E_x(\times 10^{-2})$ ')
plt.legend()
plt.xlim(0,160)
plt.ylim(0,8)
plt.show()