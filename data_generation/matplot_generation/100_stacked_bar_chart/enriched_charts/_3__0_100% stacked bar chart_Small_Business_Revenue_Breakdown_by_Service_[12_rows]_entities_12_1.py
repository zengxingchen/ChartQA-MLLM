import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Renewable Energy', 'Waste Management', 'Water Conservation', 'Green Transportation', 'Sustainable Agriculture', 
              'Air Quality Improvement', 'Energy Efficiency', 'Biodiversity Protection', 'Climate Education', 'Recycling Programs']
urban = [35, 25, 40, 20, 45, 30, 50, 25, 40, 30]
suburban = [45, 50, 30, 55, 35, 40, 30, 35, 20, 50]
rural = [20, 25, 30, 25, 20, 30, 20, 40, 40, 20]

# Create plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
bar_positions = np.arange(len(categories))

ax.barh(bar_positions, urban, color='#1f77b4', edgecolor='grey', height=bar_width, label='Urban')
ax.barh(bar_positions, suburban, left=urban, color='#ff7f0e', edgecolor='grey', height=bar_width, label='Suburban')
ax.barh(bar_positions, rural, left=np.array(urban) + np.array(suburban), color='#2ca02c', edgecolor='grey', height=bar_width, label='Rural')

# Labeling
ax.set_yticks(bar_positions)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage')
ax.set_title('Environmental Initiatives by Region')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()