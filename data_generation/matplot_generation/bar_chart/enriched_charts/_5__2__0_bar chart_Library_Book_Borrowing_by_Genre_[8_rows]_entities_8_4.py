
import matplotlib.pyplot as plt

# Data
countries = [
    "China", "United States", "Brazil", "India", "Germany", "Japan", 
    "Canada", "Spain", "Italy", "United Kingdom", "France", "Australia", 
    "South Korea", "Mexico", "Sweden"
]
renewable_capacity = [
    303.4, 176.3, 150.2, 134.5, 120.7, 107.1, 98.9, 91.3, 83.2, 77.4, 69.8, 
    62.5, 55.1, 49.3, 43.9
]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(14, 10))

# Horizontal bar chart
bars = ax.barh(countries, renewable_capacity, color=[
    '#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22',
    '#1abc9c', '#34495e', '#d35400', '#7f8c8d', '#27ae60', '#8e44ad',
    '#c0392b', '#2980b9', '#16a085'], height=0.5)

# Set the title and labels
ax.set_title('Top 15 Countries by Renewable Energy Capacity in 2023 (GW)', fontsize=18)
ax.set_xlabel('Renewable Energy Capacity (GW)', fontsize=14)
ax.set_ylabel('Country', fontsize=14)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Set y-axis limit
ax.set_xlim(40, 320)

# Show Values on Bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 5
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', va='center')

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()