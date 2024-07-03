
import matplotlib.pyplot as plt

# Data to plot
labels = ['Sightseeing', 'Hiking', 'Beach', 'Cultural Tours', 'Cruises', 'Adventure Sports', 'Wildlife Safari', 'City Tours']
sizes = [25, 15, 20, 10, 10, 10, 5, 5]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#8A2BE2', '#FF6347', '#4682B4']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Favorite Travel Activities', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()