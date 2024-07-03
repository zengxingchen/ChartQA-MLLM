import matplotlib.pyplot as plt
import numpy as np

data = [
    28, 30, 32, 29, 31, 33, 34, 28, 29, 30, 32, 33, 31, 35, 30, 31, 32, 33, 29, 34, 35, 28, 32, 33, 31, 34, 29, 28, 36, 35, 
    30, 31, 36, 29, 28, 37, 32, 28, 30, 35, 33, 36, 34, 32, 29, 31, 34, 30, 33, 35, 28, 31, 34, 29, 32, 33, 28, 30, 32, 31, 
    29, 36, 35, 28, 30, 27, 33, 34, 30, 28, 32, 31, 37, 29, 35, 33, 28, 36, 31, 30, 29, 34, 30, 32, 28, 35, 29, 34, 33, 28, 
    31, 36, 29, 34, 33, 30, 32, 35, 31, 36, 28, 33, 35, 28, 32, 35, 29, 33, 34, 31, 34, 30, 31, 32, 33, 36
]

bin_width = 1
bins = np.arange(min(data), max(data) + bin_width, bin_width)

fig, ax = plt.subplots(figsize=(8, 10))

ax.hist(data, bins=bins, color='#4B0082', edgecolor='#FFFFFF', linewidth=1.5, orientation='horizontal')

ax.set_title('Distribution of Daily Step Counts')
ax.set_xlabel('Frequency')
ax.set_ylabel('Steps in Thousands')

plt.show()