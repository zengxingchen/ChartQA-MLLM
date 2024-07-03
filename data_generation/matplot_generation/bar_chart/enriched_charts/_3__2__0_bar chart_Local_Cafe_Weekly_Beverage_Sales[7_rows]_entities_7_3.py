
import matplotlib.pyplot as plt

countries = ['United States', 'Switzerland', 'Norway', 'Ireland', 'Germany', 'Australia',
             'Canada', 'Finland', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria',
             'Denmark', 'Belgium', 'New Zealand', 'Luxembourg', 'Iceland', 'Israel',
             'Czech Republic', 'Japan']
gdp_per_capita = [63000, 82300, 75300, 78800, 46000, 55800, 51500, 48900, 52400, 53700,
                  43000, 51700, 61700, 48800, 42600, 118000, 59400, 43000, 28000, 42000]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173', 
          '#6b6ecf', '#b5cf6b', '#e7ba52', '#d6616b', '#ce6dbd']

plt.figure(figsize=(14, 8))
plt.bar(countries, gdp_per_capita, color=colors, edgecolor='black', width=0.6)

plt.xlabel('Country', fontsize=12)
plt.ylabel('GDP per Capita (in USD)', fontsize=12)
plt.title('GDP per Capita by Country in 2021', fontsize=16, pad=20)
plt.ylim(25000, 125000)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()