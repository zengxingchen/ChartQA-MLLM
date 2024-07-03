
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = ['Coal', 'Natural Gas', 'Hydro', 'Wind', 'Solar', 'Nuclear', 'Oil']
sizes = [27, 24, 16, 11, 9, 8, 5]
colors = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']

# Create a figure of specified width and height
plt.figure(figsize=(16, 8))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Set the title of the chart
plt.title('Global Energy Distribution in 2021')

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()