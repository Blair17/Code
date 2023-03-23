import numpy as np
import matplotlib.pyplot as plt
import LoadDektakData as LD 

datafile = '/Volumes/Sam/DekTak/C_Series/C8/C8a/Si_ITO_C8a_Post_Clean(2).csv'
etch_threshold = 200
spike_threshold = 1000
valley_threshold = -1000

lateral, profile = LD.loadData(datafile, plot=False)

resolution = lateral[1]-lateral[0]
profile = [i if i < spike_threshold else spike_threshold for i in profile]
profile = [i if i > valley_threshold else valley_threshold for i in profile]
profile = np.asarray(profile)

profile_t = np.where(profile < etch_threshold, 0, 1)

peak = [0]
trench = [0]
last_value = profile_t[0]
for i in profile_t:
    if (i == 1):
        if (i != last_value):
            peak.append(0)
        peak[-1] = peak[-1] + resolution
    if (i == 0):
        if (i != last_value):
            trench.append(0)
        trench[-1] = trench[-1] + resolution
    last_value = i

peak_height = []
trench_depth = []
last_value = None
for idx, i in enumerate(profile_t):
    if last_value is None:
        last_value = not i
    if (i == 1):
        if (i != last_value):
            peak_height.append([idx, None])
        peak_height[-1][-1] = idx
    if (i == 0):
        if (i != last_value):
            trench_depth.append([idx, None])
        trench_depth[-1][-1] = idx
    last_value = i

for idx, (p, t) in enumerate(zip(peak_height, trench_depth)):
    peak_height[idx] = np.mean(profile[p[0]:p[1]])
    trench_depth[idx] = np.mean(profile[t[0]:t[1]])

########################## Plotting ##########################

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
ax.plot(lateral, profile, 'b')
ax2 = ax.twinx()
ax2.plot(lateral, profile_t, 'r', alpha=0.5)
ax.set_xlabel('Lateral Profile [μm]', fontsize=16)
ax.set_ylabel('Total Profile [A]', fontsize=16)
plt.title('Si-ITO C8a Etch Depth', fontsize=16, fontweight='bold')

if profile_t[0] == 1:
    x_loc_p = 0.0
    x_loc_t = 0.1
else:
    x_loc_p = 0.1
    x_loc_t = 0.0

y_loc_p = 0.9
y_loc_t = 0.1
spacing_p = (1 - (2*x_loc_p)) / len(peak)
spacing_t = (1 - (2*x_loc_t)) / len(trench)
#print(spacing_p, spacing_t)
ax.text(0, 1.0, 'Peak heights =', color='red', transform=ax.transAxes)
ax.text(0, 0.0, 'Trench depths =', color='blue', transform=ax.transAxes)
for idx, (p, t) in enumerate(zip(peak_height, trench_depth)):
    x = x_loc_p + idx*spacing_p
    y = y_loc_p + (idx%2)*0.05
    label = '{:.2f}A'.format(p)
    ax.text(x, y, label, color='red', transform=ax.transAxes)

    x = x_loc_t + idx*spacing_t
    y = y_loc_t - (idx%2)*0.05
    label = '{:.2f}um'.format(t)
    ax.text(x, y, label, color='blue', transform=ax.transAxes)

ax.set_ylim([valley_threshold, spike_threshold])
ax2.set_ylim([-0.5, 1.5])

plt.savefig('/Volumes/Sam/DekTak/C_Series/C8/C8a/Si_ITO_C8a_heights.png')

depth = peak_height[0] - trench_depth[0]
print('Peak Heights=', peak_height, '\n' 'Trench Depths=', trench_depth)
print('Etch Depth=', depth)
plt.show()