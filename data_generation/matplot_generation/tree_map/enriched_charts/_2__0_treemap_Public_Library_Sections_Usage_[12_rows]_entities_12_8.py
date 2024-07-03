
import matplotlib.pyplot as plt
import squarify

# Data for music artists' market share
artists = ['Ed Sheeran', 'Adele', 'BTS', 'Taylor Swift', 'Drake', 'Billie Eilish', 'The Weeknd', 'Post Malone', 'Justin Bieber', 'Ariana Grande', 'Others']
market_share = [15.0, 12.0, 10.8, 9.5, 8.3, 7.1, 6.9, 5.2, 5.1, 4.8, 15.3]

# Custom color scheme
colors = ['#DAA520', '#FF4500', '#1E90FF', '#9370DB', '#32CD32', '#FF1493', '#8A2BE2', '#FF7F50', '#87CEEB', '#6495ED', '#40E0D0']

# Treemap
plt.figure(figsize=(14, 10))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=artists, color=colors, alpha=0.8)
plt.title('Top Music Artists Market Share Q1 2023', fontsize=15)
plt.axis('off')  # No axes for a cleaner look

plt.show()