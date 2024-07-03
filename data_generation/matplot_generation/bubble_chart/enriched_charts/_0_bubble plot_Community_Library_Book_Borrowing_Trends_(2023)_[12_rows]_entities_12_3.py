
import matplotlib.pyplot as plt

# Data
company = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Lenovo', 'LG', 'Nokia', 'Sony', 'Others']
market_share = [20.5, 15.5, 10.5, 8.5, 5.5, 4.5, 3.5, 2.5, 1.5, 1.0, 30.0]
average_selling_price = [250, 750, 300, 150, 200, 180, 150, 220, 100, 350, 125]
sales_volume = [300, 200, 150, 120, 90, 75, 65, 40, 25, 15, 220]

# Bubble sizes, normalizing sales_volume to suitable sizes for bubbles
sizes = [vol/1.5 for vol in sales_volume]

# Color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF']

# Create plot
plt.figure(figsize=(14, 8))  # Modify width and height
plt.scatter(average_selling_price, market_share, s=sizes, c=colors, alpha=0.5)
plt.title('Global Smartphone Market Share by Company (2021)')
plt.xlabel('Average Selling Price (USD)')
plt.ylabel('Market Share (%)')

# Annotate company names
for i, txt in enumerate(company):
    plt.annotate(txt, (average_selling_price[i], market_share[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()