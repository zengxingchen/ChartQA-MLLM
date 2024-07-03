
import matplotlib.pyplot as plt

# Data to plot
activities = ['Cooking', 'Grocery Shopping', 'Meal Planning', 'Eating', 'Dining Out', 'Food Research', 'Cleaning Up', 'Baking', 'Food Photography', 'Snacking', 'Reading Food Blogs']
time_spent = [3, 2.5, 1.5, 2, 1, 1.5, 2, 1.5, 1, 1.5, 2]
colors = ['#FF5733', '#33FFBD', '#FF33F6', '#335BFF', '#FF8E33', '#FF33A6', '#33FF57', '#335BFF', '#FF8E33', '#FF33A6', '#FF5733']

# Plot pie chart
plt.figure(figsize=(14, 10))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation for Food & Nutrition Activities', pad=40)
plt.show()