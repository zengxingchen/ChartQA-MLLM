
import matplotlib.pyplot as plt

countries = [
    'United States', 'Switzerland', 'Norway', 'Ireland', 'Germany', 'Australia',
    'Canada', 'Finland', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria',
    'Denmark', 'Belgium', 'New Zealand', 'Luxembourg', 'Iceland', 'Israel',
    'Czech Republic', 'Japan', 'Singapore', 'South Korea', 'France', 'Italy',
    'Spain', 'Portugal', 'Poland', 'Greece', 'Hungary', 'Slovakia'
]
gdp_per_capita = [
    63000, 85000, 79000, 81000, 50000, 58000, 52000, 49000, 54000, 56000,
    45000, 52000, 63000, 50000, 46000, 120000, 61000, 45000, 32000, 43000,
    95000, 42000, 47000, 42000, 39000, 37000, 32000, 29000, 30000, 29000
]

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#637939', 
    '#8c6d31', '#843c39', '#7b4173', '#6b6ecf', '#b5cf6b', '#e7ba52', 
    '#d6616b', '#ce6dbd', '#ff9896', '#98df8a', '#ffbb78', '#c49c94',
    '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#8c564b', '#17becf'
]

plt.figure(figsize=(10, 14))
plt.barh(countries, gdp_per_capita, color=colors, edgecolor='black', height=0.6)

plt.ylabel('Country', fontsize=12)
plt.xlabel('GDP per Capita (in USD)', fontsize=12)
plt.title('GDP per Capita by Country in 2021', fontsize=16, pad=20)
plt.xlim(25000, 125000)

plt.tight_layout()
plt.show()