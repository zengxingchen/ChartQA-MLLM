
import matplotlib.pyplot as plt

# Data points based on the table provided
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
product_a_sales = [120, 135, 128, 140, 150, 155, 160, 165, 170, 175, 180, 185]
product_b_sales = [150, 160, 172, 165, 175, 180, 185, 190, 195, 200, 205, 210]
product_c_sales = [100, 110, 105, 115, 120, 130, 135, 140, 145, 150, 155, 160]

fig, ax = plt.subplots(figsize=(14, 8))

# Stacked bar chart with custom colors and horizontal orientation
bars_a = plt.barh(months, product_a_sales, color='#1F77B4', edgecolor='white', height=0.8, label='Product A')
bars_b = plt.barh(months, product_b_sales, left=product_a_sales, color='#FF7F0E', edgecolor='white', height=0.8, label='Product B')
bars_c = plt.barh(months, product_c_sales, left=[i+j for i,j in zip(product_a_sales, product_b_sales)], color='#2CA02C', edgecolor='white', height=0.8, label='Product C')

# Customizing the axes and title
ax.set_xlabel('Sales')
ax.set_title('Monthly Sales Data for the Three Products')
ax.set_yticks(range(len(months)), labels=months)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Products')

# Padding between the end of the bars and the edge of the figure
plt.margins(y=0.1)

# Display the plot
plt.show()