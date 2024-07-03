
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
product_a_sales = [150, 200, 140, 170, 160, 190]
product_b_sales = [120, 160, 130, 180, 130, 170]
product_c_sales = [100, 130, 150, 110, 140, 160]

# Color codes for each product
colors = ['#1b9e77', '#d95f02', '#7570b3']

# Plot stacked horizontal bar chart
plt.figure(figsize=(10, 8)) # Width and height of the chart in inches
bar_width = 0.8 # Width of the bars

plt.barh(months, product_a_sales, color=colors[0], edgecolor='white', height=bar_width, label='Product A')
plt.barh(months, product_b_sales, left=product_a_sales, color=colors[1], edgecolor='white', height=bar_width, label='Product B')
plt.barh(months, product_c_sales, left=[i+j for i,j in zip(product_a_sales, product_b_sales)], color=colors[2], edgecolor='white', height=bar_width, label='Product C')

# Add labels and title
plt.xlabel('Sales')
plt.ylabel('Month')
plt.title('Monthly Sales Data for Products A, B, and C')
plt.legend()

# Display the final result
plt.show()