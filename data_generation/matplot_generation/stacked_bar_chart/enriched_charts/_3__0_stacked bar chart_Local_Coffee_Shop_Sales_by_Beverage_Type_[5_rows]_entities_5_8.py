
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
digital_goods_sales = [20000, 22000, 25000, 28000, 30000, 32000, 35000]
subscription_services_sales = [18000, 19000, 21000, 23000, 25000, 27000, 29000]
physical_products_sales = [16000, 17000, 19000, 20000, 22000, 24000, 26000]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change the figure size

bar_width = 0.6  # Change the bar width for a vertical bar chart

bar_digital = ax.bar(years, digital_goods_sales, width=bar_width, color='#FF5733', label='Digital Goods')
bar_subscription = ax.bar(years, subscription_services_sales, width=bar_width, bottom=digital_goods_sales, color='#33FF57', label='Subscription Services')
bar_physical = ax.bar(years, physical_products_sales, width=bar_width, bottom=[i+j for i,j in zip(digital_goods_sales, subscription_services_sales)], color='#3357FF', label='Physical Products')

# Add some text for labels, title and custom y-axis tick labels, etc.
ax.set_ylabel('Total Revenue')
ax.set_title('Annual Revenue Breakdown by Category', pad=20)
ax.legend(loc='upper left')

# Adding numerical labels
for bar in [bar_digital, bar_subscription, bar_physical]:
    for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, rect.get_y() + height / 2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Show the figure
plt.show()