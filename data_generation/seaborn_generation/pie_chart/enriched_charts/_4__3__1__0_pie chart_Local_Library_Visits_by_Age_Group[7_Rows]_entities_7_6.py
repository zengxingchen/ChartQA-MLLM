
import matplotlib.pyplot as plt

# Data to plot
labels = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Gym Workout', 'Pilates', 'Dance', 'Martial Arts']
sizes = [20, 25, 15, 10, 15, 5, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#A1FF33']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Favorite Sports Activities', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()