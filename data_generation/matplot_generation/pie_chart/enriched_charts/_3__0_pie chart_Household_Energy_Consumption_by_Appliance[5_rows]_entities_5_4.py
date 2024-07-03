
import matplotlib.pyplot as plt

# Data to plot
labels = 'Running', 'Yoga', 'Cycling', 'Swimming', 'Hiking'
sizes = [30.4, 25.1, 20.8, 15.2, 8.5]
colors = ['#ff6666', '#ffcc66', '#66b3ff', '#99ff99', '#c2f0c2']

# Create pie chart
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Popularity of Fitness Activities in 2023', y=1.08)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()