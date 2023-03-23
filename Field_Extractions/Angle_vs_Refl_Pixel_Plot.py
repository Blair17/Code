import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
import scipy.ndimage
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1

theta_min = 1
theta_max = 15

root = os.getcwd()

datafile = '/Volumes/Sam/Sputterer_PC/Opto_Mech_Paper/Shrink_Testing/Pixel_Data/1_15_theta_vs_spectrum.csv'
x = np.arange(1, 15, 1)
data = np.genfromtxt(datafile, delimiter=',')
data1 = data * 100

fig, ax = plt.subplots(1, 1)
mycmap1 = plt.get_cmap('gnuplot2')
k = ax.imshow(data, extent=[theta_min,theta_max,0,10], cmap=mycmap1)
ax.set_xlabel('θ', fontsize=16, fontweight='bold')
ax.set_ylabel('Wavelength', fontsize=16, fontweight='bold')
x_ticks = ['1530','1540','1550','1560','1570','1580']
ax.set_yticklabels(x_ticks)
ax.tick_params(axis='both', labelsize=14)
plt.title('Original Structure \n Si-Air-Glass Grating', fontsize=16, fontweight='bold')

def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot"""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

add_colorbar(k)

fig.tight_layout()
plt.show()

