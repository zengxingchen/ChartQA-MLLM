
import matplotlib.pyplot as plt

# Data to plot
activities = ['Meal Planning', 'Grocery Shopping', 'Cooking', 'Eating Out', 'Nutritional Research', 'Food Photography', 'Recipe Development', 'Dietary Consultations']
hours = [5, 4, 6, 3, 4, 2, 5, 6]
colors = ['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#FF1493', '#7B68EE', '#2E8B57', '#FF4500']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Time Allocation in Food & Nutrition', pad=20)
plt.show()