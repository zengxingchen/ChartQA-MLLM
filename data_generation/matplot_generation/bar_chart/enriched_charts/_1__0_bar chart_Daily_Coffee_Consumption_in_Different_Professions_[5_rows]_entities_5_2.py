
import matplotlib.pyplot as plt

# Data for plotting
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = [12000, 15000, 13000, 16000, 18000, 20000, 17000]

# Define the colors for each bar
colors = ['#5D3FD3', '#FF5733', '#33FF57', '#FF33A8', '#33FFF6', '#D333FF', '#FFDD33']

fig, ax = plt.subplots(figsize=(10, 6))

# Create vertical bars
ax.bar(days, steps, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Daily Step Count in Week', fontsize=18, pad=20)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Number of Steps', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(0, max(steps) + 5000)

# Show the actual data points on the bars
for i, v in enumerate(steps):
    ax.text(i, v + 500, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()