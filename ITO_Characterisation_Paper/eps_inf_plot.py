import numpy as np
import matplotlib.pyplot as plt

def tick_function(X):
    '''
    Converts frequency ticks to wavelength ticks, converts from Hz to μm.
    Args:
        X: [array] array of x ticks to convert
    Returns:
        ["%.0f" % z for z in V]: [array] array of converted X ticks in nm (1E9).
    '''
    V = (c/(X * 1E12)) * 1E9
    return ["%.0f" % z for z in V]

c = 3E8

# freq_THz = [358, 321, 293, 271, 253, 239, 227, 216, 207, 199, 192, 185, 179, 174, 169, 165, 161]

freq_THz = [716, 506, 414, 358, 321, 293, 271, 253, 239, 227, 216, 207, 199, 192, 185, 179, 174, 169,
            165, 161, 157, 153, 150, 147, 144, 141, 138, 136, 133, 131, 129, 127, 125, 123, 121, 120,
            118, 117, 115, 114]

freq = [f * 1E12 for f in freq_THz]
wav = [c / f for f in freq]
wav_nm = [w * 1E9 for w in wav]

freq_ticks = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

# eps_inf = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
eps_inf = np.arange(0.5,20.5,0.5)

t = eps_inf

fig, ax = plt.subplots(figsize=(10,7))
ax2 = ax.twinx()
ax.scatter(eps_inf, freq_THz, c=t, marker='s', s=50, cmap='gnuplot2')
ax.set_xlabel('$\epsilon_\infty$', fontsize=23, fontweight='bold')
ax.set_ylabel('Frequency (THz)', fontsize=23, fontweight='bold')
ax2.set_ylabel('Wavelength (nm)', fontsize=23, fontweight='bold', rotation=270)
# ax.tick_params(axis='both', labelsize=21)

ticks = freq_ticks
ax.set_yticks(ticks)
axTicks = ax.get_yticks()
ax.set_yticklabels(ticks)
ax2Ticks = axTicks
ax2.set_yticks(ax2Ticks)
ax2.set_xbound(ax.get_xbound())
ax2.tick_params(axis='both', labelsize=16)
ax.tick_params(axis='both', labelsize=16)
ax2.set_yticklabels(tick_function(axTicks))

plt.tight_layout()
plt.grid()
plt.show()