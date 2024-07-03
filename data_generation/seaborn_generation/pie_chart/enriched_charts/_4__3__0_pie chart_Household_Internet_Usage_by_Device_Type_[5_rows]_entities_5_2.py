
import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Mountain Climbing', 'Scuba Diving', 'Skydiving', 'Hiking', 'Safari', 'Snowboarding', 'Bungee Jumping', 'Paragliding']
popularity = [19.5, 14.2, 12.8, 22.4, 9.3, 10.1, 6.7, 5.0]

# Colors for each section of the pie chart
colors = ['#ff5733','#33ff57','#3357ff','#ff33a1','#a133ff','#33ffdd','#ff7733','#77ff33']

# Create a pie chart
plt.figure(figsize=(10, 7))  # Modify the size of the chart
plt.pie(popularity, labels=categories, colors=colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popularity of Adventure Activities in 2023', y=1.10)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()