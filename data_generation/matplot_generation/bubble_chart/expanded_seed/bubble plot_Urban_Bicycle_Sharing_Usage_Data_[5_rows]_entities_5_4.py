
import matplotlib.pyplot as plt

# Given data
data = [
    {'Date': '2023-01-15', 'City': 'Austin', 'Bicycles Shared': 320, 'Trips Recorded': 410, 'Bubble Size (Average Trip Distance in km)': 5.5},
    {'Date': '2023-01-15', 'City': 'Boston', 'Bicycles Shared': 275, 'Trips Recorded': 350, 'Bubble Size (Average Trip Distance in km)': 4.8},
    {'Date': '2023-01-15', 'City': 'Denver', 'Bicycles Shared': 150, 'Trips Recorded': 180, 'Bubble Size (Average Trip Distance in km)': 6.1},
    {'Date': '2023-01-15', 'City': 'Seattle', 'Bicycles Shared': 200, 'Trips Recorded': 250, 'Bubble Size (Average Trip Distance in km)': 4.3},
    {'Date': '2023-01-15', 'City': 'San Francisco', 'Bicycles Shared': 400, 'Trips Recorded': 550, 'Bubble Size (Average Trip Distance in km)': 3.9}
]

# Prepare the lists for the plot
cities = [item['City'] for item in data]
trips = [item['Trips Recorded'] for item in data]
bubble_sizes = [item['Bubble Size (Average Trip Distance in km)'] * 10 for item in data]  # Multiplied to scale up the bubble sizes for better visibility
bicycles_shared = [item['Bicycles Shared'] for item in data]
colors = bicycles_shared  # Here we will use the number of bicycles shared as the color scale

# Create the bubble chart
plt.figure(figsize=(10,6))
bubble = plt.scatter(cities, trips, s=bubble_sizes, c=colors, alpha=0.6, cmap='viridis')

# Create a colorbar to show the scale of bicycles shared
cbar = plt.colorbar(bubble)
cbar.set_label('Number of Bicycles Shared')

# Title and labels
plt.title('Trips Recorded vs Cities with Bubble Sizes\n(Average Trip Distance) and Color Scale (Bicycles Shared) on 2023-01-15')
plt.xlabel('Cities')
plt.ylabel('Trips Recorded')

# Show the plot
plt.show()