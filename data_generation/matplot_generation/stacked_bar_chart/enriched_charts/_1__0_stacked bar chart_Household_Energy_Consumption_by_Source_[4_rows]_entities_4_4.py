
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
fruits = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]
vegetables = [20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000]
dairy = [18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000]
meat = [22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000]

fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_height = 0.6  # Change height of bars

# Plotting data (change direction of chart to vertical)
p1 = ax.bar(months, fruits, bar_height, color='#FF6F61', label='Fruits')
p2 = ax.bar(months, vegetables, bar_height, bottom=fruits, color='#6B5B95', label='Vegetables')
p3 = ax.bar(months, dairy, bar_height, bottom=[i+j for i,j in zip(fruits, vegetables)], color='#88B04B', label='Dairy')
p4 = ax.bar(months, meat, bar_height, bottom=[i+j+k for i,j,k in zip(fruits, vegetables, dairy)], color='#FFA500', label='Meat')

ax.set_ylabel('Sales')
ax.set_title('Monthly Food Sales Comparison')
ax.set_xticks([i for i in range(len(months))])
ax.set_xticklabels(months, rotation=45)
ax.legend()

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')
plt.show()