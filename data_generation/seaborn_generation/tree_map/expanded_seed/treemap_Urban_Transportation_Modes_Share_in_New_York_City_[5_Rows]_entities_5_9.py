
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Given data
data = [
    {'Mode': 'Subway', 'Passenger Trips (Million)': 1680},
    {'Mode': 'Bus', 'Passenger Trips (Million)': 637},
    {'Mode': 'Rail', 'Passenger Trips (Million)': 92},
    {'Mode': 'Bicycle', 'Passenger Trips (Million)': 49},
    {'Mode': 'Ferry', 'Passenger Trips (Million)': 21}
]

# Convert the above data to sizes and labels for the treemap
sizes = [item['Passenger Trips (Million)'] for item in data]
labels = [item['Mode'] for item in data]

# Plot
plt.figure(figsize=(12, 8))
colors = sns.color_palette('pastel', len(data))

# Create a treemap using squarify
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Remove axis lines
plt.axis('off')

# Set the title of the treemap
plt.title('Passenger Trips (Million) by Mode', fontsize=16)

# Use Seaborn's styling
sns.despine(left=True, bottom=True)

plt.show()