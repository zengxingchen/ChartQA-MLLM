
import matplotlib.pyplot as plt

# Data to plot
categories = ['Education', 'Healthcare', 'Defense', 'Technology', 'Environment', 'Infrastructure', 'Research', 'Agriculture']
values = [215, 130, 245, 160, 90, 150, 120, 85]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('National Budget Allocation for 2023')
plt.show()