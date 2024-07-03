
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
soccer = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
basketball = [60, 55, 70, 65, 75, 80, 85, 90, 95, 100, 105, 110]
tennis = [70, 65, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
bar_width = 0.2
bar_locations_soccer = range(len(soccer))
bar_locations_basketball = [x + bar_width for x in bar_locations_soccer]
bar_locations_tennis = [x + bar_width for x in bar_locations_basketball]

bars1 = ax.bar(bar_locations_soccer, soccer, bar_width, label='Soccer', color='#1f77b4')
bars2 = ax.bar(bar_locations_basketball, basketball, bar_width, label='Basketball', color='#ff7f0e')
bars3 = ax.bar(bar_locations_tennis, tennis, bar_width, label='Tennis', color='#2ca02c')

# Set the position of the x ticks
ax.set_xticks([r + bar_width for r in range(len(soccer))])
ax.set_xticklabels(months)

# Adding labels and title
plt.ylabel('Number of Participants')
plt.title('Monthly Participation in Sports Activities')
ax.legend()

# Set y-axis limits
ax.set_ylim(50, 140)

# Display the plot
plt.tight_layout()
plt.show()