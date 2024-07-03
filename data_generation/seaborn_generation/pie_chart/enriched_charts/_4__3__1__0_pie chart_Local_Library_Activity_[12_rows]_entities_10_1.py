
import matplotlib.pyplot as plt

# Data to plot
activities = ['Reading', 'Writing', 'Meditation', 'Exercise', 'Research', 'Discussion', 'Art Creation', 'Music Listening']
time_spent = [2.0, 1.5, 1.0, 2.0, 1.5, 1.0, 1.5, 1.0]
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#DA70D6', '#5F9EA0']

# Plot pie chart
plt.figure(figsize=(12, 9))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Intellectual & Creative Activities Distribution', pad=20)
plt.show()