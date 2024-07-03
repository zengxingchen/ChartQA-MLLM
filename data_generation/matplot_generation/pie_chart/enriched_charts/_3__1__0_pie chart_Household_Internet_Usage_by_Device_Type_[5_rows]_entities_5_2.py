
import matplotlib.pyplot as plt

# Data for the pie chart
sports = ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Swimming', 'Athletics', 'Rugby', 'Cycling', 'Gymnastics']
popularity = [22.5, 18.1, 16.3, 12.0, 9.8, 8.7, 7.4, 3.2, 2.0]

# Colors for each section of the pie chart
colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#FF69B4', '#BA55D3', '#FF6347', '#3CB371', '#4682B4']

# Create a pie chart
plt.figure(figsize=(10, 8))  # Modify the size of the chart
plt.pie(popularity, labels=sports, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Favorite Sports in 2023', y=1.08)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()