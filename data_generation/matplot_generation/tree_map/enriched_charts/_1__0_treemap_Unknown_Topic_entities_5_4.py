
import matplotlib.pyplot as plt
import squarify

# Data
categories = ['Fruits', 'Vegetables', 'Dairy', 'Meat', 'Seafood', 'Grains', 'Beverages', 'Snacks', 'Miscellaneous']
revenue = [125000, 95000, 80000, 70000, 60000, 50000, 45000, 35000, 25000]

# Colors
colors = ['#FF8A65', '#4DB6AC', '#FFD54F', '#7986CB', '#F06292', '#A1887F', '#90A4AE', '#FFB74D', '#4DB6AC']

plt.figure(figsize=(12, 10))

# Treemap
squarify.plot(sizes=revenue, label=categories, color=colors, alpha=0.7)

plt.title('Revenue Distribution in Food & Nutrition', fontsize=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()