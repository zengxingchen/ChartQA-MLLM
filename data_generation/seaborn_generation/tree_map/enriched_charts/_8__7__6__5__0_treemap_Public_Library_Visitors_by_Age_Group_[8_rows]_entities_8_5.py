
import matplotlib.pyplot as plt
import squarify

topics = [
    'Artificial Intelligence', 'Machine Learning', 'Deep Learning', 'Neural Networks', 
    'Natural Language Processing', 'Computer Vision', 'Data Science', 'Big Data', 
    'Robotics', 'Internet of Things', 'Cybersecurity', 'Cloud Computing', 
    'Quantum Computing', 'Augmented Reality', 'Virtual Reality', 'Blockchain', 
    'Edge Computing', 'Bioinformatics', 'Autonomous Vehicles', 'Smart Cities', 
    'Wearable Technology', '5G Technology', 'Digital Twins', 'AI Ethics'
]

counts = [
    1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 
    300, 250, 200, 150, 100, 90, 80, 70, 60, 50
]

color_palette = [
    '#FF6347', '#4682B4', '#6A5ACD', '#32CD32', '#FFD700', '#FF4500', '#8A2BE2', 
    '#00CED1', '#FF1493', '#7FFF00', '#D2691E', '#20B2AA', '#FF00FF', '#FFA07A', 
    '#DC143C', '#7B68EE', '#00FF7F', '#FF69B4', '#008080', '#FFD700', '#4169E1', 
    '#8B0000', '#32CD32', '#800080'
]

plt.figure(figsize=(24, 16))

squarify.plot(sizes=counts, label=topics, color=color_palette, alpha=0.8)

plt.title('Emerging Trends in Technology', fontsize=26, fontweight='bold', pad=30)
plt.axis('off')

plt.show()