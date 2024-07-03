
import matplotlib.pyplot as plt

# Data
items = [
    "Laptop", "Smartphone", "Tablet", "Headphones", 
    "Smartwatch", "Camera", "Printer", "Monitor", 
    "Keyboard", "Mouse", "External Hard Drive", 
    "USB Flash Drive", "Router", "Webcam"
]
costs = [1200, 800, 400, 150, 200, 600, 300, 250, 80, 50, 100, 20, 100, 70]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(items, costs, color=[
    '#4E79A7', '#F28E2B', '#E15759', '#76B7B2',
    '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7',
    '#9C755F', '#BAB0AC', '#FFBE7D', '#4E79A7',
    '#F28E2B', '#E15759'
], width=0.6)  # Change bar color and width

# Adding labels and title
ax.set_ylabel('Cost (in USD)')
ax.set_title('Cost of Electronic Devices in 2023', pad=30)

# Show the plot
plt.show()