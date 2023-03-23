import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import os
from os.path import join
from scipy.optimize import least_squares

# set the paths
datapath = '/Volumes/Sam/Dektak/AN_Series/' 
savepath = '/Volumes/Sam/Dektak/AN_Series/'

## define all the functions

def fit_plot_save_step(datapath, f_name, savepath, savename, n_regions=2):
    # load the data
    x,y = load_dektak_data(datapath, f_name)
    x = np.array(x) 
    y = np.array(y) / 10 # convert Angstrom to nm

    # plot and let user select range before and after step for fitting
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.show()
    if n_regions==2:
        g = np.array(plt.ginput(4)).astype(int)
        range_left = g[0:2,0]
        range_right = g[2:4,0]
        range_mid = []
    else:
        g = np.array(plt.ginput(6)).astype(int)
        range_left = g[0:2,0]
        range_mid = g[2:4,0]
        range_right = g[4:6,0]
    
    
    # fitting a quadratic baseline and a step
    par_step = fit_quad_step(x, y, range_left, range_right, range_mid)
    # print('fitting parameters',par_step)
    a, b, c, step = par_step

    # plot data and fitted
    fig, ax = plt.subplots(1,2)
    fig.set_figwidth(8)
    ax[0].plot(x,y, label='data')

    # sort ylim
    y_low = np.min([c-2*step, c+2*step])
    y_high = np.max([c-2*step, c+2*step])
    # ax[0].set_ylim([y_low, y_high])

    # plot baseline
    y_baseline = quadratic(a, b, c, x)
    ax[0].plot(x, y_baseline, label='quadratic baseline')
    ax[0].legend()
    ax[0].set_xlabel('x [um]')
    ax[0].set_ylabel('y [nm]')
    ax[0].set_title(savename)

    # plot background corrected data
    y_corr = y - y_baseline
    ax[1].plot(x, y_corr, label='background corrected data')

    # plot step
    y_step = step*np.ones_like(y)
    ax[1].plot(x, y_step, label=f'step={step:.2f} nm')
    ax[1].plot(x, np.zeros_like(y), ':k')
    ax[1].legend()
    ax[1].set_xlabel('x [um]')
    ax[1].set_ylabel('y [nm]')

    # sort ylim
    y_low = np.min([0-step, 2*step])
    y_high = np.max([0-step, 2*step])
    ax[1].set_ylim([y_low, y_high])

    fig.tight_layout()
    
    # save figure
    fig.savefig( join(savepath, savename) )
    fig.show()

def load_dektak_data(datapath, f_name):
    f = open( join(datapath, f_name), 'r', newline='\n' )
    n_head_rows = 22
    x = []
    y = []
    i_line = 0
    started = False
    for line in f:
        if started:
            x_now, y_now = np.array( line.split(',,')[0].split(',') ).astype(float)
            x.append(x_now)
            y.append(y_now)
        i_line += 1    

        if line.startswith('Lateral'):
            started = True

    f.close()
    return x, y

def find_i(x, x_range):
    i_list = []
    for xr in x_range:
        i_now = np.argmin( np.abs( x - xr ) )
        i_list.append(i_now)
    return i_list

def crop_data(x, y, x_range):
    i_range = find_i(x, x_range)
    x_cr = x[i_range[0]:i_range[1]+1]
    y_cr = y[i_range[0]:i_range[1]+1]
    return x_cr, y_cr

def quadratic(a, b, c, x):
    # return a*x**2 + b*x + c
    return a*(x-b)**2 + c

def res_quad(par, x, y):
    # return np.linalg.norm( quadratic(par[0], par[1], par[2], x) - y )/len(x)
    return quadratic(par[0], par[1], par[2], x) - y

def res_quad_step(par_step, xl, yl, xr, yr):
    par = par_step[0:-1]
    step = par_step[-1]
    res = np.append(res_quad(par, xl, yl), res_quad(par, xr, yr - step))
    return res

def fit_quad(x,y):
    par0 = [0, np.average(x), np.average(y)]
    scales = [1e-3, np.average(x), np.abs(np.average(y))]
    res_lsq = least_squares(res_quad, par0, args=(x, y), x_scale=scales)
    par = res_lsq.x
    return par

def fit_quad_step(x, y, range_left, range_right, range_mid=[]):
    # crop the two selected regions before and after step
    if list(range_mid):
        # if three ranges are given, the first and third are taken as "left"
        xl, yl = crop_data(x, y, range_left)
        xrr, yrr = crop_data(x,y, range_right)
        xl = np.append(xl, xrr)
        yl = np.append(yl, yrr)
        # and the second range becomes "right"
        xr, yr = crop_data(x, y, range_mid)

    else:
        xl, yl = crop_data(x, y, range_left)
        xr, yr = crop_data(x, y, range_right)


    # initial guess (assuming a rising step)
    par0_l = fit_quad(xl, yl)
    par0_r = fit_quad(xr, yr)

    step_est = np.average(yr) - np.average(yl)
    par0 = np.average([par0_l, par0_r], 0)
    par0 = np.append(par0, step_est)
    
    # scales for fit normalisation
    scales = [1e-3, 500, 1, np.abs(step_est)]

    # do the fit
    res_lsq = least_squares(res_quad_step, par0, args=(xl, yl, xr, yr), x_scale=scales)
    par_step = res_lsq.x

    # fig, ax = plt.subplots()
    # ax.plot(xl, yl)
    # ax.plot(xr, yr-par_step[-1])
    # ax.plot(x, quadratic(par_step[0], par_step[1], par_step[2], x))
    # ax.plot(x, quadratic(par0_l[0], par0_l[1], par0_l[2], x))
    # ax.plot(x, quadratic(par0_r[0], par0_r[1], par0_r[2], x))
    # fig.show()
    return par_step

# name of the dektak file
file_name = 'AN3_PostDev_ITOLayer_001.csv'

# name of the plot to save
savename = 'AN3_PostDev_ITOLayer_001.png'

# load, plot and fit the data
fit_plot_save_step(datapath, file_name, savepath, savename, n_regions=2)

plt.show()