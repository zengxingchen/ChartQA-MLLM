
import matplotlib.pyplot as plt

# Data for plotting
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [3400, 4200, 3100, 4700, 5300, 5900, 4900]

# Define the colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
ax.barh(days, sales, color=colors, edgecolor='black', height=0.4)

# Set chart title and labels
ax.set_title('Weekly Sales Data', fontsize=18, pad=20)
ax.set_xlabel('Number of Sales', fontsize=14)
ax.set_ylabel('Day', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(0, max(sales) + 1000)

# Show the actual data points on the bars
for i, v in enumerate(sales):
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