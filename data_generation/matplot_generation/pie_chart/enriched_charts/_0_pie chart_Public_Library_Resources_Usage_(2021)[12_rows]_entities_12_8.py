
import matplotlib.pyplot as plt

# Data to plot
labels = 'Coal', 'Natural Gas', 'Nuclear', 'Hydropower', 'Wind', 'Solar', 'Biomass', 'Geothermal', 'Oil'
sizes = [19, 40, 10, 7, 15, 5, 2, 1, 1]
colors = ['#0b5394', '#6aa84f', '#ff9900', '#3c78d8', '#674ea7', '#a64d79', '#e69138', '#b6d7a8', '#f6b26b']

# Plot
plt.figure(figsize=[12, 8])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Electricity Generation by Energy Source')
plt.show()