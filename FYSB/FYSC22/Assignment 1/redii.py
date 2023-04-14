import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0
epsilon = epsilon_0
r0 = 1.25e-15
A = [11, 15, 21, 25, 29, 33, 37, 43]
Z = [round(a/2) for a in A]
e = 1.602e-19
aa = 23
ac = 0.72
av = 15.67
a_s = 17.23
mp = 938.272 #MeV
mn = 939.565 #MeV



k = [0.6*1.44*A**(2/3) for A in A]


m, a = np.polyfit(k,BElst, 1)
r0 = 1/m



def Be(A,Z):
    return av*A - a_s*A**(2/3) - ac*Z*(Z-1)/A**(1/3) - aa*((((A-Z)-Z)**2)/A)

def M(A,Z):
    return Z*mp + (A-Z)*mn - Be(A,Z)

def DeltaBe(A,Z):
    #return av*A - (a_s*A**(2/3)) - (ac*(Z**2/A**(1/3))) - (aa*((((A-Z)-Z)**2)/A))
    return abs(M(A,Z) - M(A,Z-1))
    #return (Z-(Z-1))*mp + ((A - Z)-Z)*mn + ac*(Z**2 - (Z - 1)**2)/A**(1/3)

Alst = [a**(2/3) for a in A]
BcLst = []
for i in range (0,len(A)):
    BcLst.append(DeltaBe(A[i],Z[i])+0.782455)

 #Fitted line
r0 = (0.8640/m)*10**(-11)
plt.scatter(A,BcLst)


#####################################

def Ec(A):
   return 0.6*(e**2/(4*np.pi*epsilon*r0))*A**(2/3)
Ec = [Ec(a) for a in A]