
import matplotlib.pyplot as plt
import squarify

# Data for Future Technologies & Society
topics = [
    'Artificial Intelligence', 'Quantum Computing', 'Cybersecurity', 
    'Blockchain Technology', 'Renewable Energy', 'Biotechnology', 
    'Space Exploration', '5G Technology', 'Autonomous Vehicles', 
    'Augmented Reality', 'Robotics', 'Smart Cities', 'Others'
]
popularity = [
    18.5, 15.6, 14.0, 13.2, 12.5, 11.3, 
    10.4, 9.8, 8.7, 7.9, 6.5, 5.9, 4.7
]

# Custom color scheme
colors = [
    '#2E8B57', '#FF6347', '#4682B4', '#87CEEB', '#D2691E', 
    '#8A2BE2', '#FFD700', '#DC143C', '#00CED1', '#FF7F50', 
    '#6A5ACD', '#20B2AA', '#FF4500'
]

# Treemap
plt.figure(figsize=(16, 12))  # Adjusting the size of the treemap
squarify.plot(sizes=popularity, label=topics, color=colors, alpha=0.8)
plt.title('Popularity of Future Technologies and Society Topics in 2023', fontsize=20)
plt.axis('off')  # No axes for a cleaner look

plt.show()