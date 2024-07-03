
import matplotlib.pyplot as plt

# Data to plot
categories = ['Cardiovascular Health', 'Mental Health', 'Nutrition', 'Physical Fitness', 'Preventive Care', 'Dental Health', 'Vision Care', 'Sleep Health']
values = [180, 120, 95, 110, 140, 70, 85, 75]
colors = ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9', '#92a8d1', '#f7786b', '#034f84', '#98b4d4']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Health & Psychology Budget Allocation for 2023', pad=20)
plt.show()