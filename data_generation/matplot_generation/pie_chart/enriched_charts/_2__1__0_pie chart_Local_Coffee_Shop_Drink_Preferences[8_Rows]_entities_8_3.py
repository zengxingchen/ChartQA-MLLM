
import matplotlib.pyplot as plt

# Data
destinations = [
    'Paris', 'New York', 'Tokyo', 'Rome', 'London', 
    'Barcelona', 'Bangkok', 'Dubai', 'Sydney', 
    'Singapore', 'Los Angeles', 'Amsterdam', 
    'Hong Kong', 'Berlin'
]
visitors = [300, 250, 200, 180, 160, 140, 120, 100, 90, 80, 70, 60, 50, 40]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', 
    '#33FFF5', '#FFBD33', '#8B33FF', '#33FF85', '#FF3380', 
    '#FFA533', '#3385FF', '#FF3333', '#85FF33'
]

# Create a pie chart
plt.figure(figsize=(14, 12))  # Adjusting the size of the pie chart
plt.pie(visitors, labels=destinations, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Top Travel Destinations by Annual Visitors', pad=20)

plt.show()