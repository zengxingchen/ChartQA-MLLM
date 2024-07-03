
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
smartphones_sales = [180, 190, 210, 200, 220, 230, 250, 260, 270, 280, 290, 300]
tablets_sales = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
laptops_sales = [200, 220, 240, 230, 250, 270, 280, 300, 320, 330, 350, 360]

fig, ax = plt.subplots(figsize=(10, 12))

bars_smartphones = plt.bar(months, smartphones_sales, color='#D32F2F', edgecolor='white', width=0.5, label='Smartphones')
bars_tablets = plt.bar(months, tablets_sales, bottom=smartphones_sales, color='#1976D2', edgecolor='white', width=0.5, label='Tablets')
bars_laptops = plt.bar(months, laptops_sales, bottom=[i+j for i,j in zip(smartphones_sales, tablets_sales)], color='#388E3C', edgecolor='white', width=0.5, label='Laptops')

ax.set_ylabel('Sales')
ax.set_title('Monthly Sales Data for Electronics in 2024', pad=20)
ax.set_xticks(range(len(months)), labels=months, rotation=45)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1), title='Products')

for bars in [bars_smartphones, bars_tablets, bars_laptops]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_y() + yval/2, f'{yval}', ha='center', va='center', color='white', fontweight='bold')

plt.margins(x=0.1)

plt.show()