
import matplotlib.pyplot as plt

# Data to plot
activities = ['Sleep', 'Work', 'Commute', 'Eating', 'Leisure', 'Exercise', 'Housework', 'Online Browsing']
time_spent = [8, 9, 2, 1.5, 3, 1, 1.2, 2.3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4']

# Plot pie chart
plt.figure(figsize=(10, 7))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Activities Distribution')
plt.show()