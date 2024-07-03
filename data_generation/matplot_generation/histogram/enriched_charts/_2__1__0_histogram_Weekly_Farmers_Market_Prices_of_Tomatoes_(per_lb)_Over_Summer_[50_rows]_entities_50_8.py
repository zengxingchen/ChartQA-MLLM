
import matplotlib.pyplot as plt
import numpy as np

travel_time = np.array([
    8, 10, 15, 9, 14, 18, 21, 16, 22, 27, 24, 19, 15, 11, 17, 23, 26, 20, 28, 32, 
    31, 29, 25, 21, 18, 16, 13, 12, 14, 17, 19, 22, 26, 30, 33, 29, 25, 21, 20, 15,
    13, 18, 24, 27, 31, 28, 25, 23, 19, 16, 12, 10, 8, 9, 11, 13, 17, 20, 23, 26, 
    29, 33, 35, 37, 31, 27, 24, 20, 18, 15, 13, 11, 9, 14, 17, 20, 23, 27, 30, 33, 
    36, 32, 28, 24, 21, 17, 14, 12, 10, 8
])

bin_width = 2
bins = np.arange(min(travel_time) - bin_width/2, max(travel_time) + bin_width/2, bin_width)

fig, ax = plt.subplots(figsize=(14, 8))
ax.hist(travel_time, bins=bins, orientation='horizontal', color='#FF5733', rwidth=0.6)

plt.title('Distribution of Daily Travel Time (Minutes)', fontsize=16, pad=20)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Travel Time (Minutes)', fontsize=14)

plt.grid(True, linestyle='--', linewidth=0.5, color='#aaaaaa')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()