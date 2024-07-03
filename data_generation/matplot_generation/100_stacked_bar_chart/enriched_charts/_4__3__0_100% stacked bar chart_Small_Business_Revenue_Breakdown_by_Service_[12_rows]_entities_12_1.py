
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Solar Power', 'Wind Energy', 'Hydropower', 'Geothermal Energy', 'Nuclear Energy', 
              'Bioenergy', 'Wave and Tidal', 'Smart Grids', 'Energy Storage', 'Electric Vehicles', 
              'Energy Efficiency', 'Carbon Capture']
usa = [25, 35, 20, 10, 10, 25, 5, 30, 15, 25, 35, 10]
uk = [30, 25, 20, 15, 10, 30, 5, 25, 20, 30, 30, 15]
canada = [20, 30, 25, 20, 5, 25, 10, 35, 25, 30, 25, 20]
germany = [40, 35, 15, 5, 5, 15, 5, 20, 10, 25, 35, 5]
japan = [35, 25, 30, 10, 0, 20, 5, 25, 15, 35, 30, 10]

# Create plot
fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.7
bar_positions = np.arange(len(categories))

ax.bar(bar_positions, usa, color='#1f77b4', edgecolor='grey', width=bar_width, label='USA')
ax.bar(bar_positions, uk, bottom=usa, color='#ff7f0e', edgecolor='grey', width=bar_width, label='UK')
ax.bar(bar_positions, canada, bottom=np.array(usa) + np.array(uk), color='#2ca02c', edgecolor='grey', width=bar_width, label='Canada')
ax.bar(bar_positions, germany, bottom=np.array(usa) + np.array(uk) + np.array(canada), color='#d62728', edgecolor='grey', width=bar_width, label='Germany')
ax.bar(bar_positions, japan, bottom=np.array(usa) + np.array(uk) + np.array(canada) + np.array(germany), color='#9467bd', edgecolor='grey', width=bar_width, label='Japan')

# Labeling
ax.set_xticks(bar_positions)
ax.set_xticklabels(categories, rotation=90)
ax.set_ylabel('Percentage')
ax.set_title('Energy Sources by Country')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()