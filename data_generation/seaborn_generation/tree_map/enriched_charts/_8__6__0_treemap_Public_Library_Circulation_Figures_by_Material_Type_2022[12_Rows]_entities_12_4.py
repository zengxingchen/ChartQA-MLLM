
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Category': ['Movies', 'TV Shows', 'Books', 'Video Games', 'Music', 'Podcasts', 
                 'Theater', 'Concerts', 'Festivals', 'Comics', 'Online Streaming', 'Live Sports'],
    'Percentage': [0.10, 0.15, 0.12, 0.08, 0.10, 0.05, 0.06, 0.07, 0.05, 0.04, 0.06, 0.12]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF6347', '#FFA07A', '#20B2AA', '#8A2BE2', '#5F9EA0', '#7FFF00', 
          '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#00008B']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Entertainment & Leisure Categories', fontsize=24, pad=20)
plt.axis('off')
plt.show()