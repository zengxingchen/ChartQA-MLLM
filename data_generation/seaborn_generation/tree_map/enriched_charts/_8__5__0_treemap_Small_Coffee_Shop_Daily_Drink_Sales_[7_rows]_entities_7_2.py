
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Topic': [
        'Artificial Intelligence', 'Quantum Computing', 'Biotechnology', 'Renewable Energy', 'Space Exploration',
        'Virtual Reality', 'Cybersecurity', 'Blockchain', '3D Printing', 'Robotics', 
        'Nanotechnology', 'Genomics'
    ],
    'Values': [
        300, 200, 250, 400, 350,
        150, 320, 180, 140, 260,
        170, 220
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#1E90FF', '#FF4500', '#32CD32', '#FFD700', '#6A5ACD',
    '#FF69B4', '#8A2BE2', '#FF6347', '#7FFF00', '#20B2AA',
    '#ADFF2F', '#FF1493'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=df['Values'], label=df['Topic'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Impact of Future Technologies on Society', fontsize=24)

# Show the plot
plt.show()