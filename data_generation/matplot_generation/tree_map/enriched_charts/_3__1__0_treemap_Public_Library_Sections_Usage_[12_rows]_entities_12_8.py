
import matplotlib.pyplot as plt
import squarify

# Data for future technologies market share
topics = ['Smartphones', 'Wearable Devices', 'IoT Devices', 'Electric Vehicles', 'AI Assistants', 
          'Drones', '3D Printing', 'AR/VR', 'Blockchain', 'Quantum Computing', 'Robotics', 
          'Nanotechnology', 'Biotechnology']
market_share = [22.0, 12.0, 16.0, 8.0, 10.0, 5.0, 6.0, 4.0, 7.0, 3.0, 7.0, 2.0, 6.0]

# Custom color scheme
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c1f0c1', '#ff9999', '#66b3ff', '#99ff99',
    '#ffcc99', '#c2c2f0', '#ffb3e6'
]

# Treemap
plt.figure(figsize=(12, 18))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=topics, color=colors, alpha=0.8)
plt.title('Future Technologies Market Share 2022', pad=30, fontsize=18)
plt.axis('off')  # No axes for a cleaner look

plt.show()