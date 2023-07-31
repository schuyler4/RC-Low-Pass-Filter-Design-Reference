#
# FILENAME: RC.py
#
# DESCRIPTION: This script generates a table and and a plot that may be useful for RC low pass filter design.
#
# Written by: Marek Newton
#

import numpy as np
from matplotlib import pyplot as plt, ticker

decimal_places = 1

# Generate a vector of logarithmically spaced time values.
tau = np.logspace(-9, 1, 11, base=10)

# Create a numpy array of the cut off frequency values and the time constant.
frequencies = 1/(2*np.pi*tau)

# Calculation correctness check. 
assert np.isclose(frequencies[0], 159.1549431e6), 'The nanosecond time constant is incorrect.'
assert np.isclose(frequencies[6], 159.1549431), 'The millisecond time constant is incorrect.'
assert np.isclose(frequencies[frequencies.size-2], 0.1591549431), 'The second time constant is incorrect.'
assert np.isclose(frequencies[frequencies.size-1], 0.0159154943), 'The ten second time constant is incorrect.'

table_column_labels = ('Time Constant (s)', 'Cutoff Frequency (Hz)')
table_matrix = np.array([tau, frequencies])

def format_float(my_float):
    return np.format_float_scientific(my_float, precision=decimal_places, unique=False, trim='k')

# The float formatting correctness check.
assert format_float(1.23456789e-9) == '1.2e-09', 'The format_float function is incorrect.'

format_float_matrix = np.vectorize(format_float)

table_matrix = format_float_matrix(table_matrix.T)

fig, axs = plt.subplots(2, 1)
fig.set_figheight(10)

axs[0].axis('off')
axs[0].table(table_matrix, loc='center', colLabels=table_column_labels, colLoc='center', cellLoc='center')

axs[1].plot(tau, frequencies)
axs[1].height_ratios = [1, 1]
axs[1].set_xlabel('Time Constant (s)')
axs[1].set_title('Cutoff Frequency (Hz) vs. Time Constant (s)')
axs[1].set_ylabel('Cutoff Frequency (Hz)')
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].xaxis.set_major_locator(ticker.LogLocator(numticks=100))
axs[1].xaxis.set_minor_locator(ticker.LogLocator(numticks=100, subs='auto'))
axs[1].yaxis.set_major_locator(ticker.LogLocator(numticks=100))
axs[1].yaxis.set_minor_locator(ticker.LogLocator(numticks=100, subs='auto'))
axs[1].grid(which='both', color='grey', linestyle='-', linewidth=0.1)

fig.suptitle('RC Low Pass Filter Reference', fontsize=16, fontweight='bold')


# Export a PDF file and a PNG file.
plt.savefig('RC.pdf')
plt.savefig('RC.png', dpi=300)