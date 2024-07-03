
import matplotlib.pyplot as plt

countries = ['United States', 'China', 'India', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'South Africa', 'Argentina', 'Turkey']
veg_consumption = [120, 180, 150, 200, 175, 160, 170, 140, 190, 165, 130, 155, 145, 135, 100, 185, 90, 110, 125, 105]
happiness_index = [6.9, 5.5, 4.0, 7.5, 7.0, 6.8, 6.7, 6.2, 7.1, 7.4, 5.2, 6.6, 7.3, 6.0, 5.0, 7.2, 6.1, 5.3, 6.4, 5.9]
populations = [331, 1441, 1380, 126, 83, 67, 65, 213, 60, 38, 146, 52, 26, 128, 273, 17, 35, 60, 45, 84]

size_factor = 0.5
sizes = [p * size_factor for p in populations]

colors = ['#FF4500', '#1E90FF', '#32CD32', '#800080', '#FF6347', '#4682B4', '#6A5ACD', '#FF1493', '#FF8C00', '#40E0D0', '#DA70D6', '#8B4513', '#7B68EE', '#8A2BE2', '#5F9EA0', '#DC143C', '#7FFF00', '#FF69B4', '#FFD700', '#CD5C5C']

plt.figure(figsize=(20,14))
plt.scatter(veg_consumption, happiness_index, s=sizes, c=colors, alpha=0.7, edgecolors='w', linewidth=0.5)

plt.title('Vegetable Consumption vs. Happiness Index with Population Bubble Sizes', pad=30)
plt.xlabel('Vegetable Consumption (kg/year)')
plt.ylabel('Happiness Index')

for i, country in enumerate(countries):
    plt.text(veg_consumption[i], happiness_index[i], country, ha='center', va='center', fontsize=9)

plt.tight_layout()
plt.show()