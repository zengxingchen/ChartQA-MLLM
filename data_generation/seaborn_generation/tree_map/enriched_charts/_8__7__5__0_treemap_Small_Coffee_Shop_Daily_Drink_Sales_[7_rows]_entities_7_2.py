
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Category': [
        'Exoplanets', 'Galaxies', 'Black Holes', 'Nebulae', 'Asteroids', 
        'Comets', 'Space Missions', 'Telescopes', 'Cosmology', 'Space Tourism',
        'Astronauts', 'Space Stations', 'Mars Exploration', 'Planetary Science',
        'Rockets', 'Satellite Technology', 'Space Law', 'Dark Matter'
    ],
    'Value': [
        120, 150, 140, 130, 110, 
        100, 90, 80, 115, 95,
        105, 85, 125, 75,
        65, 60, 55, 50
    ]
}

df = pd.DataFrame(data)

colors = [
    '#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#6A5ACD',
    '#FF6347', '#4682B4', '#7FFFD4', '#DA70D6', '#CD5C5C',
    '#FF69B4', '#8B4513', '#3CB371', '#FFA500', '#20B2AA',
    '#778899', '#BDB76B', '#8A2BE2'
]

fig, ax = plt.subplots(1, figsize=(20, 14))

squarify.plot(sizes=df['Value'], label=df['Category'], alpha=0.8, color=colors)

plt.axis('off')

plt.title('Significant Topics in Astronomy & Space Exploration', fontsize=24, y=1.05)

plt.show()