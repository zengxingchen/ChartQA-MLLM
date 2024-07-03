
import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'Canada', 'Australia', 'Germany', 'France', 'Brazil', 'India', 'China', 'South Africa', 'Japan']
adventure = [20, 25, 30, 15, 10, 20, 25, 20, 30, 15]
relaxation = [30, 20, 25, 30, 35, 25, 20, 25, 15, 30]
sightseeing = [25, 30, 15, 20, 25, 30, 15, 25, 20, 20]
cultural = [15, 15, 20, 25, 20, 15, 30, 20, 25, 25]
wildlife = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.6  # width of the bars

# Colors
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#1E90FF', '#8A2BE2']

# Stacked bar chart
ax.barh(countries, adventure, color=colors[0], edgecolor='white', height=width)
ax.barh(countries, relaxation, left=np.array(adventure), color=colors[1], edgecolor='white', height=width)
ax.barh(countries, sightseeing, left=np.array(adventure)+np.array(relaxation), color=colors[2], edgecolor='white', height=width)
ax.barh(countries, cultural, left=np.array(adventure)+np.array(relaxation)+np.array(sightseeing), color=colors[3], edgecolor='white', height=width)
ax.barh(countries, wildlife, left=np.array(adventure)+np.array(relaxation)+np.array(sightseeing)+np.array(cultural), color=colors[4], edgecolor='white', height=width)

# Title and labels
ax.set_title('Percentage Distribution of Travel Activities by Country', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Country')

# Legend
ax.legend(['Adventure', 'Relaxation', 'Sightseeing', 'Cultural', 'Wildlife'], loc='upper right', bbox_to_anchor=(1.15, 1))

# Show plot
plt.tight_layout()
plt.show()