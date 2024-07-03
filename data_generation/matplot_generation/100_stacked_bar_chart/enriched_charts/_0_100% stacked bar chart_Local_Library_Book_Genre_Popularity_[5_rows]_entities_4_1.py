
import matplotlib.pyplot as plt

# Preparing data
categories = ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6', 'Product 7', 'Product 8']
A = [34, 27, 22, 19, 15, 10, 5, 2]
B = [33, 36, 39, 42, 45, 30, 25, 20]
C = [33, 37, 39, 39, 40, 60, 70, 78]

# Summing the data points to normalize
totals = [i+j+k for i, j, k in zip(A, B, C)]
A_percentage = [i / j * 100 for i, j in zip(A, totals)]
B_percentage = [i / j * 100 for i, j in zip(B, totals)]
C_percentage = [i / j * 100 for i, j in zip(C, totals)]

fig, ax = plt.subplots(figsize=(10, 8))  # Changed width & height of the chart

# Stacking the bars horizontally
ax.barh(categories, A_percentage, color='#ff9999', edgecolor='white', height=0.8)  # Changed color & bandwidth
ax.barh(categories, B_percentage, left=A_percentage, color='#85e085', edgecolor='white', height=0.8)  # Changed color
ax.barh(categories, C_percentage, left=[i+j for i,j in zip(A_percentage, B_percentage)], color='#66b3ff', edgecolor='white', height=0.8)  # Changed color

# Adding labels
ax.set_xlabel('Percentage')
ax.set_title('Market Share by Product Category')

# Customizing the legend
plt.legend(['Category A', 'Category B', 'Category C'], loc='upper right', bbox_to_anchor=(1.2, 1))

plt.show()