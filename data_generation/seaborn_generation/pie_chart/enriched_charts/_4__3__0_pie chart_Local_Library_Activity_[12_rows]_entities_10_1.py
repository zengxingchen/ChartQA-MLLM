
import matplotlib.pyplot as plt

# Data to plot
activities = ['Strength Training', 'Cardio', 'Flexibility Exercises', 'Balance Training', 'Sports', 'Outdoor Activities', 'Rest and Recovery', 'Nutrition Planning']
hours_spent = [3, 2, 1.5, 1, 2.5, 1.5, 3, 2]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33', '#FF33A6', '#33FFF5', '#7D33FF', '#FF8C33']

# Plot pie chart
plt.figure(figsize=(14, 10))
plt.pie(hours_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Physical Activities Distribution', pad=20)
plt.show()