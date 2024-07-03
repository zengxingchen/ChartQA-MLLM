
import matplotlib.pyplot as plt

# Data
types = [
    'E-books', 'Printed Books', 'Audiobooks', 'Magazines', 
    'Comics', 'Newspapers', 'Journals', 'Manuscripts', 
    'Brochures', 'Catalogs', 'Reports', 'Pamphlets', 
    'Newsletters', 'Guides'
]
inventory_count = [60, 45, 30, 25, 20, 15, 10, 5, 8, 12, 18, 22, 14, 11]
colors = [
    '#FFA07A', '#20B2AA', '#778899', '#4682B4', '#9ACD32', 
    '#FF6347', '#FF4500', '#BA55D3', '#DA70D6', '#7B68EE', 
    '#32CD32', '#8A2BE2', '#FF8C00', '#FFD700'
]

# Create a pie chart
plt.figure(figsize=(12, 10))  # Adjusting the size of the pie chart
plt.pie(inventory_count, labels=types, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Library Inventory Distribution by Type', pad=20)

plt.show()