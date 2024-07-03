
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J']
books = [14, 19, 13, 17, 23, 18, 21, 17, 20, 16]
electronics = [10, 13, 8, 12, 16, 12, 15, 10, 12, 9]
clothing = [6, 9, 5, 8, 11, 8, 9, 7, 8, 6]
furniture = [11, 15, 9, 13, 18, 14, 16, 12, 14, 11]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(10, 12))  # Set width and height of the chart
bars1 = ax.bar(stores, books, label='Books', color='#FF5733', edgecolor='white', width=0.5)
bars2 = ax.bar(stores, electronics, label='Electronics', color='#33FF57', edgecolor='white', width=0.5, bottom=books)
bars3 = ax.bar(stores, clothing, label='Clothing', color='#3357FF', edgecolor='white', width=0.5, bottom=[i+j for i, j in zip(books, electronics)])
bars4 = ax.bar(stores, furniture, label='Furniture', color='#FF33A1', edgecolor='white', width=0.5, bottom=[i+j+k for i, j, k in zip(books, electronics, clothing)])

# Labeling and customization
ax.set_xlabel('Stores')
ax.set_ylabel('Sales (Thousands of Dollars)')
ax.set_title('Sales Distribution Across Different Categories')
ax.legend(loc='upper left')

# Adding numerical labels
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2 - 0.1, yval + 1, yval, ha='center', va='bottom')
for bar, yval in zip(bars2, electronics):
    plt.text(bar.get_x() + bar.get_width()/2 - 0.1, bar.get_y() + bar.get_height() + yval/2, yval, ha='center', va='bottom')
for bar, yval in zip(bars3, clothing):
    plt.text(bar.get_x() + bar.get_width()/2 - 0.1, bar.get_y() + bar.get_height() + yval/2, yval, ha='center', va='bottom')
for bar, yval in zip(bars4, furniture):
    plt.text(bar.get_x() + bar.get_width()/2 - 0.1, bar.get_y() + bar.get_height() + yval/2, yval, ha='center', va='bottom')

# Display the chart
plt.show()