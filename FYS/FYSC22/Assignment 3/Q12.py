from uncertainties import ufloat
import numpy as np

Avagadro = 6.022e23
d = ufloat(12.0,0.1) /1000 *100
r = ufloat(5.00,0.01)
A = r**2*np.pi
m113 = 112.900
m115 = 114.903
N113 = Avagadro * d * A / m113
N115 = Avagadro * d * A / m115

Z = 4.08e6 / A
