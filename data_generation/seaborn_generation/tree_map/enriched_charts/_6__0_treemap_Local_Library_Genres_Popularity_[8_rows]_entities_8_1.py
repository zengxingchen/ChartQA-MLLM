
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

# Creating a DataFrame from the provided dataset
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Italy',
                'Brazil', 'Canada', 'South Korea', 'Russia', 'Australia', 'Spain', 'Mexico', 'Indonesia',
                'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland', 'Argentina', 'Sweden', 'Nigeria',
                'Poland', 'Thailand'],
    'GDP': [21427, 14140, 5150, 3846, 2875, 2827, 2716, 2001, 1839, 1643, 1642, 1633, 1393, 1393, 1267, 1119,
            912, 779, 743, 703, 449, 529, 448, 595, 543]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(24, 14))
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33",
          "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62", "#8da0cb",
          "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3", "#ffed6f",
          "#b2df8a", "#fdbf6f", "#cab2d6", "#6a3d9a", "#ff00ff", "#1f78b4", "#b15928"]

# Using squarify to plot treemap
squarify.plot(sizes=df['GDP'], label=df['Country'], color=colors, alpha=0.7)
plt.title('GDP Distribution by Country (in billion USD)', fontsize=24)
plt.axis('off')
plt.show()