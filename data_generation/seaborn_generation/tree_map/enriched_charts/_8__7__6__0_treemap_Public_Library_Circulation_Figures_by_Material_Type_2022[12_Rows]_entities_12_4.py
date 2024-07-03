
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Category': ['Books', 'Movies', 'Music', 'Theater', 'TV Shows', 'Podcasts', 
                 'Video Games', 'Board Games', 'Concerts', 'Sports Events', 
                 'Art Exhibitions', 'Festivals', 'Amusement Parks', 'Escape Rooms', 
                 'Street Performances'],
    'Percentage': [0.12, 0.11, 0.10, 0.09, 0.08, 0.08, 0.07, 0.06, 0.05, 0.05, 
                   0.04, 0.04, 0.03, 0.02, 0.01]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFD5', 
          '#FF8C33', '#FF3333', '#8C33FF', '#33FF83', '#FF5733', '#57FF33', 
          '#5733FF', '#FF33A1', '#33A1FF']

# Plot the Treemap
plt.figure(figsize=(18, 14))
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Popular Entertainment & Leisure Activities', fontsize=26, pad=30)
plt.axis('off')
plt.show()