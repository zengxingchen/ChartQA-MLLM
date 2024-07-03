
import matplotlib.pyplot as plt

# Data to plot
activities = ['Research', 'Reading', 'Writing', 'Meetings', 'Brainstorming', 'Lunch Break', 'Reviewing Literature', 'Networking']
time_spent = [3.5, 2.5, 4, 1.5, 2, 1, 2.5, 2]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Plot pie chart
plt.figure(figsize=(12, 8))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Academic Activities Distribution')
plt.show()