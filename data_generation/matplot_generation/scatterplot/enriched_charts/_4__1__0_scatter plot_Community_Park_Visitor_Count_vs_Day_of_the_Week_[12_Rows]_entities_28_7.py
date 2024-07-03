
import matplotlib.pyplot as plt

# Data
art_pieces = [
    "Mona Lisa", "The Starry Night", "The Persistence of Memory", "Girl with a Pearl Earring",
    "The Scream", "Guernica", "The Night Watch", "American Gothic", 
    "Les Demoiselles d'Avignon", "The Birth of Venus", "The Last Supper", 
    "Sunflowers", "The Kiss", "Whistler's Mother", "The Arnolfini Portrait",
    "The Hay Wain", "The Garden of Earthly Delights", "The School of Athens",
    "The Storm on the Sea of Galilee", "The Swing"
]
years_created = [1503, 1889, 1931, 1665, 1893, 1937, 1642, 1930, 1907, 1486, 1498, 1888, 1908, 1871, 1434, 1821, 1515, 1511, 1633, 1767]
estimated_values = [850, 100, 120, 90, 200, 150, 140, 80, 200, 300, 450, 110, 180, 70, 120, 50, 500, 320, 95, 85]

# Scatter plot
fig, ax = plt.subplots(figsize=(16, 9))  # Change the width and height of the chart
scatter = ax.scatter(
    years_created,
    estimated_values,
    alpha=0.8,
    c=[
        '#FF4500', '#FFD700', '#DAA520', '#8A2BE2', '#5F9EA0',
        '#D2691E', '#DC143C', '#006400', '#8B008B', '#FF1493',
        '#1E90FF', '#32CD32', '#FF6347', '#4682B4', '#800080',
        '#20B2AA', '#CD5C5C', '#4B0082', '#FF8C00', '#9932CC'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Famous Art Pieces: Year Created vs Estimated Value', pad=20)
ax.set_xlabel('Year Created')
ax.set_ylabel('Estimated Value (in millions)')

# Adding the art piece names as labels next to each point
for i, art_piece in enumerate(art_pieces):
    ax.annotate(art_piece, (years_created[i], estimated_values[i]), fontsize=8, ha='right')

plt.show()