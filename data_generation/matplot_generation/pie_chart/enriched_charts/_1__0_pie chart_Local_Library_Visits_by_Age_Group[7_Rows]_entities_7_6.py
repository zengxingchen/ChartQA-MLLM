
import matplotlib.pyplot as plt

# Data to plot
labels = ['Running', 'Yoga', 'Swimming', 'Cycling', 'Weightlifting', 'Hiking', 'Dancing', 'Rowing']
sizes = [30, 20, 15, 10, 15, 5, 3, 2]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#FF4500', '#2E8B57']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Fitness Activities', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()