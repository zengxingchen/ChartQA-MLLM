
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['AI & Robotics', 'Quantum Computing', '5G Networks', 'Blockchain', 'Virtual Reality',
                 'Augmented Reality', 'IoT Devices', 'Renewable Energy', 'Biotechnology', 'Autonomous Vehicles',
                 'Smart Cities', 'Cybersecurity', 'Wearable Tech', '3D Printing', 'Space Exploration',
                 'Nanotechnology', 'Genetic Engineering', 'Cloud Computing', 'Big Data', 'Drones'],
    'Users': [1200000, 950000, 1100000, 800000, 600000,
              500000, 700000, 900000, 1000000, 850000,
              750000, 650000, 450000, 300000, 400000,
              550000, 350000, 1250000, 1050000, 770000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16,12))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFA6',
          '#A633FF', '#FFA633', '#33A6FF', '#FF5733', '#33FF57',
          '#3357FF', '#FF33A6', '#33FFA6', '#A633FF', '#FFA633',
          '#33A6FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A6']

squarify.plot(sizes=df['Users'], label=df['Category'], color=colors, alpha=0.8)

plt.title('User Distribution Across Future Technologies', fontsize=20)

plt.axis('off')

plt.show()