import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
import scipy.ndimage
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1

root = os.getcwd()

period = 1000000 / 600
subp = 500
gratingthickness = 750
dutycycle = 0.5
ridgewidth = subp * dutycycle
accum_width = 4
gratingindex = 2
accumulationindex = 2.0
depletionindex = 2.1 
sio2index = 1.45
accindex = 2.1
loss = 0.0

nharm = 20
TEamp = 1
TMamp = 0

zmin = -1000000*5
zmax = 1000000*5
xmin = -1000000*5
xmax = 1000000*5

xstep = 10000
zstep = 10000

lambda1 =  500
simulate = True

if simulate:
        args = (f'period = {period}; accumulationindex = {accumulationindex}; depletionindex = {depletionindex}; gratingthickness = {gratingthickness}; dutycycle = {dutycycle};'
                f'ridgewidth = {ridgewidth}; lambda1 = {lambda1}; zmin = {zmin}; nharm = {nharm};'
                f'gratingindex = {gratingindex}; accum_width = {accum_width}; sio2index = {sio2index}; TEamp = {TEamp}; TMamp = {TMamp};'
                f'zmax = {zmax}; xmin = {xmin}; xmax = {xmax}; subp = {subp}; accindex = {accindex}; xstep = {xstep}; zstep = {zstep};')

        lua_script = 'Code/Projects/Field_Plots/E_Field_accumulation.lua'
        os.system(f'S4 -a "{args}" {lua_script}')

datafile1 = '/Users/samblair/Desktop/eps_r.csv'
data2 = np.genfromtxt(datafile1, delimiter=',')

data3 = np.ones_like(data2)
for z_idx, z in enumerate(data2):
        for x_idx, d in enumerate(z):
                if d > 2.2:
                        data3[z_idx][x_idx] = 2.2 # 2.0
#                 # if d < 2.15 and d > 2.0:
#                 #         data3[z_idx][x_idx] = 1.45
                
datafile = '/Users/samblair/Desktop/spectrum_E.csv'
x = np.arange(xmin, xmax+1, xstep) 
z = np.arange(zmin, zmax+1, zstep)
data = np.genfromtxt(datafile, delimiter=',')

# fig, ax = plt.subplots(1, 1, figsize=(10, 7))
# # c = ax.pcolor(data, shading='gouraud')
# c = ax.imshow(data2, extent=[xmin,xmax,zmin,zmax])
# divider = make_axes_locatable(ax)
# cax = divider.new_vertical(size="5%", pad=0.7, pack_start=True)
# fig.add_axes(cax)
# ax.set_title('λ = '+str(lambda1)+' nm (P = '+str(subp)+' nm, T = '+str(gratingthickness)+' nm, FF = '+str(dutycycle)+' %)', fontsize=18, fontweight='bold')
# fig.colorbar(c, cax=cax, orientation="horizontal")
# ax.set_xlabel('X Position [nm]', fontsize=16, fontweight='bold')
# ax.set_ylabel('Z Position [nm]', fontsize=16, fontweight='bold')
# ax.tick_params(axis='both', labelsize=14)
# #ax2.plot(data[550], 'c', lw=2, label='Z = 150 nm')
# #ax2.plot(data[475], 'r', lw=2, label='Z = 75 nm')
# #ax2.plot(data[400], 'b', lw=2, label='Z = 0 nm')
# #ax2.set_xlabel('X Position [nm]', fontsize=16, fontweight='bold')
# #ax2.set_ylabel('Field Data', fontsize=16, fontweight='bold')
# #ax2.set_ylim([7])
# #ax2.set_xticklabels([x])
# #ax2.legend(frameon=True, loc='upper right', prop={'size': 14})

fig, ax = plt.subplots(1, 1)
mycmap1 = plt.get_cmap('gnuplot2')
k = ax.imshow(data, extent=[xmin,xmax,zmin,zmax], cmap=mycmap1)
ax.contour(x, z, data3, colors=('k'))
ax.set_xlabel('X Position [nm]', fontsize=16, fontweight='bold')
ax.set_ylabel('Z Position [nm]', fontsize=16, fontweight='bold')
ax.set_title('TM '+str(lambda1)+' nm (P = '+str(subp)+' nm, \n T = '+str(gratingthickness)+' nm, FF = '+str(dutycycle)+')', fontsize=18, fontweight='bold')
ax.tick_params(axis='both', labelsize=14)

def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

add_colorbar(k)

fig.tight_layout()
# plt.savefig('/Users/samblair/Desktop/802.png')
plt.show()

