
import matplotlib.pyplot as plt

# Data to plot
labels = 'Reading', 'Exercise', 'Sleeping', 'Working', 'Leisure'
sizes = [40, 20, 50, 60, 30]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Daily Activities Distribution', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()