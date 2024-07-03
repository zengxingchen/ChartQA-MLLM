
import matplotlib.pyplot as plt

# Data from the given table
data = [
    {'Month': 'January', 'Paper': 3200, 'Plastic': 2800, 'Glass': 1500, 'Metal': 900, 'Electronics': 100},
    {'Month': 'February', 'Paper': 3100, 'Plastic': 2900, 'Glass': 1600, 'Metal': 850, 'Electronics': 90},
    {'Month': 'March', 'Paper': 3300, 'Plastic': 3000, 'Glass': 1650, 'Metal': 950, 'Electronics': 120},
    {'Month': 'April', 'Paper': 3400, 'Plastic': 3100, 'Glass': 1700, 'Metal': 970, 'Electronics': 130},
    {'Month': 'May', 'Paper': 3500, 'Plastic': 3200, 'Glass': 1550, 'Metal': 900, 'Electronics': 140},
    {'Month': 'June', 'Paper': 3600, 'Plastic': 3300, 'Glass': 1500, 'Metal': 950, 'Electronics': 150},
    {'Month': 'July', 'Paper': 3700, 'Plastic': 3400, 'Glass': 1600, 'Metal': 1000, 'Electronics': 160},
    {'Month': 'August', 'Paper': 3800, 'Plastic': 3100, 'Glass': 1650, 'Metal': 920, 'Electronics': 170},
    {'Month': 'September', 'Paper': 3650, 'Plastic': 3200, 'Glass': 1600, 'Metal': 930, 'Electronics': 180},
    {'Month': 'October', 'Paper': 3550, 'Plastic': 3300, 'Glass': 1700, 'Metal': 950, 'Electronics': 190},
    {'Month': 'November', 'Paper': 3450, 'Plastic': 3400, 'Glass': 1750, 'Metal': 960, 'Electronics': 200},
    {'Month': 'December', 'Paper': 3350, 'Plastic': 3500, 'Glass': 1800, 'Metal': 980, 'Electronics': 210}
]

# Extracting the months from the dataset
months = [item['Month'] for item in data]

# Extracting material data
paper = [item['Paper'] for item in data]
plastic = [item['Plastic'] for item in data]
glass = [item['Glass'] for item in data]
metal = [item['Metal'] for item in data]
electronics = [item['Electronics'] for item in data]

# Creating the figure and axis
fig, ax = plt.subplots()

# Stacking each material on top of the other in the bar chart
ax.bar(months, paper, label='Paper')
ax.bar(months, plastic, bottom=paper, label='Plastic')
# We have to add up the previous stacks to get the starting point for the next
ax.bar(months, glass, bottom=[p + pl for p, pl in zip(paper, plastic)], label='Glass')
ax.bar(months, metal, bottom=[p + pl + g for p, pl, g in zip(paper, plastic, glass)], label='Metal')
ax.bar(months, electronics, bottom=[p + pl + g + m for p, pl, g, m in zip(paper, plastic, glass, metal)], label='Electronics')

# Adding labels and title
ax.set_ylabel('Total Quantity')
ax.set_xlabel('Month')
ax.set_title('Monthly Material Recycling Quantities')

# Rotate the months on the x-axis for better readability
plt.xticks(rotation=45)

# Adding a legend to describe the stacks
ax.legend()

# Displaying the stacked bar chart
plt.tight_layout()
plt.show()