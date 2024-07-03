
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Rock Music', 'Pop Music', 'Classical Music', 'Jazz', 'Hip Hop', 
              'Electronic Dance Music', 'Country Music', 'Reggae', 'Blues', 
              'Opera', 'Folk Music', 'Musical Theater', 'Film Scores', 
              'Latin Music', 'Indie Music', 'World Music', 'Punk Rock', 
              'Heavy Metal', 'R&B']
count = [1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 350, 300, 250, 200, 150, 100, 50]

# TreeMap customization
color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                 '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
                 '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173', 
                 '#a55194', '#637939', '#bcbd22', '#17becf']
plt.figure(figsize=(18, 10))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Music & Performing Arts Genres by Popularity', fontsize=20, fontweight='bold')
plt.axis('off')

plt.show()