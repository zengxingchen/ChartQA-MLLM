
import matplotlib.pyplot as plt

# Data
brand = ['Coca-Cola', 'Pepsi', 'Nestle', 'Red Bull', 'Gatorade', 'Tropicana', 'Monster', 'Aquafina', 'Lipton', 'Fanta', 'Others']
market_share = [22.0, 18.0, 10.0, 8.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 21.0]
average_selling_price = [1.5, 1.3, 2.0, 3.0, 2.5, 1.8, 2.2, 1.0, 2.0, 1.7, 1.2]
sales_volume = [350, 300, 200, 120, 100, 90, 80, 60, 40, 20, 250]

# Bubble sizes, normalizing sales_volume to suitable sizes for bubbles
sizes = [vol/1.5 for vol in sales_volume]

# Color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFA6', 
          '#A633FF', '#FF8C33', '#33FF8C', '#8C33FF', '#33A6FF', '#FFD133']

# Create plot
plt.figure(figsize=(16, 10))  # Modify width and height
plt.scatter(average_selling_price, market_share, s=sizes, c=colors, alpha=0.5)
plt.title('Market Share of Different Beverage Brands', fontsize=16, pad=20)
plt.xlabel('Average Selling Price (USD)', fontsize=14)
plt.ylabel('Market Share (%)', fontsize=14)

# Annotate company names
for i, txt in enumerate(brand):
    plt.annotate(txt, (average_selling_price[i], market_share[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()