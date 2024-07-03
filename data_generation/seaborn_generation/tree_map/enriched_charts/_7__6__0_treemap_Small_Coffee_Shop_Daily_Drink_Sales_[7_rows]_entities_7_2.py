
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Topic': [
        'E-commerce', 'Fintech', 'Artificial Intelligence', 'Cryptocurrencies',
        'Green Technology', 'Remote Work Solutions', 'Cloud Computing', 'Cybersecurity',
        'Big Data', 'Robotics', 'Digital Marketing', 'Virtual Reality',
        'Augmented Reality', 'Blockchain', 'Wearable Technology', '5G Networks',
        'Quantum Computing', 'Autonomous Vehicles', 'Biotechnology', 'Gene Editing',
        'Internet of Things', 'Edge Computing', 'Smart Cities', 'Nanotechnology',
        '3D Printing', 'Solar Energy', 'Wind Energy', 'Hydrogen Fuel Cells',
        'Telemedicine'
    ],
    'Popularity': [
        500, 450, 400, 380, 350, 330, 320, 310, 300, 290,
        280, 270, 260, 250, 240, 230, 220, 210, 200, 190,
        180, 170, 160, 150, 140, 130, 120, 110, 100
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', 
    '#c2f0c2', '#ff6666', '#ffb366', '#c2c2d6', '#c2d1f0', '#ff9999', 
    '#ffb3b3', '#99b3ff', '#b3ff99', '#ffb366', '#ff66b3', '#ff99cc', 
    '#c2b3b3', '#b366ff', '#c2f099', '#99ffcc', '#99b3b3', '#b3ffcc', 
    '#ccff99', '#ff99b3', '#cc99ff', '#99ccff', '#ff6699'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(16, 10))

# Create a treemap
squarify.plot(sizes=df['Popularity'], label=df['Topic'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Popularity of Emerging Business Technologies', fontsize=22, pad=20)

# Show the plot
plt.show()