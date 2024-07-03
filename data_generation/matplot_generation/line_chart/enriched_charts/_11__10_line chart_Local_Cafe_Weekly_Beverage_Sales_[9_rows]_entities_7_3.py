
import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Protein Shakes': 120, 'Green Smoothies': 140, 'Energy Drinks': 80, 'Detox Juices': 100, 'Herbal Teas': 90},
    {'Day': 'Tuesday', 'Protein Shakes': 130, 'Green Smoothies': 135, 'Energy Drinks': 85, 'Detox Juices': 95, 'Herbal Teas': 85},
    {'Day': 'Wednesday', 'Protein Shakes': 115, 'Green Smoothies': 130, 'Energy Drinks': 75, 'Detox Juices': 110, 'Herbal Teas': 100},
    {'Day': 'Thursday', 'Protein Shakes': 140, 'Green Smoothies': 145, 'Energy Drinks': 95, 'Detox Juices': 120, 'Herbal Teas': 105},
    {'Day': 'Friday', 'Protein Shakes': 150, 'Green Smoothies': 150, 'Energy Drinks': 100, 'Detox Juices': 130, 'Herbal Teas': 110},
    {'Day': 'Saturday', 'Protein Shakes': 160, 'Green Smoothies': 160, 'Energy Drinks': 110, 'Detox Juices': 140, 'Herbal Teas': 115},
    {'Day': 'Sunday', 'Protein Shakes': 155, 'Green Smoothies': 155, 'Energy Drinks': 105, 'Detox Juices': 135, 'Herbal Teas': 120}
]

days = [item['Day'] for item in data]
protein_shakes_sales = [item['Protein Shakes'] for item in data]
green_smoothies_sales = [item['Green Smoothies'] for item in data]
energy_drinks_sales = [item['Energy Drinks'] for item in data]
detox_juices_sales = [item['Detox Juices'] for item in data]
herbal_teas_sales = [item['Herbal Teas'] for item in data]

plt.figure(figsize=(14, 10))
plt.plot(days, protein_shakes_sales, label='Protein Shakes', linestyle='-', marker='o', color='#1f77b4')
plt.plot(days, green_smoothies_sales, label='Green Smoothies', linestyle='--', marker='s', color='#ff7f0e')
plt.plot(days, energy_drinks_sales, label='Energy Drinks', linestyle='-.', marker='^', color='#2ca02c')
plt.plot(days, detox_juices_sales, label='Detox Juices', linestyle=':', marker='D', color='#d62728')
plt.plot(days, herbal_teas_sales, label='Herbal Teas', linestyle='-', marker='*', color='#9467bd')

plt.title('Weekly Beverage Sales', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Drinks Sold')
plt.legend(loc='upper right')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

for i, txt in enumerate(detox_juices_sales):
    plt.annotate(txt, (days[i], detox_juices_sales[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()