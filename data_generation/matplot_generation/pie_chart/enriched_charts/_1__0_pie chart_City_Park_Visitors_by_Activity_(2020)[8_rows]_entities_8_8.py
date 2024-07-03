
import matplotlib.pyplot as plt

# Data to plot
categories = ['Paris', 'Tokyo', 'New York', 'London', 'Sydney', 'Berlin', 'Dubai', 'Cape Town']
values = [220, 135, 250, 175, 100, 140, 130, 95]
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Tourist Visits in Major Cities for 2023', pad=20)
plt.show()