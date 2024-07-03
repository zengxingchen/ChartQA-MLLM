import matplotlib.pyplot as plt
import numpy as np

categories = ['Literature', 'Writing', 'Poetry', 'Fiction', 'Non-fiction', 
              'Biography', 'Essay', 'Drama', 'Philosophy', 'Criticism']
product_a = [20, 25, 15, 30, 35, 40, 25, 20, 15, 30]
product_b = [30, 35, 25, 45, 20, 30, 40, 35, 40, 25]
product_c = [50, 40, 60, 25, 45, 30, 35, 45, 45, 45]

# Convert data to numpy array for easier manipulation
data = np.array([product_a, product_b, product_c])
data_cum = data.cumsum(axis=0)

# Colors for the bars
colors = ['#FF5733', '#33FF57', '#3357FF']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
for i, col in enumerate(colors):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.6, color=col, label=f'Product {chr(65+i)}')

# Add a legend
ax.legend(loc='upper right')

# Add labels and title
ax.set_xlabel('Percentage')
ax.set_title('Distribution of Products in Literature & Writing Categories', pad=20)

# Show the plot
plt.tight_layout()
plt.show()