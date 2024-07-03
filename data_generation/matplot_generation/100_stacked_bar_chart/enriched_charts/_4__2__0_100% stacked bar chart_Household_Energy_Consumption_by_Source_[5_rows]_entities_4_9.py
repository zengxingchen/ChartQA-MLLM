
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
classical = [12, 18, 20, 25, 30, 10, 15]
rock = [20, 22, 18, 28, 10, 30, 25]
jazz = [28, 20, 22, 15, 25, 20, 18]
hip_hop = [15, 25, 20, 20, 15, 25, 28]
pop = [25, 15, 20, 12, 20, 15, 14]

# Stacked Bar Chart
barWidth = 0.8
bars = np.arange(len(categories))

# Colors
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 9))

ax.bar(bars, classical, color=colors[0], edgecolor='white', width=barWidth, label='Classical')
ax.bar(bars, rock, bottom=classical, color=colors[1], edgecolor='white', width=barWidth, label='Rock')
ax.bar(bars, jazz, bottom=np.add(classical, rock), color=colors[2], edgecolor='white', width=barWidth, label='Jazz')
ax.bar(bars, hip_hop, bottom=np.add(np.add(classical, rock), jazz), color=colors[3], edgecolor='white', width=barWidth, label='Hip-Hop')
ax.bar(bars, pop, bottom=np.add(np.add(np.add(classical, rock), jazz), hip_hop), color=colors[4], edgecolor='white', width=barWidth, label='Pop')

# Add labels
ax.set_ylabel('Percentage')
ax.set_title('Weekly Music Genre Preference', pad=20)
ax.set_xticks(bars)
ax.set_xticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.show()