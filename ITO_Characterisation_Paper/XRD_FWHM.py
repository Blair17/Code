import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.optimize as opt

def gauss(x, p): # p[0]==mean, p[1]==stdev
    return 1.0/(p[1]*np.sqrt(2*np.pi))*np.exp(-(x-p[0])**2/(2*p[1]**2))

root = os.getcwd()
# AC2 = Low Conductivity Annealed
# AI2 = High Conductivity Annealed

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

sliced_AI2 = data_AI2[500:650]
sliced_angle_AI2 = angle_AI2[500:650]

xmin = np.min(sliced_angle_AI2)
xmax = np.max(sliced_angle_AI2)
print(xmin, xmax)

Y = gauss(sliced_angle_AI2, sliced_AI2)

## Fit Gaussian ##
p0 = [0,1] # Inital guess is a normal distribution
errfunc = lambda p, x, y: gauss(x, p) - y # Distance to the target function
p1, success = opt.leastsq(errfunc, p0[:], args=(sliced_angle_AI2, Y))

fit_mu, fit_stdev = p1

FWHM = 2*np.sqrt(2*np.log(2))*fit_stdev
print("FWHM", FWHM)

##########################################################################################

fig, ax = plt.subplots(figsize=[12,5])

ax.plot(sliced_angle_AI2, sliced_AI2, label='Data')
ax.plot(sliced_angle_AI2, gauss(sliced_angle_AI2,p1),lw=3,alpha=.5, color='r', label='Gaussian Fit')
ax.axvspan(fit_mu-FWHM/2, fit_mu+FWHM/2, facecolor='g', alpha=0.5)
# ax.plot(sliced_angle_AI2,sliced_AI2, label='AI2', color='darkviolet')

ax.set_yticklabels([])
ax.set_xlabel('Diffraction Angle (2Θ)', fontsize=22, fontweight='bold', color='k')
ax.set_ylabel('Intensity (a.u.)', fontsize=22, fontweight='bold', color='k')
ax.legend(frameon=True, loc=0, prop={'size': 14})
ax.tick_params(axis='both', labelsize=18)
plt.xlim([xmin, xmax])

plt.tight_layout()
plt.show()