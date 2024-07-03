
import matplotlib.pyplot as plt

# Data to plot
activities = ['Exercise', 'Meditation', 'Therapy', 'Healthy Eating', 'Reading', 'Sleep', 'Work-Life Balance', 'Social Interaction']
time_spent = [2.0, 1.5, 1.0, 1.5, 2.0, 7.0, 3.0, 2.5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76D7C4']

# Plot pie chart
plt.figure(figsize=(10, 7))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Health & Psychology Activities Distribution', pad=20)
plt.show()