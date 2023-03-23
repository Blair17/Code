import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

SR = [41.74, 140.3, 2654.00, 1935.20, 907.73, 714.158, 1117.60]
# SR = [39.71, 1086.33, 1062.00, 1986.67, 1953.33, 1423.67]
# 87.30
# Sigma = 1 / SR * T
# [0, 1, 2.5, 3.5, 5, 7.5]
# thickness = 150E-09

# thickness = [190E-09, 240E-09, 250E-09, 265E-09, 245E-09, 245E-09]
thickness = [1.91E-07, 2.60E-07, 2.51E-07, 2.90E-07, 2.70E-07, 2.46E-07, 2.47E-07]
thickness_err = 70E-09
sigma = [1 / (s * t) * 0.01 for s, t in zip(SR, thickness)]
print(sigma)

# mobility = [4.5, 30, 24, 12, 7, 12]
mobility = [28.57, 25.74, 24.42, 1.998, 1.077, 1.114, 1.699]

O2 = [0, 0.5, 1, 2.5, 3, 5, 7.5]
O2_percent = [(i / (i + 20)) * 100 for i in O2] # O2 / O2 + Ar

SR_err = [0.47, 0.22, 32.20, 33.38, 79.13, 31.40, 19.64]
sigma_err = [Z * ((s_err / s) ** 2 + (thickness_err / t) ** 2) for s_err, s, t, Z in zip(SR_err, SR, thickness, sigma)]
# print(sigma_err)
mobility_err = 1

labels = ['0', '0.5', '1', '2.5', '3.5', '5', '7.5']

# f = interp1d(O2_percent, SR, kind='quadratic')
# xnew = np.linspace(0,27,num=200,endpoint=True)

# X_Y_Spline = make_interp_spline(O2_percent, SR)
# X = np.linspace(min(O2_percent), max(O2_percent), 500)
# Y = X_Y_Spline(X)

fig, ax = plt.subplots(figsize=(10,7))
ax2 = ax.twinx()
# ax3 = ax.twiny()
ax.scatter(O2_percent,sigma, marker='o', color='k', s=150)
ax.errorbar(O2_percent, sigma, yerr=sigma_err, fmt='None', ecolor='k', capsize=3)
ax2.scatter(O2_percent, mobility, marker='^', color='r', s=200)
ax2.errorbar(O2_percent, mobility, yerr=mobility_err, fmt='None', ecolor='r', capsize=3)
ax.plot(O2_percent,sigma, 'k--', label='Conductivity')
ax2.plot(O2_percent, mobility, 'r--', label='Mobility')

# ax.plot(xnew,f(xnew), 'r-', label='Interpolation')
ax2.set_ylim([0,35])
ax.set_xlabel('$\mathregular{O_{2}}$ Concentration (%)', fontsize=28, fontweight='bold')
ax.set_ylabel('Conductivity (S/cm)', fontsize=28, fontweight='bold')
# ax2.set_ylabel('Mobility (cm$^2$/Vs)', fontsize=28, fontweight='bold', color='r', rotation=270, labelpad=40)
ax2.set_ylabel('Mobility ' r'($\bf{cm^{2}}$/Vs)', fontsize=28, fontweight='bold', color='r', rotation=270, labelpad=40)
ax.tick_params(axis='both', labelsize=25)
ax2.tick_params(axis='both', labelsize=25)
ax.set_yscale('log')
# ax2.set_yscale('log')
# ax.set_ylim([0,100])
# ax3.tick_params('y', labelsize=21)

# ax3.set_xticks(O2_percent)
# ax3.set_xticklabels(labels)

# plt.title('$\mathregular{O_{2}}$ Concentration vs Sheet Resistance \n', fontsize=22, fontweight='bold', color='k')
plt.grid()
plt.tight_layout()
# plt.savefig('/Users/samblair/Desktop/300_dpi/Fig2.png')
# plt.legend()
# plt.savefig('/Users/samblair/Desktop/PhD/ITO_Characterisation_Paper/Figures/Fig2_O2_vs_Sigma.png')
# plt.show()