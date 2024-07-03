
import matplotlib.pyplot as plt

# Data
fruit = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries',
         'Figs', 'Grapes', 'Honeydews', 'Kiwis', 'Lemons',
         'Mangoes', 'Nectarines', 'Oranges', 'Papayas', 'Quinces',
         'Raspberries', 'Strawberries', 'Tangerines', 'Ugli Fruit', 'Watermelons']
consumption = [86, 153, 4.1, 8.5, 0.15,
               1.1, 77, 6.4, 4.3, 19,
               55, 5.1, 73, 7, 0.6,
               0.8, 9, 10.5, 0.003, 117]

# Create bar chart
plt.figure(figsize=(12, 9))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
          '#ffb3e6', '#ff6666', '#c2f0c2', '#ffb366', '#f0b3ff',
          '#ffccff', '#c266ff', '#ccffcc', '#cc99ff', '#ffcc66',
          '#ff99cc', '#66b2ff', '#ff99e6', '#99ffcc', '#ff6666']

plt.bar(fruit, consumption, color=colors, width=0.7)

# Customizing the plot
plt.ylabel('Consumption in Million Tons')
plt.title('Global Fruit Consumption in Million Tons (2020)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()