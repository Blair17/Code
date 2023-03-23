import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import find_peaks

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = '/Volumes/Sam/ITO_Characteristics_Paper/Data/Background/Y1_Background_int135_pol200_TE.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTE, spectrum_bTE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/ITO_Characteristics_Paper/Data/Background/Y1_Background_int155_pol290_TM.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTM, spectrum_bTM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

###########################################################################################

datafilename = '/Volumes/Sam/GMR1/November/301122/Y1_P400_int350_pol200_TE.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE, spectrum_TE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/301122/Y1_P400_int550_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TM, spectrum_TM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

normTE = 490/135
normTM = 700/155

background_TE = spectrum_bTE * normTE
spec_TE = spectrum_TE / background_TE * 100

background_TM = spectrum_bTM * normTM
spec_TM = spectrum_TM / background_TM * 100

#############################################################################################

fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(wavelength_TE, spec_TE, 'r', lw=2, label='TE')
ax.plot(wavelength_TM, spec_TM, 'm', lw=2, label='TM') 
# ax.plot(wavelength_bTE,spectrum_bTE)
ax.set_xlabel('Wavelength (nm)', fontsize=26, fontweight='bold')
ax.set_ylabel('Reflectance (%)', fontsize=26, fontweight='bold')
ax.tick_params(axis='both', labelsize=23)
ax.legend(frameon=True, loc='upper right', prop={'size': 23})
# plt.title('TE & TM Spectra - Y1, P550', 
#           fontsize=21, fontweight='bold', y=1.025)
plt.xlim([575, 750])
plt.ylim([0, 100])
# plt.text(0.1, 0.98,''+date+'', ha='center', va='center', fontsize=10, 
#          fontweight='bold', color='c', transform=ax.transAxes)
plt.tight_layout()

plt.show()

