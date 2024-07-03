
import matplotlib.pyplot as plt

# Given data
data = [
    {'Device Type': 'Smartphones', 'Monthly Repair Requests': 320},
    {'Device Type': 'Tablets', 'Monthly Repair Requests': 150},
    {'Device Type': 'Laptops', 'Monthly Repair Requests': 190},
    {'Device Type': 'Desktop Computers', 'Monthly Repair Requests': 70},
    {'Device Type': 'Smartwatches', 'Monthly Repair Requests': 60},
    {'Device Type': 'E-readers', 'Monthly Repair Requests': 20},
    {'Device Type': 'Portable Game Consoles', 'Monthly Repair Requests': 55},
    {'Device Type': 'Wireless Headphones', 'Monthly Repair Requests': 85},
    {'Device Type': 'Bluetooth Speakers', 'Monthly Repair Requests': 40},
    {'Device Type': 'Digital Cameras', 'Monthly Repair Requests': 25},
    {'Device Type': 'Drones', 'Monthly Repair Requests': 30},
    {'Device Type': 'GPS Navigation Systems', 'Monthly Repair Requests': 10}
]

# Extracting device types and their corresponding monthly repair requests
device_types = [item['Device Type'] for item in data]
repair_requests = [item['Monthly Repair Requests'] for item in data]

# Creating bar locations
bar_positions = range(len(device_types))

# Starting the plot
plt.figure(figsize=(10, 6))  # Custom figure size

# Creating the bar chart with horizontal bars
plt.barh(bar_positions, repair_requests, color='skyblue', edgecolor='black')

# Setting the y-ticks to device type names
plt.yticks(bar_positions, device_types)

# Adding a title and labels
plt.title('Monthly Repair Requests by Device Type')
plt.xlabel('Number of Monthly Repair Requests')
plt.ylabel('Device Type')

# Grid lines can help the readability of the chart
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adding value labels to each bar
for index, value in enumerate(repair_requests):
    plt.text(value, index, f' {value}', va='center')

# Show the plot
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.show()