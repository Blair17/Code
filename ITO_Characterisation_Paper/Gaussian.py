from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
root = os.getcwd()

def gauss(x, a, x0, sigma, offset):
    return a * np.exp(-( (x - x0)**2 / (2 * sigma**2) ) ) + offset

def FWHM(stdev):
    return 2*np.sqrt(2*np.log(2))*stdev

# AC2 = Low Conductivity Annealed
# AI2 = High Conductivity Annealed

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

datafilename = '/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/XRD/AC2_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AC2, data_AC2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

datafilename = '/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/XRD/AI2_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AI2, data_AI2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

datafilename = '/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/XRD/XRD_AE2.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AE2, data_AE2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

labels = [30.2, 30.4, 30.6, 30.8, 31.0, 31.2]

# AE2 (222)
# a = 1020
# b = 1120

# AI2 and AC2 (222)
a = 520
b = 620

# AE2 (440)
# a = 3050
# b = 3200

# AI2 and AC2 (440)
# a = 2550
# b = 2700

x = np.array(angle_AI2[a:b])
y = np.array(data_AI2[a:b])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
# ax.plot(x, y, c='k', label='Function')
ax.scatter(x, y, color='darkviolet', s=150, label='0% O$_2$ Data')
y_max = np.argmax(y)
x_max = x[y_max]
y_amp = max(y) - min(y)
off = 1
p0 = [y_amp, x_max, 0.1, off]
popt, pcov = curve_fit(gauss, x, y, p0)

ym = gauss(x, popt[0], popt[1], popt[2], popt[3])
ax.plot(x, ym, c='k', lw=3.5, label='0% O$_2$ Fit')
ax.legend()
FWHM_1 = FWHM(popt[2])
FWHM_errors = FWHM(pcov[2])
plt.axvspan(popt[1]-FWHM_1/2, popt[1]+FWHM_1/2, facecolor='turquoise', alpha=0.5)
print(FWHM_1)
print(f'FWHM errors are {FWHM_errors}')
# ax.set_xticklabels(labels)
ax.set_xlabel('Diffraction Angle (2Θ)', fontsize=38, fontweight='bold', color='k')
ax.set_ylabel('Intensity (a.u.)', fontsize=38, fontweight='bold', color='k')
ax.legend(frameon=True, loc=0, prop={'size': 24})
ax.tick_params(axis='both', labelsize=32)

ax.text(0.25, 0.9,'(222)', ha='center', va='center', fontsize=32, color='k', transform=ax.transAxes)

plt.ylim([0, 270])
plt.tight_layout()
plt.savefig('/Users/samblair/Desktop/Fig3d_0_FWHM.png')
# plt.show()
