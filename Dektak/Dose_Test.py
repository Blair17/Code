import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

datafile = '/Volumes/Sam/DekTak/DoseTest/4000rpm/O1_DoseTest(4).csv'
with open(datafile, 'r') as f:
    all_data = f.read()

all_data = all_data.split('\n\n\n')

lateral, profile, _, _ = np.genfromtxt(
    StringIO(all_data[-1]), 
    delimiter=',', 
    skip_header=2, 
    unpack=True)   

profilenm = profile / 10

fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.plot(lateral, profilenm, 'k', lw=2, label='Dose Test')
#ax.legend(frameon=True, loc='upper right', prop={'size': 21})
ax.set_xlabel('Lateral Profile [μm]', fontsize=21, fontweight='bold')
ax.set_ylabel('Total Profile (nm)', fontsize=21, fontweight='bold')
ax.tick_params(axis='both', labelsize=21)
plt.title('O1 Dose Test \n Base Dose = 100 μC/$\mathregular{cm^{2}}$', fontsize=21, fontweight='bold')
# plt.xlim([0, 1700])
plt.savefig('/Volumes/Sam/DekTak/DoseTest/4000rpm/O1_DoseTest(4).png')
plt.show()

