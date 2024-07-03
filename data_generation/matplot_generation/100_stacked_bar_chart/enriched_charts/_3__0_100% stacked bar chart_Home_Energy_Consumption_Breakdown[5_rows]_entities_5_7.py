
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Paris', 'Tokyo', 'Sydney', 'New York', 'Cape Town', 'Barcelona', 'Dubai', 'Istanbul', 'Rio de Janeiro', 'Marrakesh']
backpackers = [20, 25, 15, 30, 10, 25, 15, 20, 30, 10]
family_travelers = [30, 35, 25, 20, 30, 25, 35, 30, 25, 20]
luxury_travelers = [25, 20, 30, 35, 30, 25, 40, 30, 20, 40]
adventure_seekers = [25, 20, 30, 15, 30, 25, 10, 20, 25, 30]

# Colors
colors = ['#FF5733', '#33FFBD', '#335BFF', '#FF33A1']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Create the horizontal stacked bar chart
width = 0.5
ax.barh(labels, backpackers, color=colors[0], edgecolor='white', label='Backpackers', height=width)
ax.barh(labels, family_travelers, left=backpackers, color=colors[1], edgecolor='white', label='Family Travelers', height=width)
ax.barh(labels, luxury_travelers, left=np.add(backpackers, family_travelers), color=colors[2], edgecolor='white', label='Luxury Travelers', height=width)
ax.barh(labels, adventure_seekers, left=np.add(np.add(backpackers, family_travelers), luxury_travelers), color=colors[3], edgecolor='white', label='Adventure Seekers', height=width)

# Add title and labels
ax.set_title('Types of Travelers Across Destinations', loc='center', fontsize=16, pad=20)
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Destinations')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Show plot
plt.tight_layout()
plt.show()