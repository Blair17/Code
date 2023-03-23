import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import polynomial as P
import pandas as pd
from scipy.stats import sem

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
    
TE = np.array([42.4,37.9,33.2,21.8])
lamTE_nm = np.array([590,653,746,839])
lamTE = np.array([a*0.001 for a in lamTE_nm])
p = [35,400,475,550]
TM = np.array([21.0,15.0,13.9,10.4])
lamTM_nm = np.array([583,637,734,839])
lamTM = np.array([a*0.001 for a in lamTM_nm])

TE_err = 1
lamTE_err = 0.5 * 0.001
TM_err = 1
lamTM_err = 0.5 * 0.001

a, b = np.polyfit(lamTE, TE, 1)
a1, b1 = np.polyfit(lamTM, TM, 1)

######################################################################
fig, ax = plt.subplots(figsize=(10,7))

ax.scatter(lamTE, TE, s=200, color='k')
ax.plot(lamTE, a*lamTE+b,color='k', label='TE', lw=3)
ax.scatter(lamTM, TM, marker='^', s=200, color='r')
ax.plot(lamTM, a1*lamTM+b1, color='r', label='TM', lw=3)
plt.errorbar(lamTE, TE, yerr=TE_err, xerr=lamTE_err, 
             fmt='None', ecolor='k', capsize=3)
plt.errorbar(lamTM, TM, yerr=TM_err, xerr=lamTM_err, 
             fmt='None', ecolor='r', capsize=3)

ax.set_xlabel('Wavelength (μm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Relative Reflectance (%)', fontsize=28, fontweight='bold')
plt.ylim([0,50])
ax.tick_params(axis='both', labelsize=25)
ax.legend(frameon=True, loc='upper right', prop={'size': 22})
plt.tight_layout()
plt.grid()
plt.savefig('/Users/samblair/Desktop/300_dpi/Fig1c_Relative_Amplitudes.png')
# plt.show()