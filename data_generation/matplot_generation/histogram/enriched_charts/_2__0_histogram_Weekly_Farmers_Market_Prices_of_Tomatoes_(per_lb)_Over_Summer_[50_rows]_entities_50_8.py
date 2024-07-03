import matplotlib.pyplot as plt
import numpy as np

heights = np.array([
    170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 
    190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 
    210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 
    230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250
])

bin_width = 5
bins = np.arange(min(heights) - bin_width/2, max(heights) + bin_width/2, bin_width)

fig, ax = plt.subplots(figsize=(10, 12))
ax.hist(heights, bins=bins, color='#4A90E2', rwidth=0.75)

plt.title('Distribution of Heights of a Population', fontsize=18, pad=20)
plt.ylabel('Frequency', fontsize=14)
plt.xlabel('Height (cm)', fontsize=14)

plt.grid(True, linestyle='--', linewidth=0.5, color='#BBBBBB')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()