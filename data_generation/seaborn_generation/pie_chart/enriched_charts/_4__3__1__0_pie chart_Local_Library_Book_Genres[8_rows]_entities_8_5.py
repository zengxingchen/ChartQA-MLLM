
import matplotlib.pyplot as plt

# Data points
categories = [
    'Artificial Intelligence', 'Quantum Computing', 'Blockchain', 'Renewable Energy', '5G Networks', 
    'Virtual Reality', 'Internet of Things', 'Biotechnology', 'Augmented Reality', 'Autonomous Vehicles'
]

popularity = [
    23.0, 18.5, 14.2, 12.0, 9.0, 
    8.5, 7.0, 4.8, 2.7, 0.8
]

# Colors for each section
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFB833',
    '#8D33FF', '#33FFF7', '#FF3333', '#57FF33', '#5733FF'
]

# Resize the chart
plt.figure(figsize=(12, 10))

# Create the pie chart
plt.pie(popularity, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Future Technologies & Society Topics in 2023', fontsize=18, pad=30)

# Display the chart
plt.show()