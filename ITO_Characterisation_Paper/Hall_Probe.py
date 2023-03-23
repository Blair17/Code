import os
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()

datafilename = '/Users/samblair/Desktop/2023.01.10_ITOHallEffectMeasurement/AA4/20230110_AA4_0.5mA_#1.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
freqs_R1, n_R1, eps_R1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)