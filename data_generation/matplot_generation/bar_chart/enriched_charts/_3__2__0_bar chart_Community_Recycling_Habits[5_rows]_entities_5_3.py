
import matplotlib.pyplot as plt

# Data
genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical', 'Country', 'Electronic', 'Reggae', 'Blues', 'Folk', 'R&B', 'Latin', 'Soul', 'Metal', 'Punk', 'Disco', 'Funk', 'Gospel', 'Techno', 'Opera']
popularity = [85, 90, 75, 60, 50, 70, 80, 65, 55, 45, 95, 40, 35, 30, 25, 20, 15, 10, 5, 12]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Figure size
plt.figure(figsize=(14, 8))

# Horizontal bar chart
plt.barh(genres, popularity, color=colors, height=0.5)

# Labeling
plt.xlabel('Popularity')
plt.title('Popularity of Music Genres')

# Show and save plot
plt.tight_layout()
plt.show()