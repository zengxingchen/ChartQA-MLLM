
import matplotlib.pyplot as plt

# Data for plotting
categories = [
    "Innovation", "Technology", "AI", "Robotics", "Quantum Computing",
    "Blockchain", "Cybersecurity", "VR/AR", "Biotech", "Nanotechnology",
    "3D Printing", "Autonomous Vehicles", "Space Travel", "Sustainable Energy"
]
values = [
    12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75
]

# Changing figure size
plt.figure(figsize=(14, 8))

# Plotting - horizontal bar chart
bar_height = 0.6
plt.barh(categories, values, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#33FFEC',
    '#B833FF', '#FFE933', '#FF3333', '#33FFA5', '#8F33FF', '#FF3338',
    '#33FFD7', '#FF3380'
], height=bar_height)

# Customize chart
plt.xlabel('Value', fontsize=14)
plt.ylabel('Category', fontsize=14)
plt.title('Key Innovations and Technologies', fontsize=16)

# Resize bar height
plt.yticks(categories, [str(category) for category in categories], fontsize=10)

# Show plot
plt.show()