
import matplotlib.pyplot as plt

# Data for the pie chart
hobbies = ['Reading', 'Traveling', 'Gardening', 'Cooking', 'Photography', 'Painting', 'Writing', 'Dancing', 'Gaming']
popularity = [22.5, 18.0, 15.0, 13.2, 10.8, 8.5, 7.1, 3.8, 1.1]

# Colors for each section of the pie chart
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#7FFF00']

# Create a pie chart
plt.figure(figsize=(14, 12))  # Modify the size of the chart
plt.pie(popularity, labels=hobbies, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popular Hobbies in 2023', fontsize=16, y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()