
import matplotlib.pyplot as plt

# Data
locations = [
    'Mountains', 'Beaches', 'Cities', 'Deserts', 'Forests', 
    'Islands', 'Lakes', 'Rivers', 'Caves', 'Villages', 
    'Road Trips', 'Cruises', 'National Parks', 'Camping Sites'
]
counts = [80, 60, 70, 40, 50, 55, 45, 65, 35, 30, 68, 52, 62, 48]
colors = [
    '#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0', 
    '#3F51B5', '#009688', '#E91E63', '#00BCD4', '#795548', 
    '#673AB7', '#607D8B', '#FF9800', '#8BC34A'
]

# Create a pie chart
plt.figure(figsize=(10, 8))  # Adjusting the size of the pie chart
plt.pie(counts, labels=locations, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Interest Distribution by Travel & Adventure Locations', pad=30)

plt.show()