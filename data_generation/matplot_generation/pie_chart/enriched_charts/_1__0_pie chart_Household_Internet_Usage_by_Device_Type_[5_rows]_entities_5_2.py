
import matplotlib.pyplot as plt

# Data for the pie chart
destinations = ['Japan', 'France', 'Italy', 'Australia', 'Canada', 'Thailand', 'Spain', 'New Zealand', 'Iceland']
popularity = [20.3, 18.7, 15.6, 12.4, 10.2, 8.1, 7.3, 4.5, 3.0]

# Colors for each section of the pie chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFBD33', '#33FFF6', '#9933FF', '#FF3388', '#33FF99']

# Create a pie chart
plt.figure(figsize=(12, 10))  # Modify the size of the chart
plt.pie(popularity, labels=destinations, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popular Travel Destinations in 2023')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()