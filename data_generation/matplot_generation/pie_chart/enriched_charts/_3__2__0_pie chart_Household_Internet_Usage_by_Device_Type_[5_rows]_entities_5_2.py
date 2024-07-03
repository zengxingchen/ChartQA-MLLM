
import matplotlib.pyplot as plt

# Data for the pie chart
foods = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy']
percentages = [20.0, 25.0, 30.0, 15.0, 10.0]

# Colors for each section of the pie chart
colors = ['#FFA07A', '#98FB98', '#FFD700', '#8A2BE2', '#5F9EA0']

# Create a pie chart
plt.figure(figsize=(10, 8))  # Modify the size of the chart
plt.pie(percentages, labels=foods, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Composition of a Balanced Diet in 2023')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()