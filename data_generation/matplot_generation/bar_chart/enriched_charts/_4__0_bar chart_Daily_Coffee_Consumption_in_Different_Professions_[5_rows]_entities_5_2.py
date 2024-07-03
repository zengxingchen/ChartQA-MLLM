
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

average_exercise = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

# Define the colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1a5276', '#ff9a00']

fig, ax = plt.subplots(figsize=(10, 6))

# Create vertical bars
ax.bar(months, average_exercise, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Average Daily Exercise Duration in 2023 (City XYZ)', fontsize=18)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Daily Exercise (minutes)', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(20, max(average_exercise) + 10)

# Show the actual data points on the bars
for i, v in enumerate(average_exercise):
    ax.text(i, v + 1, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()