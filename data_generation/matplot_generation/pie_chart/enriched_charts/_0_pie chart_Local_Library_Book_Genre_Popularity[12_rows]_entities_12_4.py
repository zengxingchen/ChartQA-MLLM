
import matplotlib.pyplot as plt

# Data to plot
categories = [
    'Electronics', 'Home Appliances', 'Books', 'Clothing', 'Grocery', 
    'Toys', 'Sports', 'Beauty', 'Gardening', 'Stationery'
]
sales = [35000, 23000, 15000, 40000, 30000, 12000, 18000, 11000, 8000, 7000]

# Define colors for each category
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFFF99', 
    '#FF6666', '#C2F0C2', '#FFB266', '#FFB6C1', '#D1E8E2'
]

# Creating the pie chart
plt.figure(figsize=(10,8))
plt.pie(sales, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Store Sales Distribution by Product Category')

plt.show()