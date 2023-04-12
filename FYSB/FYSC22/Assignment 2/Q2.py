import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const



# constants in MeV
aa = 23
ac = 0.72
av = 15.67
a_s = 17.23
a_p = 12
He = 3728.40
mp = const.physical_constants['proton mass energy equivalent in MeV'][0]
mn = const.physical_constants['neutron mass energy equivalent in MeV'][0]
# binding energy function
def B(A,Z):
    # Calculate mass using Weizsäcker formula
    delta = 0
    if A % 2 == 1:
        delta = a_p / A**(1/2)
    elif Z % 2 == 0 and A % 2 == 0:
        delta = -a_p / A**(1/2)
    B = av*A - a_s*A**(2/3) - (ac*(Z*(Z-1)/A**(1/3))) - (aa*(((A-Z)-Z)**2/A))+ (delta * A)
    return B

# mass function
def M(A,Z):
    M = Z*mp + (A-Z)*mn - B(A,Z)/const.c
    return M

def Q(A,Z):
    Q = M(A,Z) - M(A-4,Z-2) - He
    return Q

print(Q(296,120))

def T(A,Z):
    hbar = const.physical_constants['Planck constant over 2 pi times c in MeV fm']
    R = 1.2*A**(1/3)
    m = const.physical_constants['alpha particle mass energy equivalent in MeV']
    G = np.sqrt(abs(2*m[0]*R**2*(Q(A,Z)-B(A,Z))))/hbar[0]
    P = np.exp(-2*G)
    T = hbar[0] * np.log(2)/P
    return T
print(T(296,120))