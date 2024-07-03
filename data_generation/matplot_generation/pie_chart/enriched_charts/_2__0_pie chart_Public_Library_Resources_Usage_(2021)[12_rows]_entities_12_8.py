
import matplotlib.pyplot as plt

# Data to plot
labels = 'Modern Art', 'Classical Art', 'Sculpture', 'Photography', 'Digital Art', 'Installation Art', 'Performance Art', 'Crafts', 'Street Art'
sizes = [20, 15, 10, 18, 12, 8, 6, 5, 6]
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8', '#a833ff', '#33fff0', '#f0ff33', '#ff8f33', '#33ffa3']

# Plot
plt.figure(figsize=[10, 6])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Art Categories')
plt.show()