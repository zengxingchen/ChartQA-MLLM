
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

total_precipitation = [50, 40, 55, 65, 80, 90, 100, 95, 85, 75, 60, 50]

# Define the colors for each bar
colors = ['#4682B4', '#5F9EA0', '#6495ED', '#00CED1', '#20B2AA',
          '#3CB371', '#2E8B57', '#66CDAA', '#8FBC8F', '#32CD32',
          '#9ACD32', '#ADFF2F']

fig, ax = plt.subplots(figsize=(10, 14))

# Create vertical bars
ax.bar(months, total_precipitation, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Monthly Precipitation in City XYZ', fontsize=18)
ax.set_ylabel('Total Precipitation (mm)', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(0, max(total_precipitation) + 20)

# Show the actual data points on the bars
for i, v in enumerate(total_precipitation):
    ax.text(i, v + 2, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()