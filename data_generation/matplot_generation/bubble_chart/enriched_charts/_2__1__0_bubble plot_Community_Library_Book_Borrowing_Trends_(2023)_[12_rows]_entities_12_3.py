
import matplotlib.pyplot as plt

# Data
brand = ['Nike', 'Adidas', 'Puma', 'Under Armour', 'Reebok', 'Asics', 'New Balance', 'Fila', 'Sketchers', 'Columbia', 'Others']
market_share = [25.0, 20.0, 15.0, 10.0, 8.0, 7.0, 6.0, 4.0, 3.0, 2.0, 30.0]
average_selling_price = [100.0, 85.0, 70.0, 60.0, 55.0, 50.0, 45.0, 40.0, 35.0, 30.0, 25.0]
sales_volume = [450, 400, 300, 200, 180, 150, 120, 100, 90, 80, 600]

# Bubble sizes, normalizing sales_volume to suitable sizes for bubbles
sizes = [vol/1.5 for vol in sales_volume]

# Color codes
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', 
          '#00FFFF', '#800000', '#008000', '#000080', '#808000', '#808080']

# Create plot
plt.figure(figsize=(18, 12))  # Modify width and height
plt.scatter(average_selling_price, market_share, s=sizes, c=colors, alpha=0.6)
plt.title('Market Share of Different Sportswear Brands', fontsize=18, pad=30)
plt.xlabel('Average Selling Price (USD)', fontsize=15)
plt.ylabel('Market Share (%)', fontsize=15)

# Annotate company names
for i, txt in enumerate(brand):
    plt.annotate(txt, (average_selling_price[i], market_share[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()