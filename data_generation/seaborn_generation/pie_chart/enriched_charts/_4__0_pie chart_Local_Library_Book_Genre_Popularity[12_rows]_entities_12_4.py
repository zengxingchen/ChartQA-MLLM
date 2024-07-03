
import matplotlib.pyplot as plt

# Data to plot
categories = [
    'Basketball', 'Soccer', 'Tennis', 'Swimming', 'Cycling', 
    'Running', 'Gym Equipment', 'Yoga', 'Golf', 'Baseball'
]
sales = [22000, 34000, 15000, 20000, 18000, 27000, 25000, 16000, 19000, 13000]

# Define colors for each category
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#33FFF6', 
    '#FF33F6', '#F633FF', '#FF9633', '#33FF9C', '#FF3333'
]

# Creating the pie chart
plt.figure(figsize=(12,10))
plt.pie(sales, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Sports & Fitness Equipment Sales Distribution', fontsize=14, pad=20)

plt.show()