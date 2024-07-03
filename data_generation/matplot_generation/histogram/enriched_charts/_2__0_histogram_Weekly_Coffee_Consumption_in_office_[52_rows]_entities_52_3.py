
import matplotlib.pyplot as plt
import numpy as np

data = [2.5, 3.1, 3.0, 4.2, 2.8, 5.5, 6.3, 4.8, 4.1, 3.6, 2.7, 4.3, 5.2, 5.0, 4.9, 3.7, 3.3, 4.0, 4.5, 5.7, 6.2, 5.8, 6.1, 4.4, 4.6, 3.8, 3.2, 3.5, 2.6, 3.9, 5.4, 6.0, 5.6, 4.7, 3.4, 5.1, 2.9, 5.9, 6.4, 6.5]

bin_width = 0.5
bins = np.arange(min(data), max(data) + bin_width, bin_width)

fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(data, bins=bins, orientation='vertical', color='#ff7f0e', edgecolor='#1f77b4', linewidth=1.2)

ax.set_title('Distribution of Distances Walked')
ax.set_ylabel('Frequency')
ax.set_xlabel('Distance (km)')

plt.show()