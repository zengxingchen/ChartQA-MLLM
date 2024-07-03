
import matplotlib.pyplot as plt

# Data
art_pieces = [
    "Mona Lisa", "The Starry Night", "The Persistence of Memory", "Girl with a Pearl Earring",
    "The Scream", "Guernica", "The Night Watch", "American Gothic", 
    "Les Demoiselles d'Avignon", "The Birth of Venus", "The Last Supper", 
    "Sunflowers", "The Kiss", "Whistler's Mother", "The Arnolfini Portrait"
]
years_created = [1503, 1889, 1931, 1665, 1893, 1937, 1642, 1930, 1907, 1486, 1498, 1888, 1908, 1871, 1434]
estimated_values = [850, 100, 120, 90, 200, 150, 140, 80, 200, 300, 450, 110, 180, 70, 120]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change the width and height of the chart
scatter = ax.scatter(
    years_created,
    estimated_values,
    alpha=0.8,
    c=[
        '#FF6347', '#4682B4', '#FFA07A', '#20B2AA', '#8470FF',
        '#FF69B4', '#8A2BE2', '#00FA9A', '#CD3333', '#FF4500',
        '#DA70D6', '#1E90FF', '#32CD32', '#800080', '#40E0D0'
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