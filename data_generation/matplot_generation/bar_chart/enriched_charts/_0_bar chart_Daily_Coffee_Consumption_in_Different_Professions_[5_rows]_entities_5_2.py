
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

average_temperatures = [5, 6, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]

# Define the colors for each bar
colors = ['#FF5733', '#FF7D33', '#FFA133', '#FFC533', '#FFE633',
          '#BFFF33', '#8FFF33', '#6AFF33', '#33FF57', '#33FF8E',
          '#33FFFF', '#3378FF']

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
ax.barh(months, average_temperatures, color=colors, edgecolor='black', height=0.7)

# Set chart title and labels
ax.set_title('Average Monthly Temperatures in City XYZ', fontsize=18)
ax.set_xlabel('Average Temperature (°C)', fontsize=14)
ax.set_ylabel('Month', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(0, max(average_temperatures) + 5)

# Show the actual data points on the bars
for i, v in enumerate(average_temperatures):
    ax.text(v + 0.5, i, str(v), color='black', va='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Turn off y ticks for cleaner look
ax.yaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()