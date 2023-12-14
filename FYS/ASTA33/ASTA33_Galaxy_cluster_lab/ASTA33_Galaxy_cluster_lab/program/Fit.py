
import numpy as np
import matplotlib.pyplot as plt
### Read in data.
<<<<<<< HEAD
=======
#path = '/Users/adib/Git/pythonProjects/FYS/ASTA33/ASTA33_Galaxy_cluster_lab/ASTA33_Galaxy_cluster_lab/program'
>>>>>>> 2488086473f558d9464da1fa0fdb780b0669e26b
datadir = './yellow-1.dat'
data = np.loadtxt(datadir)
mag = data[:,0] # Magnitude.
emag = data[:,1] # Error in magnitude.
col = data[:,2] # Colour.
ecol = data[:,3] # Error in colour.
### Mask data.
mask = (mag < 24) # Remove galaxies dimmer than 24 magnitude.
mag = mag[mask]
emag = emag[mask]
col = col[mask]
ecol = ecol[mask]
### Line fit by least square method.
(p1, p2) = np.polyfit(mag, col, deg=1, full=False) # polynomial coefficients.
### Simple plot.
# Set up figure.
plt.style.use('classic')
fig = plt.figure(figsize=(8,6))
plt.minorticks_on()
plt.gca().tick_params(axis='both', which='both', direction='in', labelsize=14)
plt.ylabel(r'${\rm Colour,}\ (V-I)$', fontsize=18)
plt.xlabel(r'${\rm Magnitude,}\ I$', fontsize=18)
plt.ylim(0,4)
plt.xlim(18,26)
# Plot data-points with errorbars.
plt.errorbar(mag,col,xerr=emag,yerr=ecol,color='r', fmt=' ',
ecolor='k', elinewidth=1, capsize=2, label='shape-data')
# Plot fitted line.
x = np.linspace(min(mag), max(mag)) # To plot fit.
<<<<<<< HEAD
plt.plot(x, p1*x+p2, '-r', lw=2, alpha=0.7)
plt.title('Plot of all objects selected')
=======
plt.plot(x, p1*x+p2, '-r', lw=2, alpha=0.7, label= 'fit')
plt.title('Plot Elliptical galaxies with fitted line')
plt.legend()
>>>>>>> 2488086473f558d9464da1fa0fdb780b0669e26b
# Finalise plot.
plt.tight_layout()
plt.show()
print(len(mag))