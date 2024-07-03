
import matplotlib.pyplot as plt

locations = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Berlin', 'London', 'Moscow', 'Rio de Janeiro', 'Toronto', 'Rome', 'Dubai', 'Beijing', 'Mumbai', 'Bangkok', 'Seoul', 'Buenos Aires', 'Cape Town', 'Istanbul', 'Singapore', 'Los Angeles', 'San Francisco', 'Hong Kong', 'Melbourne', 'Amsterdam']
happiness_index = [7.4, 6.8, 7.2, 7.8, 7.0, 6.9, 5.8, 6.2, 7.5, 7.1, 6.6, 6.4, 6.0, 6.7, 7.3, 6.5, 6.1, 6.3, 7.7, 7.6, 7.9, 7.0, 7.4, 7.5]
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC', '#8B0000', '#E9967A', '#8FBC8F', '#483D8B', '#2F4F4F', '#9400D3', '#FFD700']

plt.figure(figsize=(14, 8))
plt.barh(locations, happiness_index, color=colors, height=0.5)
plt.xlabel('Happiness Index')
plt.title('Happiness Index by City')
plt.xlim(5, max(happiness_index) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()