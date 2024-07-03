
import matplotlib.pyplot as plt

# Data for plotting
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
distances = [3200, 4500, 3600, 4100, 4900, 5600, 4800]

# Define the colors for each bar
colors = ['#4B0082', '#FF4500', '#32CD32', '#FFD700', '#1E90FF', '#FF69B4', '#8B4513']

fig, ax = plt.subplots(figsize=(10, 6))

# Create vertical bars
ax.bar(days, distances, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Weekly Running Distance', fontsize=18, pad=20)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Distance (meters)', fontsize=14)

# Set the limits for the y-axis to start from a specific value other than zero
ax.set_ylim(2000, max(distances) + 1000)

# Show the actual data points on the bars
for i, v in enumerate(distances):
    ax.text(i, v + 100, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()