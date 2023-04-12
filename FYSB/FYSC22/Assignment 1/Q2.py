import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0 , e, pi
# constants
epsilon = 8.854
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

# binding energy function
def Eb(EZ, Z):
    EbZ = abs(Z - EZ*1e-6 )
    MeV = EbZ * 931.493
    return MeV

# mass excess
B11 = 9305
C11 = 11434
ZB = 5
ZC = 6

N15 = 109
O15 = 3065
ZN = 7
ZO = 8

Ne21 = -6153
Na21 = -2345
ZNe = 10
ZNa = 11

Mg25 = -14163
Al25 = -9571
ZMg = 12
ZAl = 13
#
Si29 = -23505
P29 = -18199
ZSi = 14
ZP = 15
#
S33 = -28542
Cl33 = -22548
ZS = 16
ZCl = 17
#
Ar37 = -33224
K37 = -26623
ZAr = 18
ZK = 19
#
Sc43 = -38849
Ti43 = -31476
ZSc = 21
ZTi = 22

# list of binding energies    
BElst = [C11-B11, O15-N15, Na21-Ne21, Al25-Mg25, P29-Si29,
         Cl33-S33, K37-Ar37, Ti43-Sc43]    
BElst =[i*931.493e-6 for i in BElst]

# value of constant k
k = [0.6*1.44*A**(2/3) for A in A]

# fitting the line
m, a = np.polyfit(k,BElst, 1)

# finding r0
r0 = 1/m*10**(-12) #e-6 micrometer*e-6 MeV
print(r0)

X = [A**(2/3) for A in A]
plt.scatter(X,BElst)
plt.xlabel(r'$A^{2/3}$')
plt.ylabel(r'$\Delta E_c (MeV)$')
