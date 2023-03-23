import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def last_9chars(x):
    return(x[-9:])

root = os.getcwd()
files = glob.glob('/Volumes/Sam/Lumerical/New/thickness_phase_tests/Phase/*.txt')
sorted_array = sorted(files, key = last_9chars)  
print(sorted_array)

l_array = []
r_array = []

for file in sorted_array:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    l, r = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=3,
        unpack=True)
    l_array.append(l)
    r_array.append(r)   

p = []
for k in l_array:
    p.append(k*1E6)

phase_pi = []
for q in r_array:
    phase_pi.append(q / np.pi)

labels = ['0.32 um', '1.05 um', '1.5 um', '2.0 um', '2.5 um', '3.0 um', '3.5 um', '4.0 um', '4.5 um', '5.0 um']

fig, ax = plt.subplots(figsize=[10,7])
for index, l in enumerate(p):
    ax.plot(l,phase_pi[index], label=[x for x in labels][index])
    ax.set_xlabel('Wavelength [μm]', fontsize=16, fontweight='bold')
    ax.set_ylabel('Phase [π rad]', fontsize=16, fontweight='bold')
    # ax.set_ylim([0,1.0])
    ax.set_xlim([0.645,0.685])
    ax.tick_params(axis='both', labelsize=14)
    ax.legend(frameon=True, loc=0, prop={'size': 14})
    plt.title('Phase Variation with Buffer Thickness', fontsize=18, fontweight='bold')
    plt.savefig('/Volumes/Sam/Lumerical/New/thickness_phase_tests/Phase/Phase_Variation.png')
    plt.axvline(x=0.665, color='k', lw=2, linestyle='--')
# ax.plot(p[0],r_array[0], label=[x for x in labels][0])
# ax.plot(p[1],r_array[1], label=[x for x in labels][1])
# ax.plot(p[2],r_array[2], label=[x for x in labels][2])
# ax.plot(p[-1],r_array[-1], label=[x for x in labels][-1])
# ax.legend(frameon=True, loc=0, prop={'size': 14})

plt.tight_layout()
plt.show()