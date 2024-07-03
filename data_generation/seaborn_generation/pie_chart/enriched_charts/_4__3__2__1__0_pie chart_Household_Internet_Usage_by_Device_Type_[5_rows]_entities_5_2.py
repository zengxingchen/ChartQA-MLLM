
import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Travel', 'Adventure', 'Cultural Exploration', 'Historical Sites', 'Beach Holidays', 'Mountain Climbing', 'Urban Exploration', 'Wildlife Safari', 'Extreme Sports']
values = [25.0, 20.0, 18.0, 12.0, 10.0, 8.0, 5.0, 1.5, 0.5]

# Colors for each section of the pie chart
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#40E0D0', '#1E90FF', '#FF69B4', '#BA55D3', '#8A2BE2', '#FF4500']

# Create a pie chart
plt.figure(figsize=(14, 8))  # Modify the size of the chart
plt.pie(values, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popular Travel & Adventure Activities in 2023', y=1.08)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()