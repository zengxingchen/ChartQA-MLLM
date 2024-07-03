
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Define the data
data = {
    'Platform': [
        'Artificial Intelligence Assistants', 'Smart Home Devices', 'Blockchain Applications',
        'Virtual Reality Platforms', 'Augmented Reality Platforms', 'Wearable Technology',
        '5G Networks', 'Autonomous Vehicles', 'Quantum Computing', 'Renewable Energy Solutions',
        'Genetic Editing Technologies', 'Space Exploration Technologies', 'Robotics', 'Internet of Things (IoT)'
    ],
    'Users (Millions)': [
        2000, 1500, 1200, 900, 850, 700, 600, 500, 300, 250, 200, 150, 100, 50
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#ff9896',
    '#c5b0d5', '#c49c94'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Users (Millions)'], label=df['Platform'], color=colors, alpha=0.8)

plt.title('Active Users of Future Technologies & Platforms (in Millions)', fontsize=22)
plt.axis('off')
plt.show()