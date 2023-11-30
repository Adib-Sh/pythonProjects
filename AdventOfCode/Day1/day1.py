import numpy as np



filename = 'input.txt'
data = np.loadtxt(filename, delimiter='2', dtype=int)
print(data)


