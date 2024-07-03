
import matplotlib.pyplot as plt

# Data setup
categories = ['Skincare', 'Makeup', 'Haircare', 'Fragrance', 'Fashion', 'Accessories', 'Shoes', 'Bags', 'Jewelry', 'Watches', 'Eyewear', 'Others']
percentages = [18, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 4]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666', '#c4e17f', '#d3b6c6', '#ffcccb', '#c0d6e4']

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))  # width and height of the chart
ax.pie(percentages, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Popular Beauty and Fashion Categories by Market Share', pad=20)

# Show plot
plt.show()