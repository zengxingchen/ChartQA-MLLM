import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
classical = [10, 15, 20, 25, 30, 15, 10]
rock = [20, 25, 15, 30, 10, 20, 30]
jazz = [30, 20, 25, 10, 15, 25, 20]
hip_hop = [15, 30, 10, 20, 25, 30, 15]
pop = [25, 10, 30, 15, 20, 10, 25]

# Stacked Bar Chart
barWidth = 0.6
bars = np.arange(len(categories))

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(bars, classical, color=colors[0], edgecolor='white', height=barWidth, label='Classical')
ax.barh(bars, rock, left=classical, color=colors[1], edgecolor='white', height=barWidth, label='Rock')
ax.barh(bars, jazz, left=np.add(classical, rock), color=colors[2], edgecolor='white', height=barWidth, label='Jazz')
ax.barh(bars, hip_hop, left=np.add(np.add(classical, rock), jazz), color=colors[3], edgecolor='white', height=barWidth, label='Hip-Hop')
ax.barh(bars, pop, left=np.add(np.add(np.add(classical, rock), jazz), hip_hop), color=colors[4], edgecolor='white', height=barWidth, label='Pop')

# Add labels
ax.set_xlabel('Percentage')
ax.set_title('Weekly Music Genre Preference', pad=20)
ax.set_yticks(bars)
ax.set_yticklabels(categories)
ax.legend(loc='lower right', bbox_to_anchor=(1.1, 0.5))

plt.show()