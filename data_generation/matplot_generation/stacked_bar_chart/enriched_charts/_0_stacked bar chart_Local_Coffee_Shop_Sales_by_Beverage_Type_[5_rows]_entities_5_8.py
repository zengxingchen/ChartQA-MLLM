
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
product_a_sales = [15000, 17000, 20000, 22000, 24000, 26000, 28000]
product_b_sales = [10000, 12000, 14000, 16000, 18000, 20000, 22000]
product_c_sales = [5000, 6000, 7000, 8000, 9000, 10000, 12000]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))  # Change the figure size

bar_width = 0.5  # Change the bar height for a horizontal bar chart

bar_a = ax.barh(years, product_a_sales, height=bar_width, color='#1f77b4', label='Product A')
bar_b = ax.barh(years, product_b_sales, height=bar_width, left=product_a_sales, color='#ff7f0e', label='Product B')
bar_c = ax.barh(years, product_c_sales, height=bar_width, left=[i+j for i,j in zip(product_a_sales, product_b_sales)], color='#2ca02c', label='Product C')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Total Sales')
ax.set_title('Annual Sales Report by Product')
ax.set_yticks([y + bar_width / 2 for y in range(len(years))])
ax.set_yticklabels(years)
ax.legend()

# Show the figure
plt.show()