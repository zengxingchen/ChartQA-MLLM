
import matplotlib.pyplot as plt
import squarify

# Data for future technologies market share
topics = ['Smartphones', 'Wearable Devices', 'IoT Devices', 'Electric Vehicles', 'AI Assistants', 
          'Drones', '3D Printing', 'AR/VR', 'Blockchain', 'Quantum Computing', 'Robotics', 
          'Nanotechnology', 'Biotechnology', 'Digital Healthcare', 'Autonomous Vehicles', 
          'Renewable Energy', 'Smart Homes', 'Cybersecurity', '5G Technology', 'Edge Computing']
market_share = [22.0, 12.0, 16.0, 8.0, 10.0, 5.0, 6.0, 4.0, 7.0, 3.0, 7.0, 2.0, 6.0, 5.0, 8.0, 9.0, 7.0, 6.0, 10.0, 4.0]

# Custom color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33',
    '#33FFD7', '#FF3333', '#33FFB1', '#FF3333', '#FFC733',
    '#3357FF', '#33FF8C', '#FF57A1', '#A1FF33', '#FF5733',
    '#33FF57', '#FF8C33', '#33FFD7', '#FF3333', '#33FFB1'
]

# Treemap
plt.figure(figsize=(14, 16))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=topics, color=colors, alpha=0.8)
plt.title('Future Technologies & Society Market Share 2022', pad=40, fontsize=20)
plt.axis('off')  # No axes for a cleaner look

plt.show()