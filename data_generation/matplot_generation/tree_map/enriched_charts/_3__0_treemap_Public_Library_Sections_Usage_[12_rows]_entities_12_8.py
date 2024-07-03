
import matplotlib.pyplot as plt
import squarify

# Data for music genres' market share
genres = ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Country', 'Electronic', 'R&B', 'Reggae', 'Soul', 'Blues', 'Latin', 'Metal', 'Punk', 'Folk', 'Dance', 'Other']
market_share = [15.5, 14.8, 13.2, 8.1, 7.4, 6.0, 5.5, 5.2, 3.7, 2.6, 2.3, 1.9, 1.5, 1.4, 1.2, 1.0, 8.7]

# Custom color scheme
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFA500', '#800080', '#FFD700', '#A52A2A', '#8B4513', '#2E8B57', '#006400', '#8B0000', '#4B0082', '#FF1493', '#7FFFD4']

# Treemap
plt.figure(figsize=(14, 10))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=genres, color=colors, alpha=0.7)
plt.title('Music Genre Market Share 2021', fontsize=18)
plt.axis('off')  # No axes for a cleaner look

plt.show()