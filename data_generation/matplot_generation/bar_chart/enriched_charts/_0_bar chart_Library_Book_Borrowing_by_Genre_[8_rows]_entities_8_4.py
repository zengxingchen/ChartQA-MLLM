
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "London", "Tokyo", "Sydney",
    "Moscow", "Dubai", "Paris", "Beijing", "Mumbai",
    "Johannesburg", "Rio de Janeiro"
]
temperatures = [
    [-1, 0, 4, 10, 16, 21, 25, 24, 20, 14, 8, 3],
    [14, 15, 15, 17, 18, 20, 22, 22, 21, 19, 16, 14],
    [4, 4, 7, 9, 13, 16, 18, 18, 15, 11, 7, 5],
    [5, 6, 9, 14, 18, 21, 25, 27, 23, 18, 13, 9],
    [23, 23, 22, 19, 16, 13, 11, 12, 14, 17, 19, 21],
    [-9, -8, -4, 5, 13, 17, 19, 17, 11, 5, -2, -7],
    [19, 20, 23, 26, 31, 33, 36, 36, 33, 29, 25, 21],
    [3, 4, 7, 10, 14, 17, 19, 19, 16, 11, 7, 5],
    [-4, -2, 5, 14, 20, 25, 26, 25, 20, 13, 4, -3],
    [24, 24, 27, 29, 30, 29, 28, 28, 28, 28, 27, 25],
    [17, 17, 16, 14, 10, 7, 7, 10, 13, 15, 16, 17],
    [26, 27, 26, 25, 23, 22, 22, 22, 23, 24, 24, 25]
]

# Data for categories (cities) based on mean temperatures
mean_temps = [sum(months) / len(months) for months in temperatures]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 8))

# Horizontal bar chart
bars = ax.barh(cities, mean_temps, color=[
               '#FF5733', '#33FF57', '#3357FF', '#F833FF', '#33FFF8', '#FFC733',
               '#FF3333', '#DAF7A6', '#581845', '#C70039', '#FFC300', '#900C3F'], height=0.5)

# Set the title and labels
ax.set_title('Average Annual Temperature of World Cities (Celsius)', fontsize=15)
ax.set_xlabel('Average Temperature (°C)', fontsize=12)
ax.set_ylabel('City', fontsize=12)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.5
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.1f}',
            va='center')

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()