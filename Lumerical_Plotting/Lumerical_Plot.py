import os
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/New/thickness_phase_tests/R/optbuffer0.32_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR, refl = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=4,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/New/Optimised_Grating/TM_S_Param_S22_Gn_Angle_P450_FF0.8_T100.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamP, phase = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=4,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/New/Ag_mirror_R_data.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamAg, reflAg = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=1,
#     unpack=True)

# lamAu_nm = lamAu * 1E9

# reflAu_percent = reflAu * 100
# reflAl_percent = reflAl * 100
# reflAg_percent = reflAg * 100

lam1 = lamR*1E9
refl1 = refl*100

# phase1 = np.array(phase)
phase2 = phase / np.pi
phase3 = phase2 - min(phase2)

fig, ax = plt.subplots(figsize=[10,7])
l1, = ax.plot(lam1, refl1, lw=2, color='k', label='Reflection')
# ax.plot(lamAu_nm, reflAu_percent, lw=3, color='k', label='Au')
# ax.plot(lamAl, reflAl_percent, lw=3, color='m', label='Al')
# ax.plot(lamAg, reflAg_percent, lw=3, color='c', label='Ag')
# plt.axvline(x=668, color='r', lw=1)

# plt.ylim([0, 1])
ax2 = ax.twinx()
# l2, = ax2.plot(lamP, phase3, lw=2, color='c', label='Phase')
ax.set_xlabel('Wavelength [nm]', fontsize=21, fontweight='bold')
ax.set_ylabel('Reflection [%]', fontsize=22, fontweight='bold', color='k')
ax2.set_ylabel('Phase [π rad]', fontsize=22, fontweight='bold', color='c')
# plt.legend((l1, l2), (l1.get_label(), l2.get_label()), loc='center right', prop={'size': 18})
# plt.legend(frameon=True, loc='lower right', prop={'size': 18})
plt.xlim([600, 800])
# plt.ylim([0, 100])
# plt.axis([None, None, 0, 1])
ax.tick_params(axis='both', labelsize=20)
ax2.tick_params(axis='both', labelsize=18)
plt.tight_layout()
plt.show()