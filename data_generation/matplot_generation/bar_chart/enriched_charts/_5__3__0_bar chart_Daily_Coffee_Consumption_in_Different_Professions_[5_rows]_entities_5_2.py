
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
total_calories = [2200, 1800, 2000, 2500, 2700, 3000, 3200, 3100, 2900, 2800, 2600, 2400]

# Define the colors for each bar
colors = ['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#7FFF00', 
          '#32CD32', '#00FA9A', '#00CED1', '#1E90FF', '#4169E1', 
          '#8A2BE2', '#DA70D6']

fig, ax = plt.subplots(figsize=(14, 10))

# Create horizontal bars
ax.barh(months, total_calories, color=colors, edgecolor='black', height=0.6)

# Set chart title and labels
ax.set_title('Monthly Average Caloric Intake in City XYZ', fontsize=18, pad=20)
ax.set_xlabel('Total Calories', fontsize=14)
ax.set_ylabel('Month', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(min(total_calories) - 200, max(total_calories) + 200)

# Show the actual data points on the bars
for i, v in enumerate(total_calories):
    ax.text(v + 50, i, str(v), color='black', va='center', fontsize=12)

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