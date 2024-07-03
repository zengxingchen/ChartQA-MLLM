
import matplotlib.pyplot as plt

# Data
brand = ['Nestle', 'PepsiCo', 'Coca-Cola', 'Unilever', 'Mondelez', 'General Mills', "Kellogg's", 'Danone', 'Mars', 'Heinz', 'Others']
market_share = [18.0, 15.0, 14.0, 12.0, 10.0, 9.0, 8.0, 6.0, 5.0, 3.0, 20.0]
average_selling_price = [120.0, 110.0, 105.0, 95.0, 90.0, 85.0, 80.0, 75.0, 70.0, 60.0, 50.0]
sales_volume = [500, 450, 420, 380, 350, 330, 310, 280, 260, 220, 700]

# Bubble sizes, normalizing sales_volume to suitable sizes for bubbles
sizes = [vol/1.5 for vol in sales_volume]

# Color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55a2']

# Create plot
plt.figure(figsize=(16, 10))  # Modify width and height
plt.scatter(average_selling_price, market_share, s=sizes, c=colors, alpha=0.6)
plt.title('Market Share and Average Price of Popular Food Brands', fontsize=18, pad=30)
plt.xlabel('Average Selling Price (USD)', fontsize=15)
plt.ylabel('Market Share (%)', fontsize=15)

# Annotate company names
for i, txt in enumerate(brand):
    plt.annotate(txt, (average_selling_price[i], market_share[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()