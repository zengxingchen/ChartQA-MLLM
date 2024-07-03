
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
books = [25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000]
electronics = [38000, 36000, 37000, 39000, 35000, 34000, 33000, 32000, 31000, 30000, 29000, 28000]
home_appliances = [22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000]
clothing = [27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000]

fig, ax = plt.subplots(figsize=(10, 8)) # change width and height of the chart

bar_width = 0.4 # change width of bars

# Plotting data (change direction of chart to horizontal)
p1 = ax.barh(months, books, bar_width, color='#EE6352', label='Books')
p2 = ax.barh(months, electronics, bar_width, left=books, color='#08B2E3', label='Electronics')
p3 = ax.barh(months, home_appliances, bar_width, left=[i+j for i,j in zip(books, electronics)], color='#AAD5A5', label='Home Appliances')
p4 = ax.barh(months, clothing, bar_width, left=[i+j+k for i,j,k in zip(books, electronics, home_appliances)], color='#FF9B42', label='Clothing')

ax.set_xlabel('Sales')
ax.set_title('Monthly Sales Comparison')
ax.set_yticks([i + bar_width / 2 for i in range(len(months))])  # Modify tick position due to horizontal
ax.set_yticklabels(months)
ax.legend()

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')
plt.show()