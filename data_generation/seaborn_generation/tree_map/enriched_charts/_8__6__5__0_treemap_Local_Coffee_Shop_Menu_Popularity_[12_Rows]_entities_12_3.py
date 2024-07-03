
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Topic': ['Artificial Intelligence', 'Quantum Computing', 'Blockchain Technology', 'Internet of Things', '5G Networks',
              'Autonomous Vehicles', 'Virtual Reality', 'Augmented Reality', 'Nanotechnology', 'Biotechnology',
              'Cybersecurity', 'Renewable Energy', 'Smart Cities', 'Space Exploration', 'Wearable Technology',
              'Robotics', '3D Printing', 'Advanced Materials', 'Big Data', 'Edge Computing',
              'Digital Twins', 'Neurotechnology', 'Genomics', 'Smart Agriculture'],
    'Amount (Billions)': [500.0, 450.0, 400.0, 350.0, 320.0,
                          280.0, 260.0, 240.0, 220.0, 200.0,
                          180.0, 160.0, 140.0, 120.0, 100.0,
                          80.0, 70.0, 60.0, 50.0, 40.0,
                          30.0, 20.0, 15.0, 10.0]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
          '#00CED1', '#FF4500', '#DA70D6', '#ADFF2F', '#F0E68C',
          '#CD5C5C', '#9400D3', '#00FA9A', '#5F9EA0', '#FFE4C4',
          '#8B4513', '#DEB887', '#7B68EE', '#48D1CC', '#FF69B4',
          '#B22222', '#DC143C', '#F4A460', '#2E8B57']

# Plotting the Treemap
plt.figure(figsize=(22, 14))
squarify.plot(sizes=df['Amount (Billions)'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Investment in Future Technologies - 2024 (Billions USD)', fontsize=24, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()