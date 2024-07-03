
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Country': ['United States', 'China', 'Japan', 'Great Britain', 'ROC', 
                'Australia', 'Netherlands', 'France', 'Germany', 'Italy', 
                'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 
                'South Korea', 'Poland', 'Czech Republic', 'Kenya', 'Norway',
                'Jamaica', 'Spain', 'Sweden', 'Switzerland', 'Denmark'],
    'Gold Medals': [39, 38, 27, 22, 20, 
                    17, 10, 10, 10, 10, 
                    7, 7, 7, 7, 6, 
                    6, 4, 4, 4, 4,
                    4, 3, 3, 3, 3]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
          '#a55194', '#d6616b', '#6b6ecf', '#e7ba52', '#c7c7c7',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Changed width and height
squarify.plot(sizes=df['Gold Medals'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Top 25 Countries by Olympic Gold Medals in 2021', fontsize=18, fontweight='bold', loc='center')
plt.axis('off')
plt.show()