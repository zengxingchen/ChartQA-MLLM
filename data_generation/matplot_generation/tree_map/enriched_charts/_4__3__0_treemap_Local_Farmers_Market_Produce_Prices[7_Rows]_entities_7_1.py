
import matplotlib.pyplot as plt
import squarify

# Data points
topics = ['Artificial Intelligence', 'Blockchain', 'Quantum Computing', 'Nanotechnology', '3D Printing', 
          'Autonomous Vehicles', 'Renewable Energy', 'Augmented Reality', 'Virtual Reality', '5G Technology', 
          'Biotechnology', 'Cybersecurity', 'Internet of Things', 'Wearable Technology', 'Robotics', 
          'Big Data', 'Smart Cities', 'Genomics', 'Edge Computing', 'Others']
percentages = [18.5, 12.0, 9.0, 7.5, 8.5, 11.0, 15.5, 6.8, 10.5, 14.0, 13.2, 8.9, 16.5, 5.7, 7.8, 10.3, 9.6, 4.5, 6.2, 3.9]

# Color scheme
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733',
          '#C70039', '#900C3F', '#581845', '#D3D3D3']

plt.figure(figsize=(16, 12))
squarify.plot(sizes=percentages, label=topics, color=colors, alpha=0.8)

# Chart details
plt.title('Emerging Technologies in 2024', fontsize=22, pad=30)
plt.axis('off')

plt.show()