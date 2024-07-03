
import matplotlib.pyplot as plt
import numpy as np

data = [
    6.5, 7, 7.2, 8, 6.8, 7.5, 8.2, 9, 6.9, 7.1, 8.5, 7.4, 6.7, 8.8, 7.8, 8.3, 7.6, 6.6, 7.9, 8.4, 7.3, 6.5, 7.7, 9.1, 
    6.4, 8.6, 7.2, 6.3, 9.3, 8.7, 6.9, 7.0, 8.9, 7.1, 6.2, 9.4, 7.3, 6.4, 7.2, 8.0, 7.5, 9.0, 8.1, 7.6, 6.8, 7.8, 8.4, 
    6.7, 7.9, 8.5, 6.6, 7.3, 8.2, 6.5, 7.4, 8.1, 7.0, 6.9, 9.2, 8.3, 6.3, 7.1, 6.2, 7.8, 8.0, 7.5, 6.8, 7.6, 9.5, 6.4, 
    8.7, 7.7, 6.5, 8.8, 7.4, 6.9, 7.2, 8.6, 7.0, 8.1, 7.3, 9.1, 6.2, 8.4, 7.8, 6.7, 7.9, 9.0, 6.6, 8.2, 7.5, 6.8, 7.6, 
    9.3, 7.1, 8.9, 6.5, 7.7, 8.5, 6.4, 7.2, 8.0, 7.4, 8.3, 7.9, 6.3, 7.0, 6.9, 8.8
]

bin_width = 0.5
bins = np.arange(min(data), max(data) + bin_width, bin_width)

fig, ax = plt.subplots(figsize=(10, 8))

ax.hist(data, bins=bins, color='#FF6347', edgecolor='#000000', linewidth=1.2)

ax.set_title('Distribution of Hours of Sleep per Night')
ax.set_xlabel('Hours of Sleep')
ax.set_ylabel('Frequency')

plt.show()