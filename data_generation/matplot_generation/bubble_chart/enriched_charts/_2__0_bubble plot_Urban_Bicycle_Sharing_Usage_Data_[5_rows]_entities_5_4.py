
import matplotlib.pyplot as plt

countries = ['United States', 'China', 'India', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'South Africa', 'Argentina', 'Turkey']
GDP_growth = [2.9, 6.1, 5.5, 0.7, 1.4, 1.3, 1.2, 1.1, 0.3, 1.7, 1.3, 2.0, 2.4, 2.3, 5.0, 2.6, 3.4, 0.2, -2.1, 0.9]
life_expectancy = [78.8, 76.9, 69.7, 84.6, 81.2, 81.3, 82.5, 75.9, 83.4, 82.3, 72.6, 83.3, 82.9, 75.1, 71.7, 82.1, 75.4, 64.1, 76.5, 77.4]
populations = [331, 1441, 1380, 126, 83, 67, 65, 213, 60, 38, 146, 52, 26, 128, 273, 17, 35, 60, 45, 84]

size_factor = 0.5
sizes = [p * size_factor for p in populations]

colors = ['#FF6347', '#4682B4', '#9ACD32', '#8A2BE2', '#FF7F50', '#20B2AA', '#87CEEB', '#8B0000', '#FF69B4', '#5F9EA0', '#D2691E', '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#B8860B', '#A9A9A9', '#006400', '#FF8C00', '#9932CC']

plt.figure(figsize=(18,12))
plt.scatter(GDP_growth, life_expectancy, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

plt.title('GDP Growth vs. Life Expectancy with Population Bubble Sizes', pad=20)
plt.xlabel('GDP Growth (%)')
plt.ylabel('Life Expectancy (years)')

for i, country in enumerate(countries):
    plt.text(GDP_growth[i], life_expectancy[i], country, ha='center', va='center', fontsize=8)

plt.tight_layout()
plt.show()