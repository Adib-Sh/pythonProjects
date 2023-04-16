import numpy as np
import scipy.constants as const



# constants in MeV
c = const.c
aa = 23
ac = 0.72
av = 15.67
a_s = 17.23
a_p = 11.5
#a = 1.44e-15
a = 1/137

# masses in MeV
He = 3726.42/c**2
mp = const.physical_constants['proton mass energy equivalent in MeV'][0]/c**2
mn = const.physical_constants['neutron mass energy equivalent in MeV'][0]/c**2
m_h = 938.783/c**2
m_n = 939.565/c**2
hbar = const.physical_constants['reduced Planck constant in eV s'][0]*1e-6
m = const.physical_constants['alpha particle mass energy equivalent in MeV'][0]/c**2

# binding energy function
def B(A,Z):
    # Calculate mass using Weizsäcker formula
    delta = 0
    if A % 2 == 1:
        delta = a_p / A**(1/2)
    elif Z % 2 == 0 and A % 2 == 0:
        delta = -a_p / A**(1/2)
    B = av*A - a_s*A**(2/3) - (ac*(Z*(Z-1)/A**(1/3))) - (aa*(((A-Z)-Z)**2/A)) + (delta /np.sqrt(A))
    return B
print('B is:'+str(B(296,120)))

# mass function
def M(A,Z):
    M = Z*m_h + (A-Z)*mn - B(A,Z)/c**2
    return M
print('M is:'+str(M(296,120)))

# Q_alpha function
def Q(A,Z):
    Q = (M(A,Z) - M(A-4,Z-2) - m)*c**2
    return Q
print('Q is:'+str(Q(296,120)))

def G(A,Z):
    #G = np.sqrt((2 * m) / hbar) * (1 / (np.sqrt(Q(A,Z)))) * a * Z * (Z-2) * (np.arccos(np.sqrt(Q(A,Z)/B(A,Z)))-np.sqrt((Q(A,Z)/B(A,Z))*(1-(Q(A,Z)/B(A,Z)))))
    G = 2 * a * (Z-2) * np.sqrt((2*m*const.c**2)/Q(A,Z))*(np.arccos(np.sqrt(Q(A,Z)/B(A,Z))) - np.sqrt((Q(A,Z)/B(A,Z))*(1-(Q(A,Z)/B(A,Z)))))
    return G
print('G is:'+str(G(296,120)))

def T(A,Z):
    P = np.exp(-2*G(A,Z))
    T = hbar * np.log(2)/P
    return T
print('T is:'+str(T(296,120)))