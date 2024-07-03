
import matplotlib.pyplot as plt

# Data to plot
categories = [
    'North America', 'Europe', 'Asia', 'South America', 'Africa', 
    'Australia', 'Antarctica'
]
sales = [45000, 32000, 28000, 15000, 9000, 11000, 500]

# Define colors for each category
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', 
    '#FFC733', '#33FFF7'
]

# Creating the pie chart
plt.figure(figsize=(12,10))
plt.pie(sales, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Continental Population Distribution', pad=20)

plt.show()