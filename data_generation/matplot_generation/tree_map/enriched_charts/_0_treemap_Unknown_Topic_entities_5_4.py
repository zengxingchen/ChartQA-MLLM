
import matplotlib.pyplot as plt
import squarify

# Data
categories = ['Electronics', 'Home & Kitchen', 'Sports & Outdoors', 'Clothing & Accessories',
              'Beauty & Health', 'Books', 'Toys & Games', 'Grocery & Gourmet Food',
              'Pet Supplies', 'Handmade']
revenue = [120000, 85000, 60000, 55000, 45000, 30000, 20000, 15000, 10000, 5000]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33FF', '#FFFF33', '#33FFFF', '#FF8333', '#33FF85', '#8357FF']

plt.figure(figsize=(14, 8))

# Treemap
squarify.plot(sizes=revenue, label=categories, color=colors, alpha=0.7)

plt.title('E-commerce Store Revenue Distribution by Category', fontsize=18)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()