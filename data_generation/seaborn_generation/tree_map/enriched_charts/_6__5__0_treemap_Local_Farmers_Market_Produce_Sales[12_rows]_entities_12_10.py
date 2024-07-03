
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Topic': [
        'Artificial Intelligence', 'Blockchain Technology', 'Quantum Computing', 
        'Renewable Energy', 'Virtual Reality', 'Augmented Reality', 
        '3D Printing', 'Genetic Engineering', 'Nanotechnology', 
        'Cybersecurity', 'Robotics', 'Internet of Things', 
        'Big Data', 'Autonomous Vehicles'
    ],
    'Value': [
        1200, 850, 300, 950, 420, 380, 270, 620, 480, 750, 540, 690, 880, 520
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF6347', '#FFD700', '#FF4500', '#ADFF2F', '#00FA9A', '#00CED1', 
    '#1E90FF', '#BA55D3', '#FF69B4', '#FFA07A', '#7CFC00', '#6495ED', 
    '#DC143C', '#8A2BE2'
]

# Define size of the figure
plt.figure(figsize=(20, 12))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Value'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Prominent Future Technologies by Value (in Millions)', fontsize=24)
plt.axis('off')
plt.show()