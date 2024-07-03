
import matplotlib.pyplot as plt

countries = ['Germany', 'South Korea', 'Finland', 'Denmark', 'Singapore', 
             'New Zealand', 'Iceland', 'Ireland', 'Luxembourg', 'Belgium', 
             'Portugal', 'United States']
life_expectancy = [81.2, 83.3, 82.1, 81.4, 84.8, 82.6, 82.9, 82.2, 82.3, 82.0, 81.9, 78.9]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6',
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33',
          '#FF8C33', '#A6FF33']

plt.figure(figsize=(14, 8))
plt.barh(countries, life_expectancy, color=colors, height=0.5)
plt.xlabel('Life Expectancy (Years)')
plt.title('Life Expectancy in Various Countries', pad=20)
plt.xlim(min(life_expectancy) - 1, max(life_expectancy) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()