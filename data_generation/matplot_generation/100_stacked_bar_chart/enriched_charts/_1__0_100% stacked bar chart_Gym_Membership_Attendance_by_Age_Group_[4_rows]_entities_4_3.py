
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
exercise = [25, 20, 15, 10, 5, 5]
healthy_diet = [30, 35, 30, 25, 20, 15]
mental_wellness = [20, 25, 30, 35, 40, 40]
sleep = [25, 20, 25, 30, 35, 40]

# Stacked data
data = np.array([exercise, healthy_diet, mental_wellness, sleep])
data_cum = data.cumsum(axis=0)

# Color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Bar width
bar_width = 0.5

# Chart size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
for i, (colname, color) in enumerate(zip(['Exercise', 'Healthy Diet', 'Mental Wellness', 'Sleep'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(age_groups, widths, left=starts, height=bar_width, label=colname, color=color)

# Add labels
ax.set_xlabel('Percentage (%)')
ax.set_title('Health Habits Across Age Groups')
ax.legend(loc='best')

plt.tight_layout()
plt.show()