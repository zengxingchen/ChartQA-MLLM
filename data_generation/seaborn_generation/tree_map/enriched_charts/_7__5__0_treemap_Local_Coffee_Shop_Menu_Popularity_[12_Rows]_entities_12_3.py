
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Country': ['United States', 'China', 'Japan', 'Great Britain', 'ROC', 
                'Australia', 'Netherlands', 'France', 'Germany', 'Italy', 
                'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 
                'South Korea', 'Spain', 'Kenya', 'Jamaica', 'Norway',
                'India', 'Turkey', 'Poland', 'Czech Republic', 'Iran'],
    'Medals': [113, 88, 58, 65, 71, 
               46, 36, 33, 37, 40, 
               24, 21, 20, 15, 20, 
               20, 17, 10, 9, 8,
               7, 13, 14, 11, 7]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94',
          '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#ad494a',
          '#8c6d31', '#e7ba52', '#17becf', '#7b4173', '#6b486b']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Change width and height reasonably
squarify.plot(sizes=df['Medals'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Olympic Medals by Country - 2020 Tokyo Olympics', fontsize=18, fontweight='bold')
plt.axis('off')
plt.show()