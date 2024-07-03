
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Genre': [
        'Action', 'Adventure', 'RPG', 'Simulation', 'Strategy',
        'Puzzle', 'Racing', 'Sports', 'Misc', 'Platform',
        'Fighting', 'Shooter'
    ],
    'Sales': [
        350, 150, 270, 190, 80,
        120, 200, 230, 210, 160,
        140, 320
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF4500', '#FFD700', '#00FF00', '#00CED1', '#FF1493',
    '#FFA07A', '#B22222', '#228B22', '#8A2BE2', '#FF8C00',
    '#00BFFF', '#483D8B'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=df['Sales'], label=df['Genre'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Global Sales of Video Game Genres', fontsize=18)

# Show the plot
plt.show()