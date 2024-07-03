
import matplotlib.pyplot as plt
import squarify

labels = ['France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'United Kingdom', 'Japan', 'Malaysia', 'Russia', 'Canada', 'Australia', 'Greece', 'Brazil', 'India', 'Portugal', 'Vietnam', 'Netherlands', 'Egypt', 'South Korea', 'South Africa', 'Indonesia']
sizes = [82, 81, 79, 63, 62, 51, 49, 39, 38, 37, 32, 26, 24, 22, 21, 19, 18, 17, 15, 13, 12, 11, 10, 9, 8]
colors = ['#FF6347', '#FFA07A', '#20B2AA', '#87CEFA', '#4682B4', '#6A5ACD', '#7B68EE', '#ADFF2F', '#32CD32', '#00FA9A', '#FFD700', '#FF4500', '#FF8C00', '#FF1493', '#8A2BE2', '#BA55D3', '#9370DB', '#8B008B', '#9400D3', '#9932CC', '#8B4513', '#BC8F8F', '#D2691E', '#B8860B', '#CD5C5C']

plt.figure(figsize=(20, 10))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.title('Popular Travel Destinations in 2021', fontsize=18, fontweight='bold', y=0.93)
plt.axis('off')
plt.show()