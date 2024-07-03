
import matplotlib.pyplot as plt

# Data for the pie chart
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Pineapple', 'Blueberry', 'Mango', 'Peach']
popularity = [25.5, 20.1, 15.2, 13.7, 10.9, 8.4, 4.6, 1.6, 0.8]

# Colors for each section of the pie chart
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347', '#7B68EE', '#FF7F50', '#87CEFA']

# Create a pie chart
plt.figure(figsize=(14, 8))  # Modify the size of the chart
plt.pie(popularity, labels=fruits, colors=colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Favorite Fruits Distribution in 2023', y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()