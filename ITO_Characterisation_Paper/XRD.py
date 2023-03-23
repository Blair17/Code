import numpy as np
import matplotlib.pyplot as plt
import os
root = os.getcwd()

datafilename = '/Users/samblair/Desktop/AC1_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AC1, data_AC1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

datafilename = '/Users/samblair/Desktop/AC2_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AC2, data_AC2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

datafilename = '/Users/samblair/Desktop/AI1_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AI1, data_AI1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

datafilename = '/Users/samblair/Desktop/AI2_2tw2_XRD.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AI2, data_AI2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

# fig, (ax1,ax2) = plt.subplots(2,1, figsize=[10,7])
fig, (ax1,ax2) = plt.subplots(2, 1, figsize=[10,7])
AI2_xtend = data_AI2 + 100
AC1_xtend = data_AC1 
AC2_xtend = data_AC2 + 200

ax1.set_xlim(10, 60)
# ax1.set_ylim(0, 200)
ax2.set_xlim(10, 60)
# ax2.set_ylim(0, 200)
ax1.plot(angle_AI1,data_AI1, label='Unannealed', color='k')
ax1.plot(angle_AI2,AI2_xtend, label='Annealed', color='darkviolet')
ax2.plot(angle_AC1,AC1_xtend, label='Unannealed', color='mediumblue')
ax2.plot(angle_AC2,AC2_xtend, label='Annealed', color='crimson')

ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax1.text(0.65, 0.9,'0% Oxygen During Deposition', ha='center', va='center', fontsize=10, fontweight='bold', color='k', transform=ax1.transAxes, bbox=dict(facecolor='none', edgecolor='red'))
ax2.text(0.65, 0.9,'11% Oxygen During Deposition', ha='center', va='center', fontsize=10, fontweight='bold', color='k', transform=ax2.transAxes, bbox=dict(facecolor='none', edgecolor='red'))

ax1.text(0.385, 0.9,'(222)', ha='center', va='center', fontsize=10, color='k', transform=ax1.transAxes)
ax1.text(0.51, 0.5,'(004)', ha='center', va='center', fontsize=10, color='k', transform=ax1.transAxes)
ax1.text(0.82, 0.54,'(440)', ha='center', va='center', fontsize=10, color='k', transform=ax1.transAxes)

ax2.text(0.385, 0.9,'(222)', ha='center', va='center', fontsize=10, color='k', transform=ax2.transAxes)
ax2.text(0.51, 0.65,'(004)', ha='center', va='center', fontsize=10, color='k', transform=ax2.transAxes)
ax2.text(0.82, 0.67,'(440)', ha='center', va='center', fontsize=10, color='k', transform=ax2.transAxes)

ax1.set_xlabel('Diffraction Angle (2Θ)', fontsize=14, fontweight='bold', color='k')
ax1.set_ylabel('Intensity (a.u.)', fontsize=14, fontweight='bold', color='k')
ax2.set_xlabel('Diffraction Angle (2Θ)', fontsize=14, fontweight='bold', color='k')
ax2.set_ylabel('Intensity (a.u.)', fontsize=14, fontweight='bold', color='k')

ax1.legend(frameon=True, loc=0, prop={'size': 12})
ax2.legend(frameon=True, loc=0, prop={'size': 12})

# plt.xlim([10,90])
# plt.ylim([0,250])

plt.tight_layout()
plt.show()