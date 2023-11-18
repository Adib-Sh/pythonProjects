import numpy as np

#constants

m_n = 1.00866491595      
m_Be = 10.01294      
m_alpha = 4.002603
m_Li = 7.01601  
m_H = 1.007825031898
m_He = 3.0160293
m_3H = 3.01604928
A =  931.5 
Ex_Li = 0.478




Q1 = (m_He + m_n - m_3H - m_H)* 931.5 
KE1 = (  m_3H / (m_H + m_3H)) * Q1
print(r'Q1 =' + str(Q1))
print(r'KE1 =' + str(KE1))
Q2 = (m_Be + m_n - m_Li - m_alpha) * 931.5 
KE2 =(  m_Li / (m_alpha + m_Li)) * Q2
print(r'Q2 =' + str(Q2))
print(r'KE2 =' + str(KE2))

def Q (m1,m2,m3,m4,Ex):
    return (m1 + m2 - m3 - m4)*A - Ex

def K (m1,m2,m3,m4,Ex):
    return m4* Q (m1,m2,m3,m4,Ex)/ (m3 + m4) 

print(Q(m_He, m_n, m_3H, m_H,0))
print(K(m_He, m_n, m_3H, m_H,0))
print(K(m_He, m_n, m_H, m_3H,0))

print(Q(m_Be, m_n, m_Li, m_alpha,0))
print(K(m_Be, m_n, m_alpha, m_Li,0))
print(K(m_Be, m_n, m_Li, m_alpha,0))


print(Q(m_Be, m_n, m_Li, m_alpha,Ex_Li))
print(K(m_Be, m_n, m_alpha, m_Li,Ex_Li))
print(K(m_Be, m_n, m_Li, m_alpha,Ex_Li))