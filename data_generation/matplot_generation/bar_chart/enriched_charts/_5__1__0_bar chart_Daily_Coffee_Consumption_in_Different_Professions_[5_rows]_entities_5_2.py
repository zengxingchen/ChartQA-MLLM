
import matplotlib.pyplot as plt

# Data for plotting
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calories = [2200, 2500, 2300, 2600, 2800, 3000, 2700]

# Define the colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF6', '#D333FF', '#FFDD33']

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
ax.barh(days, calories, color=colors, edgecolor='black', height=0.5)

# Set chart title and labels
ax.set_title('Calories Burned Per Day', fontsize=20, pad=20)
ax.set_xlabel('Calories', fontsize=14)
ax.set_ylabel('Day', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(min(calories) - 500, max(calories) + 500)

# Show the actual data points on the bars
for i, v in enumerate(calories):
    ax.text(v + 100, i, str(v), color='black', va='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off y ticks for cleaner look
ax.yaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()