
import matplotlib.pyplot as plt

countries = ['China', 'India', 'USA', 'Indonesia', 'Brazil', 'Russia', 'Japan', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'Australia', 'South Korea', 'Mexico', 'Spain']
life_expectancy = [76.9, 69.7, 78.6, 71.7, 75.5, 72.4, 84.5, 81.0, 82.3, 81.2, 83.4, 82.3, 82.9, 82.7, 75.4, 83.6]

colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#FF1493', '#00CED1', '#32CD32', '#FFD700', '#DC143C', '#8A2BE2']

plt.figure(figsize=(12, 8))
plt.barh(countries, life_expectancy, color=colors, height=0.5)
plt.xlabel('Life Expectancy (Years)')
plt.title('Life Expectancy by Country')
plt.xlim(65, max(life_expectancy) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()