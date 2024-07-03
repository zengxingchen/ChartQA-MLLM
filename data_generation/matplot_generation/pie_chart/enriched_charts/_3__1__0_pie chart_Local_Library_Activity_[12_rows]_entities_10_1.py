
import matplotlib.pyplot as plt

# Data to plot
activities = ['Breakfast', 'Morning Snack', 'Lunch', 'Afternoon Snack', 'Dinner', 'Workout', 'Meal Prep', 'Grocery Shopping']
time_spent = [1.5, 0.5, 2.0, 0.5, 2.0, 1.0, 1.5, 1.0]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666']

# Plot pie chart
plt.figure(figsize=(10, 7))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Food & Nutrition Activities Distribution', pad=20)
plt.show()