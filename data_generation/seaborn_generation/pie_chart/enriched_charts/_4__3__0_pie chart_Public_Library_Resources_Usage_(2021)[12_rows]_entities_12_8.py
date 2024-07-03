
import matplotlib.pyplot as plt

# Data to plot
labels = 'Sightseeing', 'Adventure Sports', 'Cultural Tours', 'Cruises', 'Nature Exploration', 'City Breaks', 'Relaxation', 'Culinary Tours'
sizes = [30, 20, 15, 10, 12, 8, 3, 2]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#F3FF33', '#A833FF', '#33FFA8']

# Plot
plt.figure(figsize=[12, 8])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Preferred Travel Activities', y=1.05)  # Adjust title position to avoid overlap
plt.show()