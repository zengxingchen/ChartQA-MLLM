
import matplotlib.pyplot as plt
import squarify

# Data for movie genres' market share
genres = ['Action', 'Drama', 'Comedy', 'Thriller', 'Romance', 'Adventure', 'Fantasy', 'Animation', 'Documentary', 'Family', 'Horror']
market_share = [21.0, 18.0, 16.0, 10.0, 8.0, 7.0, 6.0, 5.0, 3.0, 2.0, 4.0]

# Custom color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33FF', '#33FFF0', '#F033FF', '#FF33A6', '#A633FF', '#FF8C33', '#FFD700']

# Treemap
plt.figure(figsize=(10, 15))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=genres, color=colors, alpha=0.8)
plt.title('Movie Genres Market Share 2021', pad=20)
plt.axis('off')  # No axes for a cleaner look

plt.show()