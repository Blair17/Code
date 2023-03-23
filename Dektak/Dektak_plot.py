import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
from datetime import datetime

date = datetime.now().strftime("%d-%m-%Y")

datafile = '/Volumes/Sam/DekTak/DoseTest/4000rpm/O1_DoseTest(4).csv'
with open(datafile, 'r') as f:
    all_data = f.read()

all_data = all_data.split('\n\n\n')

lateral, profile, _, _ = np.genfromtxt(
    StringIO(all_data[-1]), 
    delimiter=',', 
    skip_header=2, 
    unpack=True)   

datafile = '/Volumes/Sam/DekTak/DoseTest/4000rpm/O1_DoseTest_PostEtch(1).csv'
with open(datafile, 'r') as f1:
    all_data = f1.read()

all_data = all_data.split('\n\n\n')

lateral1, profile1, _, _ = np.genfromtxt(
    StringIO(all_data[-1]), 
    delimiter=',', 
    skip_header=2, 
    unpack=True)

profilenm = profile / 10
profile1nm = profile1 / 10

lateral1a = lateral1 - 0
profile1a = profile1nm - 0

#lateral2 = lateral 
#profile2 = profilenm + 350

fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.plot(lateral, profilenm, 'k', lw=2, label='Pre-Etch')
ax.plot(lateral1, profile1nm, 'c', lw=2, label='Post-Etch')
#ax.legend(frameon=True, loc='upper left', prop={'size': 21})
ax.set_xlabel('Lateral Profile [μm]', fontsize=21, fontweight='bold')
ax.set_ylabel('Total Profile [nm]', fontsize=21, fontweight='bold')
ax.tick_params(axis='both', labelsize=21)
plt.title('O1 Dose Test', fontsize=21, fontweight='bold')
#plt.ylim([-300, 400])
#plt.xlim([0, 306])
plt.text(0.94, 0.98,''+date+'', ha='center', va='center', fontsize=10, fontweight='bold', color='c', transform=ax.transAxes)
# plt.savefig('/Volumes/Sam/Dektak/E_Series/E1/Glass_ITO_E1_Depth.png')
plt.show()
