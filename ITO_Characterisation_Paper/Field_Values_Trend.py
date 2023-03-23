import numpy as np
import matplotlib.pyplot as plt

lamTE = np.array([591.66, 650.55, 749.44, 849.44])
field_TE = np.array([2.20E+05, 2.53E+05, 2.46E+05, 2.47E+05])

lamTM = np.array([582.77, 637.77, 732.78, 834.44])
field_TM = np.array([3.94E+04, 4.04E+04, 4.43E+04, 4.60E+04])

a, b = np.polyfit(lamTE, field_TE, 1)
a1, b1 = np.polyfit(lamTM, field_TM, 1)

fig, ax = plt.subplots(figsize=[10,7])
ax.scatter(lamTE, field_TE, marker='s', s=50, color='k', label='TE')
ax.plot(lamTE, a*lamTE+b,color='k', label='Fit')

ax.scatter(lamTM, field_TM, marker='s', s=50, color='r', label='TM')
ax.plot(lamTM, a1*lamTM+b1, color='r', label='Fit')

ax.set_xlabel('Wavelength (nm)', fontsize=21, fontweight='bold')
ax.set_ylabel('Absolute Field Intensity (V/m)', fontsize=21, fontweight='bold')
ax.tick_params(axis='both', labelsize=19)
ax.legend(frameon=True, loc='center right', prop={'size': 14})
plt.ylim([0, 300000])

plt.tight_layout()
plt.grid()
plt.show()