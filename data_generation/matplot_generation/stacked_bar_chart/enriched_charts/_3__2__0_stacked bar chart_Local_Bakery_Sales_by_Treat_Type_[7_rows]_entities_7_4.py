
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
destinations_sales = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
nature_sales = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
adventure_sales = [70, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185]

fig, ax = plt.subplots(figsize=(12, 10))

bars_destinations = plt.barh(months, destinations_sales, color='#1E88E5', edgecolor='white', height=0.5, label='Destinations')
bars_nature = plt.barh(months, nature_sales, left=destinations_sales, color='#FBC02D', edgecolor='white', height=0.5, label='Nature')
bars_adventure = plt.barh(months, adventure_sales, left=[i+j for i,j in zip(destinations_sales, nature_sales)], color='#8E24AA', edgecolor='white', height=0.5, label='Adventure')

ax.set_xlabel('Number of Visitors')
ax.set_title('Monthly Visitor Data for Travel Destinations in 2024', pad=20)
ax.set_yticks(range(len(months)), labels=months)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Types of Destinations')

for bars in [bars_destinations, bars_nature, bars_adventure]:
    for bar in bars:
        width = bar.get_width()
        plt.text(bar.get_x() + width/2, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='center', color='black', fontweight='bold')

plt.margins(y=0.1)

plt.show()