
import matplotlib.pyplot as plt

# Data
fields = ['Artificial Intelligence', 'Quantum Computing', 'Renewable Energy', 'Biotechnology', 'Robotics',
          'Nanotechnology', 'Augmented Reality', '3D Printing', 'Genomics', 'Blockchain',
          'Virtual Reality', 'Cybersecurity', 'Internet of Things', 'Autonomous Vehicles', 'Wearable Technology']
values = [500, 300, 250, 200, 150, 100, 80, 70, 60, 50, 40, 30, 25, 20, 15]

# Colors
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f',
          '#34495e', '#e67e22', '#1abc9c', '#8e44ad', '#d35400',
          '#2980b9', '#c0392b', '#27ae60', '#16a085', '#f39c12']

# Pie chart
fig, ax = plt.subplots(figsize=(14, 10))  # Width, Height of the chart
ax.pie(values, labels=fields, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Investments in Future Technologies (Millions USD)', pad=20)
plt.show()