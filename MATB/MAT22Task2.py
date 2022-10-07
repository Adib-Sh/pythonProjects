import numpy as np
from numpy import linalg as LA

import matplotlib.pyplot as plt


m = np.matrix([[1, 3, 2], [-3, 4, 3], [2, 3, 1]])
matrix = m
k = 10
print(m)
# def calc(matrix,k):

evalue, evector = LA.eig(matrix)

basis = np.squeeze(np.asarray(evector))

u0 = np.array([8, 3, 12])

c = np.linalg.solve(basis, u0)


uk = []
for j in range(1, k+1):
    coliter = []
    for i in range(0, len(basis)):
        n = basis[:, i] * c[i] * evalue[i]**j
        coliter.append(n)
    uk.append(coliter)
uk = np.array(uk)
#    return uk


#Z = calc(m,20)
# print(Z)
'''
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = cbasis[2]
xline = cbasis[1]
yline = cbasis[0]
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = cbasis[2]
xdata = cbasis[1]
ydata = cbasis[0]
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
'''
