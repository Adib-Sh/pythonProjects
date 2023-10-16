import pandas as pd
import matplotlib.pyplot as plt
#import networkx as nx
#import seaborn as sns
import numpy as np
#from operator import itemgetter
#import powerlaw as pwl
from scipy.optimize import curve_fit
import powerlaw

df = pd.read_csv('exoplanet.eu_catalog.csv')

x = df.loc[:, 'mass']
y = df.loc[:, 'radius']
x1 = df[df.loc[:, 'mass']<0.2]
x2 = df[df.loc[:, 'mass']>=0.2]
#df.plot(x, y, kind='line', style='--ro', figsize=(10, 5))

def power(x, b, c):
    return b*x**c

popt1, pcov1 = curve_fit(power, x1['mass'], x1['radius'], maxfev = 2000)
popt2, pcov2 = curve_fit(power, x2['mass'], x2['radius'], maxfev = 2000)



fig, ax = plt.subplots()
ax.plot(x,y, ls='None', marker='.', ms=10)
#X = np.linspace(0, int(x.max()) , int(x.max()+10))
X1 = np.arange(x1['mass'].min(), x1['mass'].max()+1)
X2 = np.arange(x2['mass'].min(), x2['mass'].max()+1)
ax.plot(X1, power(X1, *popt1))
ax.plot(X2, power(X2, *popt2))
ax.set_xlabel('Planetary mass ($M_{Jup})$')
ax.set_ylabel('Planetary radius ($R_{Jup})$')
ax.set_yscale('log')
ax.set_xscale('log')
'''
plt.plot(x1['mass'], x1['radius'], marker='o', ls='', label='data')
plt.plot(x2['mass'], x2['radius'], marker='o', ls='', label='data')
fit1 = np.polyfit(x1['mass'], x1['radius'], deg=4)
fit2 = np.polyfit(x2['mass'], x2['radius'], deg=4)



X1 = np.arange(x1['mass'].min(), x1['mass'].max()+1)
X2 = np.arange(x2['mass'].min(), x2['mass'].max()+1)
# plot mapped fit onto X
plt.plot(X1, np.poly1d(fit1)(X1), label='fit')
plt.plot(X2, np.poly1d(fit2)(X2), label='fit')
plt.yscale('log')
plt.xscale('log')
'''