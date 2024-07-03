
import matplotlib.pyplot as plt

# Data to plot
categories = ['Research', 'Writing', 'Editing', 'Field Work', 'Interviewing', 'Reading', 'Publishing', 'Networking']
time_spent = [2, 3, 1.5, 1, 0.5, 2, 0.5, 1]
colors = ['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4']

# Plot pie chart
plt.figure(figsize=(10, 6))
plt.pie(time_spent, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation in Research & Writing Activities', pad=20)
plt.show()