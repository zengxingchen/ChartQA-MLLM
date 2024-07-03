
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Category': ['Innovation', 'Investment', 'Electric Vehicles', 'Virtual Reality', 'Space Missions', 'Ethical Debates', 'Quantum Computing', 'Smart Cities', 'Renewable Energy', 'Robotics', '3D Printing', 'Cybersecurity', 'Augmented Reality', 'Biotechnology', 'Drones', 'Nanotechnology', 'Wearable Tech', 'Genomics', 'Big Data', 'Internet of Things'],
    'Value': [95, 85, 78, 70, 90, 65, 85, 75, 80, 90, 60, 85, 70, 85, 60, 75, 65, 75, 80, 70],
    'Aspect': ['Artificial Intelligence', 'Blockchain', 'Electric Vehicles', 'Virtual Reality', 'Space Exploration', 'Ethics in AI', 'Quantum Computing', 'Smart Cities', 'Renewable Energy', 'Advanced Robotics', '3D Printing', 'Cybersecurity', 'Augmented Reality', 'Biotechnology', 'Drones', 'Nanotechnology', 'Wearable Technology', 'Genomics', 'Big Data Analytics', 'Internet of Things']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(18, 14))
cmap = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3', '#ffccff', '#c8e6c9', '#bbdefb', '#ffcdd2', '#d1c4e9', '#b39ddb', '#e57373', '#f06292', '#ba68c8', '#7986cb', '#64b5f6']

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], color=cmap, alpha=0.8)

plt.title('Key Aspects of Future Technologies & Society', fontsize=18, y=1.05)
plt.axis('off')

plt.show()