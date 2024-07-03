
import matplotlib.pyplot as plt

# Data to plot
activities = ['Research', 'Reading', 'Writing', 'Meetings', 'Brainstorming', 'Lunch Break', 'Reviewing Literature', 'Networking', 'Experimentation', 'Documentation', 'Analysis']
time_spent = [3.5, 2.5, 4, 1.5, 2, 1, 2.5, 2, 3, 1.5, 2.5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666', '#ffb366', '#c2c2f0', '#ff66b2']

# Plot pie chart
plt.figure(figsize=(14, 10))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation for Research Activities', pad=20)
plt.show()