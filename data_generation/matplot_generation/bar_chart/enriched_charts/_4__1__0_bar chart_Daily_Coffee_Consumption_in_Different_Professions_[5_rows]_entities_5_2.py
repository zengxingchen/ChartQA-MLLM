
import matplotlib.pyplot as plt

# Data for plotting
categories = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'TikTok', 'YouTube']
values = [1200, 1500, 1300, 1600, 1800, 2000, 1700]

# Define the colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
ax.barh(categories, values, color=colors, edgecolor='black', height=0.6)

# Set chart title and labels
ax.set_title('Daily Active Users on Social Media Platforms (in millions)', fontsize=18, pad=20)
ax.set_xlabel('Number of Users (in millions)', fontsize=14)
ax.set_ylabel('Social Media Platform', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(1000, max(values) + 500)

# Show the actual data points on the bars
for i, v in enumerate(values):
    ax.text(v + 50, i, str(v), color='black', va='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off y ticks for cleaner look
ax.yaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()