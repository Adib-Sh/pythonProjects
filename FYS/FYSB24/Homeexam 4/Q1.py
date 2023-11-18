
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
from peakdetect import peakdetect

'''
data1 = pd.read_csv('first.txt', sep=" ", header=None)
data2 = pd.read_csv('second.txt', sep=" ", header=None)


x1 = np.linspace(0,1,len(data1))
x2 = np.linspace(0,1,len(data2))
plt.plot(x1,data1[0])
plt.plot(x2,data2[0])

'''



# Define the wavenumber calibration function
def calibrate_wavenumber(pixel, slope, intercept):
    return slope * pixel + intercept
ref_wavenumbers = np.array([2332, 2304, 2275, 2247])


# Load the spectra data from the text files
spectrum1 = np.loadtxt('first.txt')
spectrum2 = np.loadtxt('second.txt')
# Generate pixel arrays for the spectra
pixels1 = np.arange(len(spectrum1))
pixels2 = np.arange(len(spectrum2))
calibration = np.polyfit(ref_wavenumbers, pixels1, 1)

# Calibrate the wavenumbers using first-order polynomial functions
slope1, intercept1 = np.polyfit(pixels1, np.linspace(2200,2350,len(pixels1)), 1)
slope2, intercept2 = np.polyfit(pixels2, np.linspace(2200,2350,len(pixels2)), 1)

wavenumbers1 = calibrate_wavenumber(pixels1, *calibration)
#wavenumbers1 = calibrate_wavenumber(pixels1, slope1, intercept1)
wavenumbers2 = calibrate_wavenumber(pixels2, slope2, intercept2)

# Normalize the spectra to their highest peak
spectrum1_norm = spectrum1 / np.max(spectrum1)
spectrum2_norm = spectrum2 / np.max(spectrum2)
peaks1, _ = find_peaks(spectrum1_norm) 
peaks1 = peaks1[1:(len(peaks1)-1)]
peaks2, _ = find_peaks(spectrum2_norm)
peaks2 = peaks2[np.argmax(spectrum2_norm[peaks2])]

# Plot the normalized spectra on the same figure
plt.plot(wavenumbers1, spectrum1_norm, label='Spectrum 1')
plt.plot(wavenumbers1[peaks1], spectrum1_norm[peaks1], "xr")
plt.plot(wavenumbers2, spectrum2_norm, label='Spectrum 2')
plt.plot(wavenumbers2[peaks2], spectrum2_norm[peaks2], "xr")
plt.xlabel('Wavenumber (cm$^{-1}$)')
plt.ylabel('Normalized Intensity')
plt.legend()
plt.show()
