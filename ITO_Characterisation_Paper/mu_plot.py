import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

freq_THz = [647, 458, 374, 324, 290, 264, 245, 229, 216, 205, 195, 187, 180, 
            173, 167, 162, 157, 153, 149, 145, 142, 138, 135, 132, 130, 127, 
            125, 123, 121, 119, 117, 115, 113, 111, 110, 108, 107, 105, 104, 
            103, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90,  
            89, 88, 88, 87, 86, 85, 85, 84, 83, 83, 82, 81, 81,  
            80, 79, 79, 78, 78, 77, 77, 76, 76, 75, 75, 74, 74,  
            73, 73, 72, 72, 71, 71, 71, 70, 70, 69, 69, 69, 68,  
            68, 68, 67, 67, 66, 66, 66, 65, 65, 65, 65, 64, 64,  
            64, 63, 63, 63, 62, 62, 62, 62, 61, 61, 61, 61, 60,  
            60, 60, 60]

freq = [f * 1E12 for f in freq_THz]
wav = [c / f for f in freq]
wav_nm = [w * 1E9 for w in wav]

freq_ticks = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

mu = np.arange(0.5,60.5,0.5)

t = mu

fig, ax = plt.subplots(figsize=(10,7))
ax2 = ax.twinx()
ax.scatter(mu, freq_THz, c=t, marker='s', s=50, cmap='gnuplot2')

ax.set_xlabel('$\mu$', fontsize=23, fontweight='bold')
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