
import matplotlib.pyplot as plt

# Data to plot
categories = ['Astronaut Training', 'Rocket Launch Preparation', 'Mission Control Operations', 'Scientific Research', 'Space Walks', 'Equipment Maintenance', 'Data Analysis', 'Public Outreach']
time_spent = [3, 4, 2, 5, 1, 1.5, 2.5, 1]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Plot pie chart
plt.figure(figsize=(10, 10))
plt.pie(time_spent, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Spent on Space Exploration Activities', y=1.08)
plt.show()