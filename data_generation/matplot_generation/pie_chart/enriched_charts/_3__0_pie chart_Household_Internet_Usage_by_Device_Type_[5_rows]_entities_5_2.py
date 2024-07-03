
import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Oils', 'Sweets', 'Beverages']
popularity = [23.4, 20.1, 18.7, 16.3, 12.4, 4.5, 3.0, 1.6]

# Colors for each section of the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76D7C4']

# Create a pie chart
plt.figure(figsize=(12, 9))  # Modify the size of the chart
plt.pie(popularity, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Dietary Components Popularity in 2023', y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()