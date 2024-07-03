
import matplotlib.pyplot as plt

# Data points
fruits = [
    'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 
    'Fig', 'Grape', 'Honeydew', 'Kiwi', 'Lemon'
]

popularity = [
    20.5, 15.0, 10.0, 5.5, 3.5, 
    12.0, 18.5, 8.0, 4.0, 3.0
]

# Colors for each section
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#ff8c69', '#6c5b7b', '#c06c84'
]

# Resize the chart
plt.figure(figsize=(12, 8))

# Create the pie chart
plt.pie(popularity, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Various Fruits in 2023')

# Display the chart
plt.show()