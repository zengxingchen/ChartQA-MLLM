
import matplotlib.pyplot as plt

# Data to plot
categories = ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Cycling', 'Running', 'Yoga', 'Gymnastics']
values = [300, 200, 150, 250, 180, 220, 170, 160]
colors = ['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#8A2BE2', '#FF4500', '#DA70D6', '#32CD32']

# Create pie chart
plt.figure(figsize=(14, 10))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Participation in Different Sports in 2023', pad=20)
plt.show()