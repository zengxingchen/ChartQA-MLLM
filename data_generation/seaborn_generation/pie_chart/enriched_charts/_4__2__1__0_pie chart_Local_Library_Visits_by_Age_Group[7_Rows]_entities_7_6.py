
import matplotlib.pyplot as plt

# Data to plot
labels = ['Reading', 'Writing', 'Painting', 'Sculpting', 'Photography', 'Calligraphy', 'Pottery', 'Origami', 'Sketching']
sizes = [22, 18, 14, 10, 12, 9, 8, 7, 10]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22']

# Create pie chart
plt.figure(figsize=(14, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Creative Activities', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()