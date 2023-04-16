import numpy as np
import scipy.constants as const



# constants in MeV
aa = 23
ac = 0.72
av = 15.67
a_s = 17.23
a_p = 12
He = 3728.
m_alpha = 3727
mp = const.physical_constants['proton mass energy equivalent in MeV'][0]
mn = const.physical_constants['neutron mass energy equivalent in MeV'][0]
m_h = 938.783
m_n = 939.565
a = 1/137
c = const.c

# mass function
def M(A,Z):
    N = A - Z
    B = av*A - a_s*A**(2/3) - (ac*Z**2/(A**(1/3))) - (aa*((N-Z)**2/A))
    M = (Z*m_h + (A-Z)*mn - B)
    return M


print('M is:'+str(M(296,120)))

# Q_alpha function
def Q(A,Z):
    Q = (M(A,Z) - M(A-4,Z-2) - He)
    return Q

print('Q is:'+str(Q(296,120)))


#==============================================================================
#Part b
def G(A,Z):
    N = A - Z
    B = av*A - a_s*A**(2/3) - (ac*Z**2/(A**(1/3))) - (aa*((N-Z)**2/A))
    x = Q(A,Z)/B
    G =  2 * a * (Z-2) * np.sqrt((2*m_alpha)/Q(A,Z))*np.arccos(np.sqrt(x)) - np.sqrt(x*(1-x)) 
    return G

print('G is:'+str(G(296,120)))


def T(A,Z):

    f = Q(A,Z)*1.6022e-13/const.hbar
    P = np.exp(-2*G(A,Z))
    T = np.log(2)/((f*P)*c**2)
    return T
print('T is:'+str(T(296,120)) + ' seconds')


#==============================================================================
#Part c
print('For 236U, Q is:'+str(Q(236,92)))
print('For 236U, T is:'+str(T(236,92)))
print('For 288Fl, Q is:'+str(Q(288,114)))
print('For 288Fl, T is:'+str(T(288,114)))