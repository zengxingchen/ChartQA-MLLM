
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Store 1', 'Store 2', 'Store 3', 'Store 4', 'Store 5', 'Store 6', 'Store 7', 'Store 8', 'Store 9', 'Store 10']
books = [150, 130, 140, 160, 170, 180, 190, 200, 210, 220]
stationery = [120, 110, 130, 140, 150, 160, 170, 180, 190, 200]
electronics = [100, 90, 110, 120, 130, 140, 150, 160, 170, 180]
clothing = [90, 80, 100, 110, 120, 130, 140, 150, 160, 170]

bar_width = 0.6
fig, ax = plt.subplots(figsize=(14, 10))

# Location of bars on x-axis
ind = np.arange(len(categories))

# Stacked bar chart (vertical)
plt.bar(ind, books, width=bar_width, color='#FF5733')
plt.bar(ind, stationery, width=bar_width, bottom=books, color='#33FF57')
plt.bar(ind, electronics, width=bar_width, bottom=np.add(books, stationery), color='#3357FF')
plt.bar(ind, clothing, width=bar_width, bottom=np.add(books, np.add(stationery, electronics)), color='#FF33A6')

# Labels and Titles
ax.set_ylabel('Revenue (in thousands)')
ax.set_title('Monthly Sales Distribution in Different Stores', pad=20)
ax.set_xticks(ind)
ax.set_xticklabels(categories)
ax.set_xlabel('Store')

# Numerical Labels
for i in range(len(categories)):
    plt.text(i, books[i] / 2, str(books[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(i, books[i] + stationery[i] / 2, str(stationery[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(i, books[i] + stationery[i] + electronics[i] / 2, str(electronics[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(i, books[i] + stationery[i] + electronics[i] + clothing[i] / 2, str(clothing[i]), va='center', ha='center', color='white', fontweight='bold')

# Legend
plt.legend(['Books', 'Stationery', 'Electronics', 'Clothing'], loc='upper left')

# Display the chart
plt.show()