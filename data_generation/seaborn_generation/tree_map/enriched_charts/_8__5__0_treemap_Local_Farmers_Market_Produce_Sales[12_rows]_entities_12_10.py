
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Genre': [
        'Rock', 'Pop', 'Hip-Hop', 'Classical', 'Jazz', 'Blues', 'Electronic', 'Country', 
        'Reggae', 'Folk', 'Soul', 'Heavy Metal', 'Punk', 'Disco', 'Latin', 'R&B', 
        'Gospel', 'Opera', 'Dance', 'Funk', 'K-Pop'
    ],
    'Popularity (Millions)': [
        800, 900, 750, 400, 350, 300, 600, 500, 200, 150, 250, 100, 180, 120, 320, 280, 140, 60, 220, 170, 450
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#E74C3C', '#9B59B6', 
    '#3498DB', '#1ABC9C', '#2ECC71', '#F39C12', '#D35400', '#C0392B', 
    '#2980B9', '#8E44AD', '#27AE60', '#16A085', '#2C3E50', '#7F8C8D', 
    '#BDC3C7', '#E67E22', '#5D6D7E'
]

# Define size of the figure
plt.figure(figsize=(20, 12))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Popularity (Millions)'], label=df['Genre'], color=colors, alpha=0.8)

plt.title('Music Genres by Popularity (in Millions)', fontsize=24, fontweight='bold')
plt.axis('off')
plt.show()