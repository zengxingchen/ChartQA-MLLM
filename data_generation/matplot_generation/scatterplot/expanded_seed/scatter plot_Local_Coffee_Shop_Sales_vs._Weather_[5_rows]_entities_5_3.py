
import matplotlib.pyplot as plt
from datetime import datetime

# Data
data = [
    {'Date': '2023-03-15', ' Temperature (°C)': 12, ' Coffee Sales ($)': 430},
    {'Date': '2023-03-16', ' Temperature (°C)': 7, ' Coffee Sales ($)': 550},
    {'Date': '2023-03-17', ' Temperature (°C)': 21, ' Coffee Sales ($)': 350},
    {'Date': '2023-03-18', ' Temperature (°C)': 17, ' Coffee Sales ($)': 390},
    {'Date': '2023-03-19', ' Temperature (°C)': 22, ' Coffee Sales ($)': 320}
]

# Extracting values for plotting
temperatures = [entry[' Temperature (°C)'] for entry in data]
sales = [entry[' Coffee Sales ($)'] for entry in data]
dates = [entry['Date'] for entry in data]
date_labels = [datetime.strptime(date, '%Y-%m-%d').strftime('%b %d') for date in dates]  # Formatting date labels

# Visual Encoding Details
colors = temperatures  # Color based on temperature
sizes = [sale / 10 for sale in sales]  # Size based on coffee sales

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(temperatures, sales, c=colors, s=sizes, cmap='coolwarm', alpha=0.6)

# Add color bar for temperature
cbar = plt.colorbar(scatter)
cbar.set_label('Temperature (°C)')

# Annotations for each data point
for i, date_label in enumerate(date_labels):
    plt.annotate(date_label, (temperatures[i], sales[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Labeling Axes and Title
plt.xlabel('Temperature (°C)')
plt.ylabel('Coffee Sales ($)')
plt.title('Coffee Sales vs. Temperature on Different Dates')

plt.grid(True)  # Add a grid for better readability
plt.tight_layout()  # Adjust the layout

# Show the plot
plt.show()