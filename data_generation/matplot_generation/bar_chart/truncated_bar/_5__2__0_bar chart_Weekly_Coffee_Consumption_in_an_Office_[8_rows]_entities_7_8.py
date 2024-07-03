
import matplotlib.pyplot as plt

# Data for plotting
destinations = [
    "Bali", "Swiss Alps", "New Zealand", "Iceland", "Patagonia",
    "Canadian Rockies", "Costa Rica", "Himalayas", "Alaska",
    "Kenya", "Australia", "Galapagos"
]
activities = [8, 10, 12, 9, 11, 10, 7, 13, 9, 10, 8, 12]
costs = [2500, 3000, 4000, 3500, 3200, 2800, 2200, 5000, 3800, 3400, 3100, 4500]

fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart with custom colors and bar heights
bars = ax.barh(destinations, activities, height=0.6,
               color=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF3',
                      '#8D33FF', '#FF8D33', '#33FF8D', '#FF5733', '#33A6FF',
                      '#A6FF33', '#FF338D'])

# Set the chart title and labels
ax.set_title('Top Adventure Travel Destinations', fontsize=18)
ax.set_xlabel('Number of Adventure Activities', fontsize=14)
ax.set_ylabel('Destinations', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Add value labels to each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.5  # Some padding to the right
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}',
            va='center', ha='left', fontsize=12)

# Set y-axis limits
ax.set_xlim([5, 15])

plt.tight_layout()
plt.show()