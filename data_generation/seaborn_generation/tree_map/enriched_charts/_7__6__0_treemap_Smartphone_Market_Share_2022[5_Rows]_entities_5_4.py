
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Topic': ['Future Technologies & Society'] * 18,
    'Subtopic': ['Artificial Intelligence', 'Quantum Computing', 'Virtual Reality', 'Blockchain', '5G Networks', 
                 'Smart Cities', 'Internet of Things', 'Renewable Energy', 'Autonomous Vehicles', 'Space Tourism', 
                 'Genetic Engineering', 'Cybersecurity', 'Augmented Reality', 'Robotics', 'Nanotechnology', 
                 '3D Printing', 'Smart Homes', 'Drone Technology'],
    'Value': [9000, 8500, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', 
          '#c49c94', '#f7b6d2', '#c7c7c7']

# Create a figure with a defined size
plt.figure(figsize=(20, 12))

# Plot
squarify.plot(sizes=df['Value'], label=df['Subtopic'], color=colors, alpha=0.8)
plt.title('Emerging Trends in Future Technologies & Society', fontsize=24, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()