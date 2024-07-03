
import matplotlib.pyplot as plt

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Protein', 'Dairy', 'Sweets', 'Beverages', 'Others']
percentages = [20, 15, 25, 10, 10, 8, 7, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffcc00', '#c0c0c0']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Food Categories in Daily Diet (2022)", pad=20)

# Display the chart
plt.show()