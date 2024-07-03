
import matplotlib.pyplot as plt

# Data for the pie chart
destinations = ['Paris', 'New York', 'Tokyo', 'Rome', 'Sydney', 'Cape Town', 'Dubai', 'Rio de Janeiro', 'Bangkok']
popularity = [20.5, 18.0, 15.5, 12.3, 10.0, 8.2, 6.9, 4.5, 4.1]

# Colors for each section of the pie chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF8333', '#33A1FF', '#A1FF33']

# Create a pie chart
plt.figure(figsize=(12, 10))  # Modify the size of the chart
plt.pie(popularity, labels=destinations, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Top Travel Destinations in 2023', y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()