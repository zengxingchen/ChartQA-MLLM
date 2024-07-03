
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston",
    "Phoenix", "Philadelphia", "San Antonio", "San Diego", 
    "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", 
    "Columbus", "Charlotte"
]
temperatures = [10.0, 18.2, 11.3, 20.6, 23.4, 12.9, 20.3, 17.5, 18.9, 15.5, 20.1, 20.4, 18.7, 11.7, 15.7]

# Colors for each city
colors = [
    '#3498db', '#2ecc71', '#9b59b6', '#f1c40f', '#e74c3c',
    '#34495e', '#1abc9c', '#7f8c8d', '#d35400', '#2c3e50',
    '#8e44ad', '#c0392b', '#bdc3c7', '#16a085', '#27ae60'
]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(cities, temperatures, color=colors, height=0.6) # Adjusted bar width to 0.6

# Set the title and labels
ax.set_title('Average Annual Temperature in Various Cities', fontsize=15)
ax.set_xlabel('Average Annual Temperature (°C)', fontsize=12)
ax.set_ylabel('City', fontsize=12)

# Customize the tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.2
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}°C', va='center')

# Show the plot
plt.tight_layout()
plt.show()