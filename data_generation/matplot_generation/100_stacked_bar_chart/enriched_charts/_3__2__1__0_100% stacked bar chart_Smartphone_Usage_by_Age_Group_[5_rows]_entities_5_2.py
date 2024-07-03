
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
running = [20, 25, 15, 10, 10, 5]
swimming = [15, 20, 25, 30, 20, 10]
cycling = [25, 20, 20, 15, 25, 30]
weightlifting = [30, 25, 30, 25, 30, 20]
yoga = [10, 10, 10, 20, 15, 35]

# Stack data
data = np.array([running, swimming, cycling, weightlifting, yoga])
data_cum = data.cumsum(axis=0)

# Bar widths and colors
bar_width = 0.7
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot data
for i, (colname, color) in enumerate(zip(["Running", "Swimming", "Cycling", "Weightlifting", "Yoga"], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(age_groups, widths, left=starts, height=bar_width, label=colname, color=color)

# Add title and labels
ax.set_title('Participation in Sports Activities by Age Group')
ax.set_xlabel('Percentage')
ax.set_ylabel('Age Group')
ax.legend(loc='lower right')

plt.show()