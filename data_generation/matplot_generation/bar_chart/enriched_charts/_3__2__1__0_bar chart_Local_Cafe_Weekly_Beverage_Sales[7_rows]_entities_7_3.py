
import matplotlib.pyplot as plt

categories = ['Vegetables', 'Fruits', 'Grains', 'Dairy', 'Protein', 'Fats', 'Beverages', 'Sweets', 'Spices', 'Condiments', 'Supplements', 'Snacks', 'Frozen Foods', 'Canned Foods', 'Bakery']
number_of_products = [50, 45, 40, 35, 30, 25, 20, 15, 10, 8, 6, 12, 18, 22, 28]

colors = ['#FF4500', '#FFD700', '#8A2BE2', '#32CD32', '#FF6347', '#9400D3', '#FF1493', '#4682B4', '#20B2AA', '#DC143C', '#7B68EE', '#00CED1', '#32CD32', '#8A2BE2', '#FFD700']

plt.figure(figsize=(14, 10))
plt.bar(categories, number_of_products, color=colors, edgecolor='black', width=0.6)

plt.ylabel('Number of Products', fontsize=14)
plt.xlabel('Category', fontsize=14)
plt.title('Number of Food Products per Category in 2021', fontsize=18, pad=20)
plt.ylim(0, 55)

plt.tight_layout()
plt.show()