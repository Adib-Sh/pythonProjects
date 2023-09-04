import scipy.constants as const
import numpy as np


e = const.e
eps = 55.263
Md = 1.748
a = 0.314e-3
Ek = -Md * (1)/(4*eps*np.pi*a)
print(Ek)