import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, peak_prominences, peak_widths
from scipy.optimize import curve_fit


#Data--------------------------------------------------------------------------
df = pd.read_csv('sample2.txt', sep="\t", header=None)
df.columns = ["deg", "int"]   
df = df[(df.deg > 15)]
peaks, _ = find_peaks(df.int, height=[4,max(df.int)])

X = np.array(df.deg)
Y =np.array(df.int)


#Plot--------------------------------------------------------------------------
plt.figure()
plt.plot(X, Y)
plt.xlabel('2$\\theta $ (deg)')
plt.ylabel("Intensity")
plt.plot(X[peaks], Y[peaks], 'gx', markersize=3)
#plt.title('Sample 1')


#Lattice spacing and constant--------------------------------------------------
wavelength = 0.7107  #In Angstrom
n = 1
degpeaks = X[peaks]
# For sample 2: two extra peaks at [28.91242, 35.46857]

'''
#For sample 1
degpeaks1 = []
for i in range(0,len(degpeaks)):
    if i != 2 and i != 3:
        degpeaks1.append(degpeaks[i])
'''

degpeaks1 = [20.35745, 28.91242, 35.46857] #For sample 2

bcc_indices = [[1,1,0], [2,0,0], [2,1,1], [2,2,0], [1,3,0] ]
fcc_indices = [[1,1,1], [2,0,0], [2,2,0], [1,1,3], [2,2,2] ]

theta_rad = [np.deg2rad(theta_deg/2) for theta_deg in degpeaks1] #Dividing by 2 because we have 2\theta


d = n * wavelength / (2 * np.sin(theta_rad))
a = []
i = 0
for ind in bcc_indices[0:len(degpeaks1)]:
    h,k,l = ind[0], ind[1], ind[2]
    a_entries = d[i] * np.sqrt(h**2 + k**2 + l**2)
    a.append(a_entries)
    i += 1

print(a)


#Peak intensities--------------------------------------------------------------
peak_intensities = [Y[(X >= peak - 0.1) & (X <= peak + 0.1)].sum() for peak in X[peaks]]


#Crystallites  size
FWHM, half_heights, leftvals, rightvals = peak_widths(Y, peaks, rel_height=0.5)

def remap(num, oldmin, oldmax, newmin, newmax):
    oldrange = oldmax - oldmin
    newrange = newmax - newmin
    return (num - oldmin)*newrange/oldrange + newmin

def remap_numpy(num, oldmin, oldmax, newmin, newmax):
    return np.interp(num, [oldmin, oldmax], [newmin, newmax])

leftvals = remap(leftvals, 0, len(X), X[0], X[-1])
rightvals = remap(rightvals, 0, len(X), X[0], X[-1])

plt.hlines(half_heights, leftvals, rightvals, color="red")
beta_rad = np.deg2rad(FWHM[0]/2)
k = 0.94

t = k * wavelength / (beta_rad * np.cos(theta_rad))


#Structure factor--------------------------------------------------------------
