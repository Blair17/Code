import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
import scipy.ndimage
import sys
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

period = 350
gratingthickness = 140
dutycycle = 0.7
ridgewidth = period * dutycycle
gratingindex = 2.06
sio2index = 1.45
loss = 0.0
ITOwg = 230 - gratingthickness

nharm = 20
TEamp = 0
TMamp = 1

zmin = -period/2 + gratingthickness
zmax = period/2 + gratingthickness
xmin = -period/2
xmax = period/2

xstep = 1
zstep = 1

lambda1 =  582.77777778 # Incident Wavelength

################################## DATA READ IN / SIMULATE ##############################################

simulate = True

if simulate:
        args = (f'period = {period}; gratingthickness = {gratingthickness}; dutycycle = {dutycycle};'
                f'ridgewidth = {ridgewidth}; lambda1 = {lambda1}; zmin = {zmin}; nharm = {nharm};'
                f'gratingindex = {gratingindex}; sio2index = {sio2index}; TEamp = {TEamp}; TMamp = {TMamp};'
                f'zmax = {zmax}; xmin = {xmin}; xmax = {xmax}; xstep = {xstep}; zstep = {zstep}; ITOwg = {ITOwg};')

        lua_script = '/Users/samblair/Desktop/Code/Projects/Field_Plots/Field_Extraction.lua'
        os.system(f'S4 -a "{args}" {lua_script}')

datafile = '/Users/samblair/Desktop/spectrum_E.csv'
data = np.genfromtxt(datafile, delimiter=',')

datafile_eps = '/Users/samblair/Desktop/eps_r.csv'
data2 = np.genfromtxt(datafile_eps, delimiter=',')

################################## ANALYSIS ##############################################

data_eps = np.ones_like(data2)
for z_idx, z in enumerate(data2):
        for x_idx, d in enumerate(z):
                if d > 3.8:
                        data_eps[z_idx][x_idx] = 2.1
                # elif d == 2.1:
                #         data_eps[z_idx][x_idx] = 1.45
                # else:
                #         data_eps[z_idx][x_idx] = 1.0

x = np.arange(xmin, xmax+1, xstep)
z = np.arange(zmin, zmax+1, zstep)

# mask_ITO = data2 > 3.8
# data_eps = (data2 * mask_ITO)
# # print(mask_ITO.shape)
# # print(data2.shape)
# # print(data_eps.shape)

# data_field = data * mask_ITO

# print(np.sum(np.abs(data_field)))

# ################################## PLOTTING ##############################################

# fig, (ax1, ax2) = plt.subplots(2, 1)
fig, ax = plt.subplots()
mycmap1 = plt.get_cmap('gnuplot2')
k = ax.imshow((data)*(1), extent=[xmin,xmax,zmin,zmax], cmap=mycmap1)
ax.contour(x, z, np.flipud(data_eps), extent=[xmin,xmax,zmin,zmax], colors=('k'))
ax.set_xlabel('X Position [nm]', fontsize=16, fontweight='bold')
ax.set_ylabel('Z Position [nm]', fontsize=16, fontweight='bold')
# ax1.set_title(f'TM {lambda1} nm (P = {period} nm, \n' 
        #      f'T$_G$ = {gratingthickness} nm, T$_W$ = {ITOwg}, FF = {dutycycle})', 
        #      fontsize=18, fontweight='bold')
ax.tick_params(axis='both', labelsize=14)

# ax2.imshow(data_eps,  extent=[xmin,xmax,zmin,zmax])

add_colorbar(k)
fig.tight_layout()
# plt.savefig('/Users/samblair/Desktop/802.png')
plt.show()