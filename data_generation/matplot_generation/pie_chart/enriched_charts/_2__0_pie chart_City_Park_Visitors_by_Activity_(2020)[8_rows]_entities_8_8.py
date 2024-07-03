
import matplotlib.pyplot as plt

# Data to plot
categories = ['Mental Health', 'Physical Fitness', 'Nutrition', 'Sleep', 'Stress Management', 'Preventive Care', 'Personal Development', 'Substance Abuse Prevention']
values = [180, 200, 150, 120, 170, 130, 140, 110]
colors = ['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffcc00', '#c4e17f']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Health & Psychology Budget Allocation for 2023', pad=20)
plt.show()