
import matplotlib.pyplot as plt

# Data
categories = [
    'Astronomy Books', 'Physics Books', 'Biology Books', 'Chemistry Books', 
    'Geology Books', 'Ecology Books', 'Meteorology Books', 'Oceanography Books', 
    'Paleontology Books', 'Astrobiology Books', 'Quantum Mechanics Books', 
    'Thermodynamics Books', 'Optics Books', 'Nuclear Physics Books'
]
inventory_count = [60, 50, 45, 40, 35, 30, 25, 20, 15, 12, 10, 8, 5, 3]
colors = [
    '#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', 
    '#66CCCC', '#CC99FF', '#FFB3E6', '#FF9966', '#66FF66', 
    '#FF6699', '#99CC99', '#FF99CC', '#6699FF'
]

# Create a pie chart
plt.figure(figsize=(12, 10))  # Adjusting the size of the pie chart
plt.pie(inventory_count, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Library Inventory Distribution by Category: Science & Nature', pad=40)

plt.show()