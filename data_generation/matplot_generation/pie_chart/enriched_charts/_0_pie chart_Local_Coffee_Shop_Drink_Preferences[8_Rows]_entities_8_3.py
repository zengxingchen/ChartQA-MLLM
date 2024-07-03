
import matplotlib.pyplot as plt

# Data
brands = [
    'Toyota', 'Ford', 'Honda', 'Chevrolet', 'BMW', 'Tesla', 
    'Nissan', 'Volkswagen', 'Subaru', 'Mazda', 'Mercedes-Benz', 
    'Audi', 'KIA', 'Hyundai'
]
inventory_count = [50, 75, 40, 60, 30, 20, 45, 25, 35, 15, 13, 12, 28, 33]
colors = [
    '#FFD700', '#FF8C00', '#1E90FF', '#32CD32', '#8A2BE2', 
    '#A52A2A', '#FF4500', '#2E8B57', '#D2691E', '#E6E6FA', 
    '#800080', '#FFFF54', '#40E0D0', '#C71585'
]

# Create a pie chart
plt.figure(figsize=(10, 8))  # Adjusting the size of the pie chart
plt.pie(inventory_count, labels=brands, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Car Inventory Distribution by Brand')

plt.show()