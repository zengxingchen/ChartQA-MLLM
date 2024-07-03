
import matplotlib.pyplot as plt

# Data to plot
labels = ['Hiking', 'Camping', 'Scuba Diving', 'Cycling', 'Sightseeing', 'Road Trips', 'Wildlife Safaris', 'Kayaking']
sizes = [12, 6, 3, 8, 7, 5, 4, 2]
colors = ['#8E44AD', '#2980B9', '#27AE60', '#F39C12', '#C0392B', '#16A085', '#D35400', '#3498DB']

# Create pie chart
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Weekly Hours Spent on Travel & Adventure Activities', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()