
import matplotlib.pyplot as plt

# Data to plot
activities = ['Meditation', 'Exercise', 'Therapy', 'Reading', 'Journaling', 'Hobbies', 'Socializing', 'Resting', 'Mindfulness Practice', 'Outdoor Activities', 'Healthy Eating']
time_spent = [2, 3, 1.5, 2.5, 1, 2, 3, 2, 1.5, 2.5, 2]
colors = ['#ffcccb', '#add8e6', '#90ee90', '#ffd700', '#dda0dd', '#ffb6c1', '#20b2aa', '#778899', '#f08080', '#e0ffff', '#faebd7']

# Plot pie chart
plt.figure(figsize=(12, 8))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation for Mental Wellness Activities', pad=20)
plt.show()