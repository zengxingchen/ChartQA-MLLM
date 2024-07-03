
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
product_a_sales = [150, 165, 140, 170, 200, 160, 175, 190, 220, 210, 190, 225]
product_b_sales = [120, 100, 130, 115, 135, 140, 150, 170, 180, 195, 185, 200]
product_c_sales = [90, 110, 120, 125, 95, 130, 125, 160, 150, 170, 165, 175]

# Plot setup
fig, ax = plt.subplots(figsize=(14,8))

# Create bar chart
bar_width = 0.25
bar_locations_a = range(len(product_a_sales))
bar_locations_b = [x + bar_width for x in bar_locations_a]
bar_locations_c = [x + bar_width for x in bar_locations_b]

bars1 = ax.barh(bar_locations_a, product_a_sales, bar_width, label='Product A', color='#FF5733')
bars2 = ax.barh(bar_locations_b, product_b_sales, bar_width, label='Product B', color='#33FF57')
bars3 = ax.barh(bar_locations_c, product_c_sales, bar_width, label='Product C', color='#3357FF')

# Set the position of the x ticks
ax.set_yticks([r + bar_width for r in range(len(product_a_sales))])
ax.set_yticklabels(months)

# Adding labels and title
plt.xlabel('Sales in units')
plt.title('Monthly Sales of Products A, B, and C')
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()