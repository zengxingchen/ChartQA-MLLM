
import matplotlib.pyplot as plt

# Data for the pie chart
sports = ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Swimming', 'Running', 'Cycling', 'Gymnastics', 'Martial Arts']
popularity = [30.2, 25.3, 15.8, 10.7, 7.5, 5.1, 3.7, 1.0, 0.7]

# Colors for each section of the pie chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF9', '#F9FF33', '#33FFCE', '#A133FF', '#FF8333']

# Create a pie chart
plt.figure(figsize=(12, 10))
plt.pie(popularity, labels=sports, colors=colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popularity of Different Sports in 2023', y=1.08)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()