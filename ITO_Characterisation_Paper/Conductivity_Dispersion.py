import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

def tick_function(X):
    '''
    Converts frequency ticks to wavelength ticks, converts from Hz to μm.
    Args:
        X: [array] array of x ticks to convert
    Returns:
        ["%.3f" % z for z in V]: [array] array of converted X ticks.
    '''
    c = 3E8
    V = (c/(X * 1E12)) * 1E6
    return ["%.2f" % z for z in V]

root = os.getcwd()

''' Conductivity '''
#             0 O2       1 O2         5 O2          7.5 O2
# sigmas = [713.2794807, 34.8682, 214.77940007818, 69.54]
sigmas = [225.67] # S/cm
mu = 3.12 # cm^2 / Vs
eps_inf = 4.95 # 700 nm 4.75

''' Omega P Squared '''
c = 3E8
e = 1.6E-19
m_e = 9.11E-31
m_star = m_e * 0.45
eps_0 = 8.85E-12
gamma = 1E14

''' Calculate N from sigmas '''
Ns = [sig / (mu * e) for sig in sigmas]  # cm^-3
N_m3 = [n * 1E6 for n in Ns]  # m^-3
# N_m3 = int(1E20)
omega_p_sqs = [(N * (e ** 2)) / (eps_0 * m_star) for N in N_m3]
# omega_p_sqs = (N_m3 * (e ** 2)) / (eps_0 * m_star)
print(f'N_m3 = {N_m3}')
print(f'omega p sq = {omega_p_sqs}')

''' Wavelength '''
frequency_THz = np.arange(1000, 10, -1)
frequency = [f * 1E12 for f in frequency_THz]
wavrange = [c / f for f in frequency]
omega = [2 * np.pi * f for f in frequency]
omega_sq = [w ** 2 for w in omega]

''' Drude '''
eps_drude = []
for omp in omega_p_sqs:
    eps_drude.append([eps_inf - (omp / w) for w in omega_sq])

eps_imag = []
for omp in omega_p_sqs:
    eps_imag.append([((eps_inf * omp) / (gamma * w**3)) for w in omega]) 
# print(eps_imag)

ticks = [10, 200, 400, 600, 800]
colours = ['r', 'c', 'r', 'b', 'g']
labels = ['ε$_r$', '0 SCCM', '5 SCCM', '7.5 SCCM']
colours2 = ['r', 'c', 'r', 'b', 'g']
labels_1 = ['ε$_i$', 'ε$_r$ 11% O$_2$', 'ε$_r$ 5% O$_2$', 'ε$_r$ 7.5% O$_2$']

''' Plot '''
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=[10, 7])
ax2 = ax1.twiny()
for index, eps in enumerate(eps_drude):
    ax1.plot(frequency_THz, eps, f'{colours[index]}', lw=2, label=f'{labels[index]}')
ax1.axhline(y=0, color='k', lw=2, linestyle='--')

# for i, ep in enumerate(eps_imag):
#     ax1.plot(
#         frequency_THz[::-1],
#         ep,
#         f'{colours2[i]}',
#         lw=2,
#         label=f'{labels_1[i]}')

# ax1.plot(freqs_AA[::-1], n_AA**2, 'o', markersize=10, markerfacecolor='k', markeredgecolor='k', markeredgewidth=1)
# # plt.errorbar(freqs_N5[::-1], eps_N5, yerr=yerr, fmt='None', ecolor='c', capsize=3)

ax1.legend(loc='lower left', ncol=2, prop={'size': 16}, frameon=True)
ax1.set_ylim(-3.9, 5.9)
ax2.set_xticks(ticks)
ax2Ticks = ax2.get_xticks()
ax2.set_xticklabels(ticks)
ax1Ticks = ax2Ticks
ax1.set_xticks(ax1Ticks)
ax1.set_xbound(ax2.get_xbound())
ax1.tick_params(axis='both', labelsize=(20), which='major')
ax2.tick_params(axis='both', labelsize=(20), which='major')
ax1.set_xticklabels(tick_function(ax1Ticks))
ax2.set_xlabel("Frequency (THz)", fontsize=(22), fontweight='bold', labelpad=20)
ax1.set_xlabel("Wavelength (μm)", fontsize=(22), fontweight='bold')
ax1.set_ylabel(r'$\bf{\epsilon_{r}}$ (a.u.)', fontsize=(20), fontweight='bold')

eps_array = np.array(eps_drude)
zero_mask = eps_array > 0

difference = np.diff(zero_mask, axis=1)
data1 = np.where(difference == True)

ax1.yaxis.set_major_locator(MultipleLocator(2))
# ax1.yaxis.set_minor_locator(AutoMinorLocator())
# ax2.xaxis.set_minor_locator(AutoMinorLocator())
# ax1.xaxis.set_minor_locator(AutoMinorLocator())

ax1.invert_xaxis()
ax2.invert_xaxis()

ax1.grid(axis='both', which='both')
ax2.grid(axis='both', which='both')

plt.tight_layout()
# plt.savefig('/Users/samblair/Desktop/300_dpi/Fig4a_mu.png')
# plt.grid()
plt.show()       