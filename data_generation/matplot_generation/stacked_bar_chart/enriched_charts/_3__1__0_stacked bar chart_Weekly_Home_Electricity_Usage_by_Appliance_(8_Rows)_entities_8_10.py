
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Canada', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'Australia', 'South Africa']
classical = [120, 100, 130, 110, 125, 115, 130, 105, 110, 115]
rock = [150, 140, 160, 130, 135, 125, 145, 120, 130, 135]
jazz = [110, 105, 115, 100, 110, 105, 120, 95, 100, 105]
hip_hop = [130, 120, 140, 115, 120, 110, 130, 100, 115, 120]
electronic = [140, 135, 150, 125, 130, 120, 135, 115, 125, 130]

# Colors for each genre
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Figure size
plt.figure(figsize=(14, 8))

# Bar widths
bar_height = 0.5

# Plotting
plt.barh(countries, classical, color=colors[0], edgecolor='white', height=bar_height, label='Classical')
plt.barh(countries, rock, left=classical, color=colors[1], edgecolor='white', height=bar_height, label='Rock')
plt.barh(countries, jazz, left=[classical[i] + rock[i] for i in range(len(jazz))], color=colors[2], edgecolor='white', height=bar_height, label='Jazz')
plt.barh(countries, hip_hop, left=[classical[i] + rock[i] + jazz[i] for i in range(len(hip_hop))], color=colors[3], edgecolor='white', height=bar_height, label='Hip-Hop')
plt.barh(countries, electronic, left=[classical[i] + rock[i] + jazz[i] + hip_hop[i] for i in range(len(electronic))], color=colors[4], edgecolor='white', height=bar_height, label='Electronic')

# Labels and Title
plt.xlabel('Music Genre Popularity (thousands)')
plt.title('Popularity of Different Music Genres by Country', pad=20)
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()