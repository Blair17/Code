import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import find_peaks

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError as msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = '/Volumes/Sam/GMR1/November/141122/Background_int135_pol200_TE.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTE, spectrum_bTE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/141122/Background_int165_pol290_TM.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTM, spectrum_bTM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

###########################################################################################

datafilename = '/Volumes/Sam/GMR1/November/141122/AF2/AF2_P350_int1050_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE_350, spectrum_TE_350 = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/141122/AF2/AF2_P400_int1000_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE_400, spectrum_TE_400 = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/141122/AF2/AF2_P475_int550_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE_475, spectrum_TE_475 = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = '/Volumes/Sam/GMR1/November/141122/AF2/AF2_P550_int1000_pol290_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE_550, spectrum_TE_550 = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

normTE350 = 1050/165
normTE400 = 1000/165
normTE475 = 550/165
normTE550 = 1000/165

background_TE_350 = spectrum_bTM * normTE350
spec_TE_350 = (spectrum_TE_350 / background_TE_350) * 100

background_TE_400 = spectrum_bTM * normTE400
spec_TE_400 = (spectrum_TE_400 / background_TE_400) * 100

background_TE_475 = spectrum_bTM * normTE475
spec_TE_475 = (spectrum_TE_475 / background_TE_475) * 100

background_TE_550 = spectrum_bTM * normTE550
spec_TE_550 = (spectrum_TE_550 / background_TE_550) * 100

wav_TE_550 = np.array([a * 0.001 for a in wavelength_TE_550])
wav_TE_475 = np.array([a * 0.001 for a in wavelength_TE_475])
wav_TE_400 = np.array([a * 0.001 for a in wavelength_TE_400])
wav_TE_350 = np.array([a * 0.001 for a in wavelength_TE_350])

#############################################################################################

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(wav_TE_550, spec_TE_550, 'crimson', lw=3, label='Period = 0.550 μm')
ax.plot(wav_TE_475, spec_TE_475, 'darkviolet', lw=3, label='Period = 0.475 μm')
ax.plot(wav_TE_400, spec_TE_400, 'mediumblue', lw=3, label='Period = 0.400 μm')
ax.plot(wav_TE_350, spec_TE_350, 'k', lw=3, label='Period = 0.350 μm')

ax.set_xlabel('Wavelength (μm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Reflectance (%)', fontsize=28, fontweight='bold')
ax.tick_params(axis='both', labelsize=25)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper right', prop={'size': 22})


# ax.legend(frameon=True, loc='upper right', prop={'size': 18})
plt.xlim([0.551, 0.879])
plt.ylim([15, 50])
plt.tight_layout()
plt.grid()
plt.savefig('/Users/samblair/Desktop/300_dpi/Fig1c.png')
# plt.show()

