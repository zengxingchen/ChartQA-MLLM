
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Category': [
        'Impressionism', 'Cubism', 'Surrealism', 'Abstract', 'Realism',
        'Baroque', 'Renaissance', 'Pop Art', 'Dada', 'Expressionism',
        'Neoclassicism', 'Romanticism'
    ],
    'Value': [
        450, 300, 400, 350, 320,
        250, 380, 290, 210, 270,
        340, 310
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF5733', '#33FFBD', '#3375FF', '#FF33F6', '#75FF33',
    '#FFA533', '#A533FF', '#FF3333', '#33FF57', '#FF5733',
    '#33A5FF', '#57FF33'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Popularity of Art Movements', fontsize=20, y=1.05)

# Show the plot
plt.show()