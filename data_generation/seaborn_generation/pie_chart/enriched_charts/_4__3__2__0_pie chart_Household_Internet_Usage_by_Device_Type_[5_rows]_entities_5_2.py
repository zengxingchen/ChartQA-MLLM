
import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Reading', 'Writing', 'Researching', 'Teaching', 'Editing']
values = [30.0, 25.0, 20.0, 15.0, 10.0]

# Colors for each section of the pie chart
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

# Create a pie chart
plt.figure(figsize=(12, 10))  # Modify the size of the chart
plt.pie(values, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Time Allocation in Literary Activities')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()