
import matplotlib.pyplot as plt

# Data
cities = [
    "San Francisco", "Seattle", "New York", "Los Angeles", "Miami",
    "Houston", "Denver", "Phoenix", "Chicago", "Atlanta",
    "Boston", "Las Vegas"
]
solar_power = [
    153, 97, 145, 270, 315,
    190, 212, 310, 132, 180,
    120, 335
]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(12, 10))

# Horizontal bar chart
bars = ax.barh(cities, solar_power, color=[
               '#FF5733', '#33FF57', '#3357FF', '#F833FF', '#33FFF8', '#FFC733',
               '#FF3333', '#DAF7A6', '#581845', '#C70039', '#FFC300', '#900C3F'], height=0.6)

# Set the title and labels
ax.set_title('Total Solar Power Generation in Major US Cities (MWh)', fontsize=16)
ax.set_xlabel('Total Solar Power (MWh)', fontsize=13)
ax.set_ylabel('City', fontsize=13)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 5
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}',
            va='center')

# Set the layout to be tight
plt.tight_layout()

# Set y-axis limits
ax.set_xlim(90, 350)

# Show the plot
plt.show()