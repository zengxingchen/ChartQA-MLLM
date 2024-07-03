import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['2018', '2019', '2020', '2021', '2022', '2023']
streaming_services = [15, 20, 25, 30, 35, 40]
tv_cable = [35, 30, 25, 20, 15, 10]
music_podcasts = [25, 30, 35, 40, 45, 50]
gaming = [25, 20, 15, 10, 5, 0]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create the vertical stacked bar chart
width = 0.5
ax.bar(labels, streaming_services, color=colors[0], edgecolor='white', label='Streaming Services', width=width)
ax.bar(labels, tv_cable, bottom=streaming_services, color=colors[1], edgecolor='white', label='TV & Cable', width=width)
ax.bar(labels, music_podcasts, bottom=np.add(streaming_services, tv_cable), color=colors[2], edgecolor='white', label='Music & Podcasts', width=width)
ax.bar(labels, gaming, bottom=np.add(np.add(streaming_services, tv_cable), music_podcasts), color=colors[3], edgecolor='white', label='Gaming', width=width)

# Add title and labels
ax.set_title('Entertainment Consumption Trends (2018-2023)', loc='center', fontsize=16, pad=20)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Years')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Show plot
plt.tight_layout()
plt.show()