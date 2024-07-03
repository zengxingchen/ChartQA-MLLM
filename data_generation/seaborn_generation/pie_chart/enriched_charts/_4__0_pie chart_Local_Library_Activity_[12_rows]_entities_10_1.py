
import matplotlib.pyplot as plt

# Data to plot
activities = ['Reading', 'Working', 'Commute', 'Cooking', 'Exercise', 'Social Media', 'Watching TV', 'Sleeping']
time_spent = [2.5, 8, 1.8, 1.2, 1.5, 2.3, 3.5, 7.2]
colors = ['#ff6666', '#66b2ff', '#99ff99', '#ffcc66', '#c2a2f0', '#ffb3a6', '#c4f17f', '#76d7f4']

# Plot pie chart
plt.figure(figsize=(12, 8))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Time Spent on Activities', pad=20)
plt.show()