
import matplotlib.pyplot as plt

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [150, 160, 170, 180]
product_b = [160, 170, 180, 190]
product_c = [170, 180, 190, 200]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart (horizontal)
bar_height = 0.6
plt.barh(quarters, product_a, color='#4B0082', edgecolor='white', height=bar_height, label='Product A')
plt.barh(quarters, product_b, left=product_a, color='#FFD700', edgecolor='white', height=bar_height, label='Product B')
plt.barh(quarters, product_c, left=[i+j for i,j in zip(product_a, product_b)], color='#00FA9A', edgecolor='white', height=bar_height, label='Product C')

# Labels, title, and legend
plt.xlabel('Revenue ($)')
plt.title('Quarterly Revenue Distribution of Products A, B, and C', pad=20)
plt.legend(loc='lower right')

# Numerical labels for each bar
for i in range(len(quarters)):
    plt.text(product_a[i] / 2, i, str(product_a[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(product_a[i] + (product_b[i] / 2), i, str(product_b[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(product_a[i] + product_b[i] + (product_c[i] / 2), i, str(product_c[i]), ha='center', va='center', color='white', fontweight='bold')

# Show the plot
plt.show()