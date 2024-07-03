
import matplotlib.pyplot as plt

# Data to plot
labels = 'Exercise', 'Meditation', 'Healthy Eating', 'Reading', 'Socializing', 'Hobbies', 'Sleeping', 'Working', 'Leisure'
sizes = [25, 15, 20, 10, 8, 7, 10, 5, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#ffb347']

# Plot
plt.figure(figsize=[12, 7])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Health Activities', pad=20)
plt.show()