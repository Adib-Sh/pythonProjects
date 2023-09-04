import numpy as np
import scipy.constants as const



# constants in MeV
c = const.c
aa = 23.2
ac = 0.71
av = 15.9
a_s = 18.4
a_p = 11.5
a = 1/137

# masses in MeV
He = 3728.40/c**2
m_alpha = 3727.379/c**2
mp = const.physical_constants['proton mass energy equivalent in MeV'][0]/c**2
mn = const.physical_constants['neutron mass energy equivalent in MeV'][0]/c**2
hbar = const.physical_constants['reduced Planck constant in eV s'][0]*1e-6
hbarc = const.physical_constants['reduced Planck constant times c in MeV fm'][0]
m_h = 938.783/c**2
m_n = 939.565/c**2

# binding energy function
def B(A,Z):
    # Calculate mass using Weizsäcker formula
    #delta = 0
    #if A % 2 == 1:
    #    delta = a_p / A**(1/2)
    #elif Z % 2 == 0 and A % 2 == 0:
    #    delta = -a_p / A**(1/2)
    B = av*A - a_s*A**(2/3) - (ac*(Z*(Z-1)/A**(1/3))) - (aa*((((A-2*Z)**2)/A))) #+ (delta /np.sqrt(A))
    return B
print('B is:'+str(B(296,120)))

# mass function
def M(A,Z):
    M = Z*m_h + (A-Z)*mn - B(A,Z)/c**2
    return M


print('M is:'+str(M(296,120)))

# Q_alpha function
def Q(A,Z):
    Q = (M(A,Z) - M(A-4,Z-2) - He)*c**2
    return Q

print('Q is:'+str(Q(296,120)))


#==============================================================================
#Part b
def G(A,Z):

    x = Q(A,Z)/B(A,Z)
    G =  2* a * (Z-2) * np.sqrt((2*m_alpha*c**2)/Q(A,Z))*(np.arccos(np.sqrt(x)) - np.sqrt(x-x**2))
    #G = np.sqrt((2 * m_alpha*c**2) / hbarc**2) * (1 / (np.sqrt(Q(A,Z)))) * 1.44 * 2 * (Z-2) * (np.arccos(np.sqrt(x)) - np.sqrt(x*(1-x)))
    return G

print('G is:'+str(G(296,120)))


def T(A,Z):
    f = Q(A,Z)/hbar
    P = np.exp(-2*G(A,Z))
    T = np.log(2)/((f*P))
    return T
print('T is:'+str(T(296,120)) + ' seconds')


#==============================================================================
#Part c
print('For 236U, Q is:'+str(Q(236,92)) + ' MeV')
print('For 236U, T is:'+str(T(236,92)) + ' seconds')
print('For 236U, T is:'+str(T(236,92)/(3600*24*365)) + ' years')

print('For 288Fl, Q is:'+str(Q(288,114)) + ' MeV')
print('For 288Fl, T is:'+str(T(288,114)) + ' seconds')

#==============================================================================
#Part d
print('For 296(120), Q is:'+str(Q(296,120)) + ' MeV')
print('For 296(120), T is:'+str(T(296,120)) + ' seconds')

print('For 292Og, Q is:'+str(Q(292,118)) + ' MeV')
print('For 292Og, T is:'+str(T(292,118)) + ' seconds')

print('For 288Lv, Q is:'+str(Q(288,116)) + ' MeV')
print('For 288Lv, T is:'+str(T(288,116)) + ' seconds')
print('For 288Lv, T is:'+str(T(288,116)/(3600*24*365)) + ' years')
