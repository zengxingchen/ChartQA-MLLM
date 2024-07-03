
import matplotlib.pyplot as plt

# Data points
sports = [
    'Soccer', 'Basketball', 'Tennis', 'Cricket', 'Baseball', 
    'Rugby', 'Golf', 'Swimming', 'Cycling', 'Boxing'
]

popularity = [
    35.5, 20.3, 15.2, 10.4, 7.6, 
    4.8, 2.9, 1.8, 1.0, 0.5
]

# Colors for each section
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#ff6666', '#c2f0c2', '#6666ff'
]

# Resize the chart
plt.figure(figsize=(12, 8))

# Create the pie chart
plt.pie(popularity, labels=sports, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Different Sports in 2023', y=1.05)

# Display the chart
plt.show()