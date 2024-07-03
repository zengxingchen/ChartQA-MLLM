
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
running = [15, 20, 25, 20, 10, 10]
swimming = [25, 30, 20, 15, 25, 15]
cycling = [20, 25, 20, 20, 20, 25]
weightlifting = [25, 20, 25, 20, 20, 20]
yoga = [15, 5, 10, 25, 25, 30]

# Stack data
data = np.array([running, swimming, cycling, weightlifting, yoga])
data_cum = data.cumsum(axis=0)

# Bar widths and colors
bar_width = 0.5
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

# Create vertical stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data
for i, (colname, color) in enumerate(zip(["Running", "Swimming", "Cycling", "Weightlifting", "Yoga"], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(age_groups, heights, bottom=starts, width=bar_width, label=colname, color=color)

# Add title and labels
ax.set_title('Engagement in Health & Fitness Activities by Age Group', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()