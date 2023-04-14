deltaE = [1.987,1.657,1.326,0.976,5.351]


M = 52163.642
Iav = [4*1**2/deltaE for deltaE in deltaE]
Ilst = [I*M for I in Iav]

a = 1.5
b =1
I = 0.2*M*(a**2 + b**2)

