import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, peak_prominences, peak_widths
from scipy.optimize import curve_fit


#Data--------------------------------------------------------------------------
df = pd.read_csv('sample1.txt', sep="\t", header=None)
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
plt.title('Sample 1')

#Lattice spacing and constant--------------------------------------------------
wavelength = 0.7107  
n = 1
degpeaks = X[peaks]
h = 1  
k = 1 
l = 0 
theta_rad = [np.deg2rad(theta_deg) for theta_deg in degpeaks]

d = n * wavelength / (2 * np.sin(theta_rad))
a = d * np.sqrt(h**2 + k**2 + l**2)


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

