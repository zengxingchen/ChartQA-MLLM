
import matplotlib.pyplot as plt

# Data to plot
categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacking', 'Cooking', 'Grocery Shopping', 'Meal Planning', 'Cleaning Up']
time_spent = [1, 1, 1.5, 0.5, 2, 1, 0.5, 1]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4']

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(time_spent, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Spent on Food & Nutrition Activities')
plt.show()