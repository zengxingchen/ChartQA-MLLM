
import matplotlib.pyplot as plt

# Hypothetical data representing revenue and market share by product category
categories = ['Electronics', 'Apparel', 'Home Goods', 'Beauty', 'Toys', 'Books', 'Groceries', 'Pet Supplies', 'Automotive', 'Sports Equipment']
revenue = [350, 200, 150, 100, 80, 60, 40, 20, 10, 5]
market_share = [30, 20, 15, 10, 8, 6, 4, 2, 1, 0.5]
number_of_companies = [150, 100, 75, 50, 30, 25, 20, 15, 10, 5]

# Custom color for each product category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Set the figure size
plt.figure(figsize=(14, 9))

# Scatter plot with bubble sizes
bubble_sizes = [n * 2 for n in number_of_companies]  # Scaling the number of companies for bubble size
plt.scatter(categories, revenue, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Product Category')
plt.ylabel('Revenue (in million USD)')
plt.title('Revenue and Market Share by Product Category in a Hypothetical Market', pad=20)

# Show plot
plt.show()