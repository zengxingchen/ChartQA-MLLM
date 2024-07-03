
import matplotlib.pyplot as plt

# Data to plot
categories = ['Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Water', 'Fiber', 'Sugar']
values = [180, 250, 90, 45, 35, 280, 70, 55]
colors = ['#ff6666','#66b2ff','#99ff66','#ffcc66','#c266ff','#66ffcc', '#ff66b2', '#b2ff66']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Daily Nutritional Intake Breakdown', pad=20)
plt.show()