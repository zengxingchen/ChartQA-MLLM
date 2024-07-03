
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Technology': [
        'Artificial Intelligence', 'Quantum Computing', '5G Networks', 'Blockchain',
        'Augmented Reality', 'Virtual Reality', 'Biotechnology', 'Autonomous Vehicles',
        'Internet of Things', 'Wearable Technology', 'Nanotechnology', 'Robotics',
        '3D Printing', 'Solar Energy', 'Wind Energy', 'Hydrogen Fuel Cells',
        'Smart Cities', 'Edge Computing', 'Gene Editing', 'Cryptocurrencies'
    ],
    'AdoptionRate': [
        320, 180, 270, 210, 160, 200, 250, 230, 300, 190,
        140, 220, 260, 280, 240, 230, 260, 210, 250, 300
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF6347', '#FFD700', '#8A2BE2', '#FF4500', '#7FFFD4',
    '#4682B4', '#40E0D0', '#DA70D6', '#FF7F50', '#ADFF2F',
    '#FF69B4', '#BA55D3', '#F08080', '#48D1CC', '#B0E0E6',
    '#32CD32', '#FA8072', '#BDB76B', '#FF1493', '#00FA9A'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(14, 9))

# Create a treemap
squarify.plot(sizes=df['AdoptionRate'], label=df['Technology'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Predicted Adoption Rates of Emerging Technologies', fontsize=20, pad=20)

# Show the plot
plt.show()