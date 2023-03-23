import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

def loadData(datafile, plot=False):
    with open(datafile, 'r') as f:
        all_data = f.read()

    all_data = all_data.split('\n\n\n')

    lateral, profile, _, _ = np.genfromtxt(
                StringIO(all_data[-1]), 
                delimiter=',', 
                skip_header=2, 
                unpack=True)

    if plot:
        fig, ax = plt.subplots(1, 1, figsize=(12, 6))
        ax.plot(lateral, profile)
        #plt.savefig('/Volumes/Sam/DekTak/C_Series/C8/C8a/Si_ITO_C8a_Depth_Comparison.png')
    
    return lateral, profile

if __name__ == '__main__':
    datafile = '/Volumes/Sam/DekTak/E_Series/Glass_ITO_Depth_Measurement_E_Series.csv'
    _, _ = loadData(datafile, plot=True)

