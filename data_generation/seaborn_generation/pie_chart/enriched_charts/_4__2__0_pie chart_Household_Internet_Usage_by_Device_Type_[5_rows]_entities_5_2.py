
import matplotlib.pyplot as plt

# Data for the pie chart
causes = ['Sports Injuries', 'Overtraining', 'Diet', 'Hydration', 'Sleep Quality', 'Stress', 'Genetics', 'Equipment', 'Weather Conditions']
percentages = [20.5, 18.0, 15.3, 12.7, 10.1, 8.5, 7.4, 4.5, 3.0]

# Colors for each section of the pie chart
colors = ['#ff6666','#66b2ff','#99cc99','#ffcc99','#c285c2','#ff99cc','#c2ffb3','#ffb266','#c2d1f0']

# Create a pie chart
plt.figure(figsize=(14, 10))  # Modify the size of the chart
plt.pie(percentages, labels=causes, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Factors Affecting Athletic Performance in 2023', y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()