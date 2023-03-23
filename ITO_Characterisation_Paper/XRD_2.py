import numpy as np
import matplotlib.pyplot as plt
import os
root = os.getcwd()

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

datafilename = '/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/XRD/XRD_AE2.csv'
datafilepath = os.path.join(
    root,
    datafilename)
angle_AE2, data_AE2 = np.genfromtxt(
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
    skip_header=0,
    unpack=True)

fig, ax = plt.subplots(figsize=[12,6])
AI2_xtend = data_AI2 + 0
AC2_xtend = data_AC2 + 250
AE2_xtend = data_AE2 + 450

ax.set_xlim(25, 54)
# ax.set_ylim(-10, 550)

ax.plot(angle_AI2,AI2_xtend, label='0% O$_2$', lw=3, color='darkviolet')
ax.plot(angle_AC2,AC2_xtend, label='5% O$_2$', lw=3, color='crimson')
ax.plot(angle_AE2,AE2_xtend, label='20% O$_2$', lw=3, color='k')

# ax.text(0.63, 0.9,'0% Oxygen During Deposition', ha='center', va='center', fontsize=15, fontweight='bold', color='k', transform=ax.transAxes)

ax.text(0.25, 0.3,'(222)', ha='center', va='center', fontsize=22, color='k', transform=ax.transAxes)
ax.text(0.37, 0.16,'(004)', ha='center', va='center', fontsize=22, color='k', transform=ax.transAxes)
ax.text(0.9, 0.19,'(440)', ha='center', va='center', fontsize=22, color='k', transform=ax.transAxes)

# ax.text(0.25, 0.1,'1260.9 S/cm', ha='center', va='center', fontsize=18, fontweight='bold', color='darkviolet', transform=ax.transAxes)
# ax.text(0.25, 0.6,'20.6 S/cm', ha='center', va='center', fontsize=18, fontweight='bold', color='crimson', transform=ax.transAxes)
# ax.text(0.25, 0.8,' S/cm', ha='center', va='center', fontsize=18, fontweight='bold', color='crimson', transform=ax.transAxes)

ax.set_yticklabels([])
ax.set_xlabel('Diffraction Angle (2Θ)', fontsize=28, fontweight='bold', color='k')
ax.set_ylabel('Intensity (a.u.)', fontsize=28, fontweight='bold', color='k')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], frameon=True, loc='upper right', ncol=3, prop={'size': 22})
ax.tick_params(axis='both', labelsize=25)

plt.tight_layout()

##########################################################################################

# fig, ax = plt.subplots(figsize=[12,5])
# # AC1_xtend = data_AC1 
# AC2_xtend = data_AC2 + 200

# ax.plot(angle_AC2,AC2_xtend, label='Annealed', color='crimson')
# # ax.plot(angle_AC1,AC1_xtend, label='Unannealed', color='mediumblue')

# ax.set_xlim(15, 60)
# ax.set_ylim(-10, 470)

# ax.text(0.63, 0.9,'5% Oxygen During Deposition', ha='center', va='center', fontsize=15, fontweight='bold', color='k', transform=ax.transAxes)

# ax.text(0.385, 0.8,'(222)', ha='center', va='center', fontsize=14, color='k', transform=ax.transAxes)
# ax.text(0.455, 0.60,'(004)', ha='center', va='center', fontsize=14, color='k', transform=ax.transAxes)
# ax.text(0.805, 0.62,'(440)', ha='center', va='center', fontsize=14, color='k', transform=ax.transAxes)

# ax.set_yticklabels([])
# ax.set_xlabel('Diffraction Angle (2Θ)', fontsize=22, fontweight='bold', color='k')
# ax.set_ylabel('Intensity (a.u.)', fontsize=22, fontweight='bold', color='k')
# ax.legend(frameon=True, loc=0, prop={'size': 14})
# ax.tick_params(axis='both', labelsize=18)

# ax.text(0.1, 0.6,'20.6 S/cm', ha='center', va='center', fontsize=18, fontweight='bold', color='crimson', transform=ax.transAxes)
# ax.text(0.1, 0.1,'13.5 S/cm', ha='center', va='center', fontsize=18, fontweight='bold', color='mediumblue', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('/Users/samblair/Desktop/300_dpi/Fig3a_XRD.png')
# plt.show()