
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Topic': ['Artificial Intelligence', 'Blockchain Technology', 'Quantum Computing', 'Cybersecurity', 'Augmented Reality', 
              'Virtual Reality', 'Internet of Things', 'Big Data', 'Machine Learning', 'Cloud Computing', 
              'Edge Computing', '5G Technology', 'Biotechnology', 'Genomics', 'Nanotechnology', 
              'Renewable Energy', 'Sustainable Agriculture', 'Space Exploration', 'Smart Cities', 'Autonomous Vehicles', 
              'Advanced Robotics', '3D Printing', 'Digital Twins', 'Quantum Internet', 'Human Augmentation'],
    'Books': [30, 25, 20, 15, 10, 
              18, 22, 24, 28, 26, 
              12, 16, 19, 13, 14, 
              27, 21, 23, 17, 11, 
              29, 9, 8, 7, 6]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#F5B041', '#A569BD',
          '#FF33A2', '#33FFA7', '#FF5733', '#33FF57', '#3357FF',
          '#FF5733', '#33FF57', '#3357FF', '#F5B041', '#A569BD',
          '#FF33A2', '#33FFA7', '#FF5733', '#33FF57', '#3357FF',
          '#FF5733', '#33FF57', '#3357FF', '#F5B041', '#A569BD']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Change width and height reasonably
squarify.plot(sizes=df['Books'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Popular Topics in Future Technologies & Society by Number of Books', fontsize=18, fontweight='bold')
plt.axis('off')
plt.show()