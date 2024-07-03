
import matplotlib.pyplot as plt
import squarify

genres = [
    'Rock', 'Pop', 'Jazz', 'Classical', 'HipHop', 'Country', 'Reggae',
    'Blues', 'Electronic', 'R&B', 'Metal', 'Folk', 'Latin', 'Soul', 
    'Gospel', 'Punk', 'Disco', 'Opera', 'Indie', 'KPop', 'World', 
    'Ska', 'NewAge', 'Alternative', 'House'
]

count = [
    1500, 1300, 1100, 900, 850, 800, 750, 700, 650, 600, 550, 500, 
    450, 400, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50
]

color_palette = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA6', '#FF8C33', 
    '#3385FF', '#85FF33', '#FF3333', '#33FFC4', '#A6FF33', '#FF3385', '#338AFF', 
    '#D433FF', '#33FF8C', '#FF6F33', '#3333FF', '#33FFDB', '#B533FF', '#33FF57', 
    '#5733FF', '#FFB833', '#33A1FF', '#FF33D4'
]

plt.figure(figsize=(22, 14))

squarify.plot(sizes=count, label=genres, color=color_palette, alpha=0.8)

plt.title('Popular Music Genres Distribution in the Market', fontsize=26, fontweight='bold', pad=30)
plt.axis('off')

plt.show()