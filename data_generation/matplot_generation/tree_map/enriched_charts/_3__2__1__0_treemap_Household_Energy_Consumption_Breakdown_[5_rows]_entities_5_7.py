
import matplotlib.pyplot as plt
import squarify

# Data points
industry = [
    'Artificial Intelligence', 'Blockchain', 'Cybersecurity', 'Quantum Computing', 
    'Virtual Reality', 'Augmented Reality', '5G Technology', 
    'Autonomous Vehicles', 'Internet of Things', 'Nanotechnology', 
    'Biotechnology', 'Space Exploration'
]
market_share = [30, 20, 15, 10, 5, 5, 5, 5, 5, 3, 3, 3]
revenue = [500, 300, 250, 200, 150, 100, 120, 110, 90, 80, 70, 60]

# Color scheme using specific color codes
colors = [
    '#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464', 
    '#CC0000', '#00BFFF', '#228B22', '#FF4500', '#FFD700',
    '#8A2BE2', '#FF6347'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(18, 14))

# Creating a treemap
squarify.plot(sizes=market_share, label=industry, color=colors, alpha=0.8, value=revenue, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Future Technologies Market Share', fontsize=18, color='darkblue')
plt.suptitle('Market Share and Revenue of Emerging Technologies', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()