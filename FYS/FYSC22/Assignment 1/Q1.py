import numpy as np
import matplotlib.pyplot as plt



# constants in MeV
aa = 23
ac = 0.72
av = 15.67
a_s = 17.23

# Choosing A as the most abandant
A = 56
Zbound = int(A)
# even Z between 2 and A
Z = np.linspace(2, A, int(Zbound/2))
N = [A-Z[i] for i in range(0,len(Z))]


# binding energy function
def B(A,Z):
    B = av*A - a_s*A**(2/3) - (ac*(Z**2/A**(1/3))) - (aa*(((A-Z)-Z)**2/A))
    return B

# list of Be for different Z
BE = [B(A,Z[i]) for i in range(0,int(Zbound/2))]
# finding the maximum Be
BmaxZ = [BE[i]/(A*931.493) for i in range(0,int(Zbound/2))]


plt.figure()
plt.plot(N,BmaxZ)
plt.xlabel('Neutron number N')
plt.ylabel('Binding energy per nucler mass (MeV)')
print(f' The most stable even-even iron isotope is Fe-{A} with Z = {Z[BmaxZ.index(max(BmaxZ))]}')

# seperation energy function
def Sp(A,Z):
    return B(A,Z) - B(A-1,Z-1) 
def Sn(A,Z):
    return B(A,Z) - B(A-1,Z)


Z = 26
A = range(Z, 120, 2)
Sp_values = [Sp(a,Z) for a in A]
Sn_values = [Sn(a,Z) for a in A]

# finding the minimum of Sp, Sn
y = [min(Sp_values, key=lambda l: abs(0-l)), min(Sn_values, key=lambda l: abs(0-l))]
print(f"Proton drip line: {A[Sp_values.index(y[0])] - 26}")
print(f"Neutron drip line: {A[Sn_values.index(y[1])] - 26}")

plt.figure()
plt.plot(A,Sp_values, label = r'$S_p$')
plt.plot(A,Sn_values, label = r'$S_n$')
plt.xlabel('Nuclear mass A')
plt.ylabel('Seperation energy (MeV)')
plt.legend()
Spmin = min(Sp_values, key=abs)
Snmin = min(Sn_values, key=abs)

