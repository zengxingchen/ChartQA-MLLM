
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
iron = np.array([5, 0, 35, 0, 63, 50, 35, 45])
silicon = np.array([10, 15, 30, 18, 12, 20, 23, 22])
oxygen = np.array([85, 85, 35, 82, 25, 30, 42, 33])

# Normalize the data
total = iron + silicon + oxygen
iron_percent = iron / total * 100
silicon_percent = silicon / total * 100
oxygen_percent = oxygen / total * 100

# Stack data
data = [iron_percent, silicon_percent, oxygen_percent]
labels = ['Iron', 'Silicon', 'Oxygen']
colors = ['#d32f2f','#f57c00','#388e3c']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.6  # bar width

# Create stacked bar chart
ax.bar(categories, iron_percent, color=colors[0], edgecolor='white', width=width)
ax.bar(categories, silicon_percent, bottom=iron_percent, color=colors[1], edgecolor='white', width=width)
ax.bar(categories, oxygen_percent, bottom=iron_percent + silicon_percent, color=colors[2], edgecolor='white', width=width)

# Adding title and labels
ax.set_title('Composition of Planets in the Solar System', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xlabel('Planets', fontsize=12)

# Adding legend
ax.legend(labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()