import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
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

datafilename = '/Volumes/Sam/Lumerical/New/Optimised_Grating/Optical_Buffer_T/200_step_S22_0.645-0.685.txt'
datafilepath = os.path.join(
    root,
    datafilename)
refl = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=3,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/New/Phase_data_test_sweep.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lam, spectrum = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=1,
#     unpack=True)

y_labels = ['0.1', '0.3', '0.5', '0.7', '0.9', '1.1']
x_labels = ['0.645','0.650', '0.655', '0.660', '0.665', '0.670', '0.680', '0.685']

# x = np.linspace(0.50, 0.75, 0.5)
# print(x)

d = []

totalshift = []
diff = []
for y in range(0,100,1):
    c = np.unwrap(refl[y, :], period=np.pi)
    totalshift.append(c[-1]-c[0])
    a = np.diff(c)
    diff.append(np.append(a, 0))
    d.append(c)

s = [(q+np.pi) / np.pi for q in d]

print(totalshift)

fig, ax = plt.subplots()
thickness = np.arange(0.1,1.1,0.01)
ax.plot(thickness, totalshift, lw=3)

# x = np.unwrap(np.flipud(refl[0, :]), period=np.pi)
# x1 = np.unwrap(np.flipud(refl[20, :]), period=np.pi)
# x2 = np.unwrap(np.flipud(refl[40, :]), period=np.pi)
# x3 = np.unwrap(np.flipud(refl[60, :]), period=np.pi)
# x4 = np.unwrap(np.flipud(refl[80, :]), period=np.pi)
# x5 = np.unwrap(np.flipud(refl[99, :]), period=np.pi)
    
# fig, ax = plt.subplots()  
# mycmap1 = plt.get_cmap('turbo')
# k = ax.imshow(np.fliplr(np.flipud(d)), 
#               cmap=mycmap1,aspect='auto')
# cbar = add_colorbar(k)

# x0, y0 = 0, 500
# x1, y1 = 0, 500
# num = 1000
# x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)

# zi = scipy.ndimage.map_coordinates(refl, np.vstack((x,y)))

fig, ax = plt.subplots(figsize=[10,7])
mycmap1 = plt.get_cmap('turbo')
k = ax.imshow(np.fliplr(np.flipud(s)), 
              cmap=mycmap1,
              aspect='auto',
              extent=[0, 350, 0, 100], interpolation='bicubic')
ax.set_xlabel('Wavelength [μm]', fontsize=16, fontweight='bold')
ax.set_ylabel('Metal Layer Thickness [μm]', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', labelsize=14)
cbar = add_colorbar(k)
cbar.ax.set_title('Refl', fontsize=16, fontweight='bold')
cbar.ax.tick_params(labelsize=14)
plt.axvline(x=200, color='k', lw=2, linestyle='--')

ax.set_yticklabels(y_labels)
ax.set_xticklabels(x_labels)

fig, ax = plt.subplots()
k = ax.imshow(np.fliplr(np.flipud(diff)), 
              cmap='gnuplot2',
              aspect='auto',
              extent=[0, 350, 0, 100], interpolation='bicubic')
cbar = add_colorbar(k)

# fig, ax = plt.subplots(figsize=[10,7])
# ax.plot(x,lw=3, label='0')
# ax.plot(x1,lw=3, label='20')
# ax.plot(x2,lw=3, label='40')
# ax.plot(x3,lw=3, label='60')
# ax.plot(x4,lw=3, label='80')
# ax.plot(x5,lw=3, label='99')
# ax.legend(frameon=True, loc=0)
# ax.set_xlabel('lmbda', fontsize=16, fontweight='bold')
# ax.set_ylabel('Phase [rad]', fontsize=16, fontweight='bold')
# ax.tick_params(axis='both', labelsize=14)

plt.tight_layout()
# plt.savefig('/Volumes/Sam/Lumerical/New/Optimised_Grating/Optical_Buffer_T/100_step_Rgn_0.645-0.685.png', dpi=600)
plt.show()