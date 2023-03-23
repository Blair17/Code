import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
import itertools
import scipy.ndimage
import sys
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1
np.set_printoptions(threshold=sys.maxsize)

def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

root = os.getcwd()

################################## PARAMETERS ##############################################

pmin = 430 # nm
pmax = 461 # nm
pstep = 1 # nm
nmin = 0.2
nmax = 0.81
nstep = 0.01

# p = 450
nharm = 20
n = 3.9
subindex = 1.456
gratingthickness = 200 # nm
# dutycycle = 0.7
TEamp = 0
TMamp = 1

lambda1 = 652 

prange = np.arange(pmin, pmax, pstep)
nrange = np.arange(nmin, nmax, nstep)

################################## DATA READ IN / SIMULATE ##############################################

var_lists = list(itertools.product([prange],[nrange]))
refl_array = []

for p,dutycycle in itertools.product(prange, nrange):
        args = (f'p = {p}; gratingthickness = {gratingthickness}; dutycycle = {dutycycle};'
                f'nharm = {nharm}; lambda1 = {lambda1};'
                f'n = {n}; subindex = {subindex}; TEamp = {TEamp}; TMamp = {TMamp}')

        lua_script = '/Users/samblair/Desktop/Code/Projects/High_Refl_Phase_Change/GMR_Param_Pixels.lua'
        os.system(f'S4 -a "{args}" {lua_script}')

        datafile = '/Users/samblair/Desktop/Refl_data.csv'
        data = np.genfromtxt(datafile, delimiter=',', skip_header=1)
        
        print(p,dutycycle)
        refl_array.append(data)

TwoD_data = np.reshape(refl_array, (len(prange), len(nrange)))   
df = pd.DataFrame(TwoD_data)
df.to_csv(f'/Users/samblair/Desktop/Refl_data_dump/Lambda_650nm/Si_Substrate/Si_Sub_Refl_{nmin}_{nmax}_{nstep}_{pmin}nm_{pmax}nm_{pstep}nm_{nharm}_T{gratingthickness}.csv', index=False) 

# x0, y0 = 0, 10
# x1, y1 = 40, 10
# num = 1000
# x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)
# zi = scipy.ndimage.map_coordinates(TwoD_data, np.vstack((x,y)))

########################################### PLOTTING ########################################################

TwoD_data1 = np.transpose(TwoD_data)

fig, ax = plt.subplots(figsize=[10,6])
mycmap1 = plt.get_cmap('jet')
k = ax.imshow(np.flipud((TwoD_data)),cmap=mycmap1)
ax.set_xlabel('FF', fontsize=16, fontweight='bold')
ax.set_ylabel('Period [nm]', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', labelsize=20)
# ax.plot([x0, x1], [y0, y1], 'ro-')
add_colorbar(k)
# plt.axes().set_aspect('equal')

x_labels = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8','0.9']
y_labels = ['465', '460', '455', '450', '445', '440', '435', '430']
ax.set_xticklabels(x_labels)
ax.set_yticklabels(y_labels)

# fig, ax = plt.subplots(figsize=[10,7])
# ax.plot(zi, lw=3, color='r')
# ax.set_xlabel('FF [%]', fontsize=16, fontweight='bold')
# ax.set_ylabel('Reflectance', fontsize=16, fontweight='bold')
# ax.tick_params(axis='both', labelsize=14)

# df2 = pd.DataFrame(zi)
# df.to_csv(f'/Users/samblair/Desktop/Refl_data_dump/Line_Extractions/Refl_Line_Extraction_{x0},{y0}_{x1},{y1}.csv')

fig.tight_layout()
# plt.savefig(f'/Users/samblair/Desktop/Refl_data_dump/Lambda_650nm/Si_Substrate/Si_Sub_P_vs_n_T{gratingthickness}.png')
plt.show()