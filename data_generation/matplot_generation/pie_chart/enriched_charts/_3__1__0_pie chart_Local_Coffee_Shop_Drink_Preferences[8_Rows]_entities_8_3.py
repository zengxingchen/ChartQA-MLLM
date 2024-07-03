
import matplotlib.pyplot as plt

# Data
categories = [
    'Programming Books', 'Design Books', 'Marketing Books', 'Management Books', 
    'History Books', 'Biographies', 'Science Books', 'Fiction Books', 
    'Poetry Books', 'Travel Guides', 'Cookbooks', 'Photography Books', 
    'Music Books', 'Art Books'
]
inventory_count = [55, 40, 35, 30, 25, 20, 15, 12, 10, 8, 5, 4, 3, 2]
colors = [
    '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', 
    '#DA70D6', '#7B68EE', '#FF4500', '#20B2AA', '#9ACD32', 
    '#BA55D3', '#778899', '#FFA07A', '#FF8C00'
]

# Create a pie chart
plt.figure(figsize=(14, 12))  # Adjusting the size of the pie chart
plt.pie(inventory_count, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Library Inventory Distribution by Category: Education & Learning', pad=40)

plt.show()