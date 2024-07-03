
import matplotlib.pyplot as plt
import squarify

# Data points
countries = [
    'USA', 'China', 'Japan', 'Great Britain', 'ROC', 'Australia', 'Netherlands', 'France',
    'Germany', 'Italy', 'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 'South Korea',
    'Poland', 'Czech Republic', 'Kenya', 'Norway', 'Jamaica', 'Spain', 'Sweden', 'Switzerland',
    'Denmark', 'Croatia', 'Iran', 'Serbia', 'Belgium', 'Bulgaria'
]
gold_medals = [
    39, 38, 27, 22, 20, 17, 10, 10,
    10, 10, 7, 7, 7, 7, 6, 6,
    4, 4, 4, 4, 4, 3, 3, 3,
    3, 3, 3, 3, 3, 3
]
colors = [
    '#FFD700', '#FF0000', '#1F77B4', '#2CA02C', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F',
    '#BCBD22', '#17BECF', '#FF7F0E', '#1F77B4', '#2CA02C', '#D62728', '#9467BD', '#8C564B',
    '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#FF7F0E', '#1F77B4', '#2CA02C', '#D62728',
    '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF'
]

# Plot Dimensions
plt.figure(figsize=(18, 14))

# Create a treemap
squarify.plot(sizes=gold_medals, label=countries, color=colors, alpha=0.8)

# Title
plt.title('Gold Medals Won in Tokyo 2020 Olympics', fontsize=18, y=1.05)

# Remove axes
plt.axis('off')

# Show plot
plt.show()