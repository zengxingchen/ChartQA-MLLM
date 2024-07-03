
import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Home and Kitchen', 'Books', 'Beauty Products', 'Toys', 'Sports Equipment', 'Other']
sales_percentages = [20, 15, 25, 10, 10, 8, 7, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 10))
ax.pie(sales_percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Sales Distribution Across Product Categories in 2023", pad=20)

# Display the chart
plt.show()