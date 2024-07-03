
import matplotlib.pyplot as plt

# Data to plot
labels = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Gym', 'Dance', 'Hiking', 'Martial Arts']
sizes = [30, 20, 15, 10, 8, 7, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF5', '#F5FF33', '#FF8633', '#6E33FF']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Fitness Activities', pad=20)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()