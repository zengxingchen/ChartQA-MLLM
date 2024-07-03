
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
electronics = [10, 15, 8, 12, 20]
books = [5, 3, 2, 4, 1]
clothing = [8, 10, 5, 7, 12]
home_goods = [3, 4, 6, 2, 9]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(10, 6))  # Set width and height of the chart
bars1 = ax.bar(stores, electronics, label='Electronics', color='#1f77b4', edgecolor='white', width=0.6)
bars2 = ax.bar(stores, books, label='Books', color='#ff7f0e', edgecolor='white', width=0.6, bottom=electronics)
bars3 = ax.bar(stores, clothing, label='Clothing', color='#2ca02c', edgecolor='white', width=0.6, bottom=[i+j for i, j in zip(electronics, books)])
bars4 = ax.bar(stores, home_goods, label='Home Goods', color='#d62728', edgecolor='white', width=0.6, bottom=[i+j+k for i, j, k in zip(electronics, books, clothing)])

# Labeling and customization
ax.set_xlabel('Stores')
ax.set_ylabel('Sales (Thousands of Dollars)')
ax.set_title('Sales by Product Category Across Different Stores')
ax.legend()

# Display the chart
plt.show()