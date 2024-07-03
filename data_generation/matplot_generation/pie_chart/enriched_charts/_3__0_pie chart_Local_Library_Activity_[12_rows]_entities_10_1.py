
import matplotlib.pyplot as plt

# Data to plot
food_items = ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Meal Preparation', 'Grocery Shopping', 'Dining Out', 'Nutritional Research']
time_spent = [1, 1.5, 2, 0.5, 2.5, 1, 1, 0.5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33', '#FF33A6', '#33FFF5', '#7D33FF', '#FF8C33']

# Plot pie chart
plt.figure(figsize=(12, 9))
plt.pie(time_spent, labels=food_items, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Daily Food & Nutrition Activities Distribution', pad=20)
plt.show()