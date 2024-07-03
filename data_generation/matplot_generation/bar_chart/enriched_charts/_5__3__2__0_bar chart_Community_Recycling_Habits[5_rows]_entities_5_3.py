
import matplotlib.pyplot as plt

# Data
technologies = ['Artificial Intelligence', 'Blockchain', 'Quantum Computing', 'Virtual Reality', '5G', 'Renewable Energy', 'IoT', 'Cybersecurity', 'Biotechnology', '3D Printing', 'Drones', 'Autonomous Vehicles', 'Edge Computing', 'Robotics', 'Augmented Reality', 'Wearable Technology', 'Smart Cities', 'Digital Twins', 'Space Tourism', 'Nanotechnology']
interest = [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 12]
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#a633ff', '#33ffa6', '#ffa633', '#5733ff', '#57ff33', '#ff3357', '#33a6ff', '#a6ff33', '#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#a633ff', '#33ffa6', '#ffa633', '#5733ff']

# Figure size
plt.figure(figsize=(10, 12))

# Vertical bar chart
plt.bar(technologies, interest, color=colors, width=0.6)

# Y-axis limit starting from a specific value
plt.ylim(0, 100)

# Labeling
plt.ylabel('Interest Level')
plt.title('Interest Levels in Future Technologies & Society', pad=20)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show and save plot
plt.tight_layout()
plt.show()