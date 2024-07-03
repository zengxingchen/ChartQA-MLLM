
import matplotlib.pyplot as plt
import numpy as np

countries = ['United States', 'China', 'India', 'Russia', 'Japan', 'Germany', 
             'Canada', 'Brazil', 'Australia', 'France', 'United Kingdom', 
             'South Korea', 'Italy', 'Mexico', 'Indonesia']
expenditure = np.array([7500, 5000, 1500, 1800, 2200, 2000, 1200, 1100, 900, 2100, 2300, 1700, 1600, 950, 800])
gdp = np.array([21429, 14342, 2875, 1689, 5082, 3846, 1736, 1839, 1390, 2715, 2829, 1664, 2076, 1232, 1100])
population = np.array([331, 1402, 1380, 146, 126, 83, 38, 213, 26, 65, 68, 51, 60, 127, 273])

sizes = population * 10

colors = ['#FF6347', '#4682B4', '#6A5ACD', '#20B2AA', '#FFD700', '#FF69B4', 
          '#8A2BE2', '#FF4500', '#7CFC00', '#6495ED', '#FF1493', '#00CED1', 
          '#FF8C00', '#B22222', '#ADFF2F']

plt.figure(figsize=(16, 9))

scatter = plt.scatter(gdp, expenditure, s=sizes, c=colors, alpha=0.7, edgecolors="w", linewidth=2)

plt.title('Annual Government Expenditure vs GDP by Country', pad=20)
plt.xlabel('GDP (in billions USD)')
plt.ylabel('Government Expenditure (in billions USD)')

for i, country in enumerate(countries):
    plt.annotate(country, (gdp[i], expenditure[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()