import matplotlib.pyplot as plt

countries = ['Japan', 'Switzerland', 'Australia', 'Italy', 'Sweden', 
             'Canada', 'France', 'Spain', 'Norway', 'Netherlands', 
             'United Kingdom', 'Austria']
life_expectancy = [84.2, 83.4, 82.8, 82.5, 82.4, 82.3, 82.2, 82.1, 82.1, 82.0, 81.9, 81.8]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6',
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33',
          '#FF8C33', '#A6FF33']

plt.figure(figsize=(12, 6))
plt.bar(countries, life_expectancy, color=colors, width=0.6)
plt.ylabel('Life Expectancy (Years)')
plt.title('Life Expectancy in Various Countries')
plt.ylim(80, max(life_expectancy) + 2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.show()