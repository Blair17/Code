import os
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
np.set_printoptions(threshold=sys.maxsize)

root = os.getcwd()

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

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

''' Conductivity '''
sigmas = [713]
mu = np.arange(1,8,2) # cm^2 / Vs
# mu = [2, 4, 8]
# mu = np.arange(1,60,1)
eps_inf = 4.9

''' Omega P Squared '''
c = 3E8
e = 1.6E-19
m_e = 9.11E-31
m_star = m_e * 0.35
eps_0 = 8.85E-12

''' Calculate N from sigmas '''
N_m3 = [(sigmas / (m * e)) * 1E6 for m in mu]  # cm^-3 Calculates an N for each value of mu
print(N_m3)
omega_p_sqs = [(N * (e ** 2)) / (eps_0 * m_star) for N in N_m3]

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

ticks = [10, 200, 400, 600, 800]
n = 1

''' Plot '''
colors = len(mu)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=[10, 7])
ax2 = ax1.twiny()
for eps, i, index in zip(eps_drude,range(colors),mu):
    ax1.plot(frequency_THz, eps, lw=4, color=cmap[i], label=f'$\mu$={index}')

ax1.axhline(y=0, color='k', lw=2, linestyle='--', alpha=0.5)

ax1.legend(loc='lower left', ncol=2, prop={'size': 22}, frameon=True)
ax1.set_ylim(-3.9, 5.9)
# ax1.set_yticks([-4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
ax2.set_xticks(ticks)
ax2Ticks = ax2.get_xticks()
ax2.set_xticklabels(ticks)
ax1Ticks = ax2Ticks
ax1.set_xticks(ax1Ticks)
ax1.set_xbound(ax2.get_xbound())
ax1.tick_params(axis='both', labelsize=(n*28), which='major')
ax2.tick_params(axis='both', labelsize=(n*28), which='major')
ax1.set_xticklabels(tick_function(ax1Ticks))
ax2.set_xlabel("Frequency (THz)", fontsize=(n*32), fontweight='bold', labelpad=20)
ax1.set_xlabel("Wavelength (μm)", fontsize=(n*32), fontweight='bold')
ax1.set_ylabel(r'$\bf{\epsilon_{r}}$ (a.u.)', fontsize=(n*28), fontweight='bold')
# plt.title('', fontsize=25, fontweight='bold', y=1.12)

eps_array = np.array(eps_drude)
zero_mask = eps_array > 0

difference = np.diff(zero_mask, axis=1)
data1 = np.where(difference == True)

ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax1.xaxis.set_minor_locator(AutoMinorLocator())

ax1.invert_xaxis()
ax2.invert_xaxis()

plt.tight_layout()
# plt.savefig('/Users/samblair/Desktop/300_dpi/Fig4a_mu.png')
plt.show()    