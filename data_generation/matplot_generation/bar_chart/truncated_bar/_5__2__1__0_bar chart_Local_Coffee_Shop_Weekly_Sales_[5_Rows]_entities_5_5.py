
import matplotlib.pyplot as plt

countries = [
    "China", "United States", "Brazil", "India", "Germany", "Canada",
    "Russia", "Japan", "Norway", "Spain", "France", "Italy", "Sweden",
    "Australia", "Turkey", "United Kingdom", "Mexico", "South Korea",
    "Vietnam", "Indonesia"
]
renewable_energy_production = [
    2193, 1278, 634, 524, 380, 374, 292, 256, 220, 216, 208, 196, 192,
    181, 178, 174, 162, 158, 154, 148
]

plt.figure(figsize=(16, 10))
plt.bar(countries, renewable_energy_production, color=[
    '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800',
    '#FF5722', '#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5',
    '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A',
    '#CDDC39', '#FFEB3B'], width=0.6)

plt.ylabel('Renewable Energy Production (TWh)', fontsize=14)
plt.title('Top 20 Countries by Renewable Energy Production', fontsize=18, pad=20)
plt.ylim(140, 2200)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()