
import matplotlib.pyplot as plt
import numpy as np

countries = [
    'United States', 'China', 'India', 'Germany', 'Japan', 'United Kingdom', 
    'Canada', 'Brazil', 'Australia', 'France', 'Russia', 'South Korea', 
    'Mexico', 'Italy', 'Spain', 'Nigeria', 'Egypt', 'South Africa', 'Indonesia',
    'Argentina', 'Turkey', 'Iran', 'Saudi Arabia', 'Pakistan', 'Bangladesh', 
    'Vietnam', 'Philippines', 'Thailand', 'Ukraine', 'Poland'
]
calorie_consumption = np.array([
    3750, 3000, 2500, 3400, 2700, 3400, 3500, 3200, 3400, 3300, 3200, 2800, 3200, 
    3200, 3200, 2600, 3000, 2900, 2800, 3100, 3200, 3000, 3200, 2400, 2200, 2600, 
    2500, 2700, 2900, 3100
])
obesity_rate = np.array([
    36.2, 6.2, 3.9, 22.3, 4.3, 27.8, 29.4, 22.1, 29.0, 21.6, 23.1, 5.3, 28.9, 
    19.9, 23.8, 8.1, 32.0, 28.3, 6.9, 27.7, 32.1, 21.3, 35.4, 8.1, 4.1, 2.1, 
    6.4, 10.0, 24.6, 23.1
])
population = np.array([
    331, 1402, 1380, 83, 126, 67, 38, 213, 26, 65, 146, 52, 129, 60, 47, 206, 
    104, 60, 273, 45, 85, 83, 35, 225, 164, 97, 109, 70, 41, 38
])

sizes = population * 10

colors = [
    '#FF6347', '#4682B4', '#FFD700', '#DA70D6', '#32CD32', '#1E90FF', '#FF1493', 
    '#7B68EE', '#FF4500', '#2E8B57', '#8A2BE2', '#00CED1', '#FF69B4', '#FFDAB9', 
    '#CD5C5C', '#F08080', '#6495ED', '#D2691E', '#DC143C', '#00FA9A', '#BA55D3', 
    '#FF00FF', '#B22222', '#7FFF00', '#4B0082', '#00FF7F', '#3CB371', '#FFA07A', 
    '#778899', '#6A5ACD'
]

plt.figure(figsize=(18, 10))

scatter = plt.scatter(obesity_rate, calorie_consumption, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

plt.title('Daily Calorie Consumption vs Obesity Rate by Country', pad=40)
plt.xlabel('Obesity Rate (%)')
plt.ylabel('Calorie Consumption (kcal/day)')

for i, country in enumerate(countries):
    plt.annotate(country, (obesity_rate[i], calorie_consumption[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()