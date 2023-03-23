import os
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()

datafilename = '/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/Drude_Loops/Data/N5_eps_values_postetch.csv'
datafilepath = os.path.join(
    root,
    datafilename)
freqs_N5, n_N5, eps_N5 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

def tick_function(X):
    '''
    Converts frequency ticks to wavelength ticks, converts from Hz to μm.
    Args:
        X: [array] array of x ticks to convert
    Returns:
        ["%.3f" % z for z in V]: [array] array of converted X ticks.
    '''
    V = (c/(X * 1E12)) * 1E6
    return ["%.3f" % z for z in V]

''' Conductivity '''
#             0 O2       2.5 O2         5 O2          7.5 O2
# sigmas = [713.2794807, 34.8682, 214.77940007818, 69.54]
sigmas = [1254.34]
mu = 28 # cm^2 / Vs
eps_inf = 3.5
loss = 0.08

''' Omega P Squared '''
c = 3E8
e = 1.6E-19
m_e = 9.11E-31
m_star = m_e * 0.35
eps_0 = 8.85E-12
# gamma = 0

''' Calculate N from sigmas '''
N_m3 = int(1.98E+26)
omega_p_sqs = (N_m3 * (e ** 2)) / (eps_0 * m_star)
print(f'N_m3 = {N_m3}')

''' Wavelength '''
frequency_THz = np.arange(901, 1, -1)
frequency = [f * 1E12 for f in frequency_THz]
wavrange = [c / f for f in frequency]
omega = [2 * np.pi * f for f in frequency]
omega_sq = [w ** 2 for w in omega]

''' Drude '''
eps_drude = []
eps_drude.append([eps_inf - (omega_p_sqs / w) for w in omega_sq])

eps_imag = []
eps_imag.append([((eps_inf * omega_p_sqs) / w**2)-13 for w in omega]) 

ticks = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]
colours = ['k', 'c', 'r', 'b', 'g']
labels = ['ε$_r$', '0 SCCM', '5 SCCM', '7.5 SCCM']
colours2 = ['r', 'c', 'r', 'b', 'g']
labels_1 = ['ε$_i$', 'ε$_r$ 11% O$_2$', 'ε$_r$ 5% O$_2$', 'ε$_r$ 7.5% O$_2$']

''' Plot '''
fig, ax1 = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=[10, 7])
ax2 = ax1.twiny()
ax3 = ax1.twinx()
for index, eps in enumerate(eps_drude):
    ax1.plot(
        frequency_THz[::-1],
        eps,
        f'{colours[index]}',
        lw=2,
        label=f'{labels[index]}')
ax1.axhline(
    y=0,
    color='k',
    lw=2,
    linestyle='--')
for i, ep in enumerate(eps_imag):
    ax1.plot(
        frequency_THz[::-1],
        ep,
        f'{colours2[i]}',
        lw=2,
        label=f'{labels_1[i]}')
ax1.legend(
    loc='upper right',
    prop={'size': 18})

tick_labs = ['0', '1', '2', '3', '4']


ax1.set_ylim(-13, 5)
ax2.set_xticks(ticks)
ax2Ticks = ax2.get_xticks()
ax2.set_xticklabels(ticks[::-1])
ax1Ticks = ax2Ticks
ax1.set_xticks(ax1Ticks)
ax1.set_xbound(ax2.get_xbound())
ax1.tick_params(axis='both', labelsize=16)
ax2.tick_params(axis='both', labelsize=16)
ax1.set_xticklabels(tick_function(ax1Ticks[::-1]))
ax2.set_xlabel(
    "Frequency [THz]",
    fontsize=21,
    fontweight='bold')
ax1.set_xlabel(
    "Wavelength [μm]",
    fontsize=21,
    fontweight='bold')
ax1.set_ylabel(
    "ε$_r$ [au]",
    fontsize=21,
    fontweight='bold')
ax3.set_ylabel("ε$_i$ [au]",
    fontsize=21,
    fontweight='bold')
ax3.set_yticklabels(tick_labs, fontsize=16)
plt.title('', fontsize=25, fontweight='bold', y=1.12)
plt.ylim([-13, 5])

ax1.plot(freqs_N5[::-1], eps_N5, 'o', markersize=10, markerfacecolor='c', markeredgecolor='k', markeredgewidth=1)
plt.errorbar(freqs_N5[::-1], eps_N5, fmt='None', ecolor='c', capsize=3)

plt.tight_layout()
ax1.grid()
plt.show()      