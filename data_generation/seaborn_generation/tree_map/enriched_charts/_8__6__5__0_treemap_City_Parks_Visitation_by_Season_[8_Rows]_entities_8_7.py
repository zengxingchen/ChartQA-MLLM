
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe
data = {
    'Category': ['Berries', 'Citrus', 'Tropical', 'Stone Fruits', 'Pome Fruits', 'Melons', 'Grapes', 'Exotic', 'Dried Fruits', 'Nuts', 'Seeds'],
    'Market Share': [25, 15, 20, 10, 8, 5, 7, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#ff7f7f', '#ffbf7f', '#ffff7f', '#bfff7f', '#7fffbf', '#7fffff', '#7fbfff', '#7f7fff', '#bf7fff', '#ff7fff', '#ff7fbf']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Market Share'], label=df['Category'], color=colors, alpha=0.8)

plt.axis('off')
plt.title('Market Share of Fruit Categories in 2023', fontsize=18, pad=20)
plt.show()