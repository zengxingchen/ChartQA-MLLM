
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J']
fruits = [12, 20, 16, 14, 10, 18, 22, 16, 14, 20]
vegetables = [18, 22, 12, 16, 20, 14, 16, 18, 12, 24]
dairy = [6, 14, 10, 8, 12, 10, 18, 14, 16, 20]
meat = [14, 10, 8, 12, 16, 20, 12, 14, 18, 16]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(12, 8))  # Set width and height of the chart
bars1 = ax.barh(stores, fruits, label='Fruits', color='#8B0000', edgecolor='white', height=0.5)
bars2 = ax.barh(stores, vegetables, label='Vegetables', color='#228B22', edgecolor='white', height=0.5, left=fruits)
bars3 = ax.barh(stores, dairy, label='Dairy', color='#4682B4', edgecolor='white', height=0.5, left=[i+j for i, j in zip(fruits, vegetables)])
bars4 = ax.barh(stores, meat, label='Meat', color='#FFD700', edgecolor='white', height=0.5, left=[i+j+k for i, j, k in zip(fruits, vegetables, dairy)])

# Labeling and customization
ax.set_xlabel('Sales (Thousands of Dollars)')
ax.set_ylabel('Stores')
ax.set_title('Sales by Food Category Across Different Stores')
ax.legend(loc='upper right')

# Adding numerical labels
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        width = bar.get_width()
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='center')

# Display the chart
plt.show()