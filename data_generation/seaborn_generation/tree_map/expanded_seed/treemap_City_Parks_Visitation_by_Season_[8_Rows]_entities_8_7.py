
import matplotlib.pyplot as plt
import squarify

# Your data
data = [
    {'Park Name': 'Central Park', 'Spring Visitors': 12000, 'Summer Visitors': 30000, 'Fall Visitors': 15000, 'Winter Visitors': 4000},
    {'Park Name': 'Maple Grove', 'Spring Visitors': 8000, 'Summer Visitors': 22000, 'Fall Visitors': 9000, 'Winter Visitors': 2000},
    {'Park Name': 'Harbor View', 'Spring Visitors': 6000, 'Summer Visitors': 25000, 'Fall Visitors': 10000, 'Winter Visitors': 2500},
    {'Park Name': 'Riverside', 'Spring Visitors': 4000, 'Summer Visitors': 18000, 'Fall Visitors': 8000, 'Winter Visitors': 1000},
    {'Park Name': 'Sunset Trails', 'Spring Visitors': 3500, 'Summer Visitors': 12000, 'Fall Visitors': 6000, 'Winter Visitors': 1500},
    {'Park Name': 'Pine Hill', 'Spring Visitors': 3100, 'Summer Visitors': 14000, 'Fall Visitors': 5500, 'Winter Visitors': 900},
    {'Park Name': 'Meadowlands', 'Spring Visitors': 2900, 'Summer Visitors': 11000, 'Fall Visitors': 5000, 'Winter Visitors': 1200},
    {'Park Name': 'Lakefront', 'Spring Visitors': 2700, 'Summer Visitors': 13000, 'Fall Visitors': 4900, 'Winter Visitors': 1100}
]

# Flatten the data and get the sizes for the squares
names = []
sizes = []
for park in data:
    for key in park:
        if key != 'Park Name':
            names.append(f"{park['Park Name']} - {key.split()[0]}")
            sizes.append(park[key])

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=names, alpha=0.8)

# Optional: If you want to remove the axes labels
plt.axis('off')

# Title of the treemap
plt.title('Park Visitors Treemap')

# Show the plot
plt.show()