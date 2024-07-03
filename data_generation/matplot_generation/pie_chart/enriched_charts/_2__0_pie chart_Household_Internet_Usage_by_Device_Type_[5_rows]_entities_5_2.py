
import matplotlib.pyplot as plt

# Data for the pie chart
causes = ['Work', 'Financial', 'Health', 'Family', 'Relationships', 'School', 'Social Media', 'Commute', 'Lack of Sleep']
percentages = [25.3, 20.1, 15.7, 12.4, 10.8, 6.5, 4.9, 2.2, 2.1]

# Colors for each section of the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2', '#ff6666', '#c2f0ff']

# Create a pie chart
plt.figure(figsize=(12, 9))  # Modify the size of the chart
plt.pie(percentages, labels=causes, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Common Causes of Stress in 2023')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()