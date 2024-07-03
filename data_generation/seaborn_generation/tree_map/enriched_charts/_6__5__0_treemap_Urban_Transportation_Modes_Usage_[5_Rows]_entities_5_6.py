
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Genre': ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip Hop', 'Country', 'Reggae', 'Blues', 'Electronic', 'Latin', 'Folk', 'Metal', 'Opera', 'R&B', 'Gospel', 'World'],
    'Revenue': [350, 300, 250, 200, 230, 180, 170, 160, 210, 190, 140, 150, 120, 220, 130, 110]
})

# Custom colors for the treemap
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFDD', '#FFA533', '#8D33FF', '#FF338B', '#33FFA5', '#FF8633', '#4B33FF', '#FF336B', '#A5FF33', '#338BFF', '#FFCC33']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Revenue'], label=df['Genre'], color=colors, alpha=0.8)

plt.title("Revenue Distribution in Music & Performing Arts by Genre", fontsize=26, fontweight='bold', pad=20)
plt.axis('off')  # Disable the axis

plt.show()