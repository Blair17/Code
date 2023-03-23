import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import find_peaks

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = '/Volumes/Sam/GMR1/November/301122/Background_int135_pol200_TE.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTE, spectrum_bTE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/301122/Background_int155_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTM, spectrum_bTM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

datafilename = '/Volumes/Sam/GMR1/November/301122/Y1_P625_int750_pol200_TE.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE, spectrum_TE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/301122/Y1_P625_int1300_pol290_TM.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TM, spectrum_TM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

normTE = 750/135
normTM = 1300/155

spectrum_TE1 = spectrum_bTE * normTE
true_spectrumTE = ( ( spectrum_TE / spectrum_TE1 ) - 0.15 ) * 100

norm = 750/135
spectrum_TM1 = spectrum_bTM * normTM
true_spectrumTM = ( ( spectrum_TM / spectrum_TM1 ) - 0.15 ) * 100

def FWHM(wavelength2,true_spectrum):
    deltax = wavelength2[1] - wavelength2[0]
    half_max = max(true_spectrum) / 2
    l = np.where(true_spectrum > half_max, 1, 0)
    
    return np.sum(l) * deltax

#############################################################################################

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(wavelength_TE, true_spectrumTE, 'k', lw=2, label='TE') 
ax.plot(wavelength_TM, true_spectrumTM, 'c', lw=2, label='TM') 
ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Reflectance (%)', fontsize=28, fontweight='bold')
ax.tick_params(axis='both', labelsize=25)
ax.legend(frameon=True, loc=0, prop={'size': 22})
# plt.title('AA2 - P440, TM',
#           fontsize=21, fontweight='bold', y=1.025)
plt.xlim([900, 1000])
plt.ylim([0, 100])
# plt.text(0.1, 0.98,''+date+'', ha='center', va='center', fontsize=10, 
#          fontweight='bold', color='c', transform=ax.transAxes)
plt.tight_layout()
# plt.savefig('/Volumes/Sam/GMR_X/May/120522/Plots/E10_I1_TE.png')

################################## PEAK VALUES ##############################################

# backgrounda = true_spectrumTE[:2000]

# idx_y_TE, _ = find_peaks(backgrounda, height=0.312)
# peaks_y_TE = backgrounda[idx_y_TE]
# peaks_x_TE = wavelength_TE[idx_y_TE]
# print('TE Refl Peak Index=', idx_y_TE, 'TE Refl Peak Value=', peaks_y_TE, 
#       'TE Wavelength At Peak=', peaks_x_TE)

# TE_peak_value = np.around(peaks_x_TE, 2)

# plt.text(0.5, 0.8,''+str(TE_peak_value)+'', ha='center', va='center', fontsize=16, 
#          fontweight='bold', color='r', transform=ax.transAxes)
# # plt.text(0.8, 0.8, '[666.66]', ha='center', va='center', fontsize=16, 
# #          fontweight='bold', color='r', transform=ax.transAxes)

plt.savefig('/Users/samblair/Desktop/Supp_Info_980nmRes.png')
plt.show()