import matplotlib.pyplot as plt
import squarify

# Dataset
countries = [
    'USA', 'UK', 'Canada', 'Australia', 'India', 'Germany', 'France', 'Italy',
    'Spain', 'China', 'Japan', 'Russia', 'Brazil', 'Mexico', 'South Africa',
    'South Korea', 'Turkey', 'Argentina', 'Netherlands', 'Sweden', 'Norway',
    'Finland', 'Denmark', 'Switzerland', 'Belgium', 'Austria', 'New Zealand',
    'Ireland', 'Poland', 'Greece'
]
books_read_per_year = [
    12.1, 11.5, 10.9, 10.4, 9.8, 9.4, 8.9, 8.3, 7.7, 7.5, 7.2, 6.8, 6.4, 5.9,
    5.5, 5.3, 4.9, 4.7, 4.4, 4.1, 3.9, 3.7, 3.4, 3.2, 2.9, 2.7, 2.5, 2.3, 2.1, 1.9
]

# Color Scheme
colors = [
    '#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#FF69B4', '#8A2BE2', '#00FA9A', 
    '#FF6347', '#4682B4', '#DA70D6', '#7FFF00', '#D2691E', '#FF1493', '#B0C4DE',
    '#20B2AA', '#FF7F50', '#5F9EA0', '#ADFF2F', '#FF00FF', '#9ACD32', '#F08080',
    '#D2B48C', '#FFA500', '#BC8F8F', '#BDB76B', '#2E8B57', '#CD5C5C', '#00CED1',
    '#F5DEB3', '#A52A2A'
]

plt.figure(figsize=(16, 12))

# Creating the treemap
squarify.plot(sizes=books_read_per_year, label=countries, color=colors, alpha=0.8)

# Adding a title
plt.title('Annual Books Read Per Capita by Country', fontsize=18, weight='bold', y=1.03)

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()