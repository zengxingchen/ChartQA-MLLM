
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe
data = {
    'Category': ['Lipstick', 'Foundation', 'Mascara', 'Eyeliner', 'Blush', 'Highlighter', 'Concealer', 'Bronzer', 'Primer', 'Setting Spray', 'Brow Pencil', 'Lip Gloss'],
    'Popularity': [30, 25, 20, 15, 10, 8, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#ff7f50', '#6a5acd', '#00fa9a', '#8b0000', '#ffa07a', '#b0e0e6', '#ff69b4', '#dda0dd', '#ffdab9', '#bdb76b', '#cd5c5c', '#8fbc8f']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Popularity'], label=df['Category'], color=colors, alpha=0.8)

# Remove axes
plt.axis('off')

plt.title('Popularity of Makeup Products in 2023', fontsize=18, fontweight='bold', pad=20)
plt.show()