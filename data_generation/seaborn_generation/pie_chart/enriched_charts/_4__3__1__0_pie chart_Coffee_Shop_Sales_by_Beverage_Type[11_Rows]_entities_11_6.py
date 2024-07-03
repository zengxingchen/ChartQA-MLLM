
import matplotlib.pyplot as plt

# Data
categories = ['Beaches', 'Mountains', 'Cities', 'Cruises', 'Deserts', 'Forests']
percentages = [30, 25, 20, 15, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Pie chart
plt.figure(figsize=(10, 7))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

# Title
plt.title('Favorite Travel Destinations', pad=30)

# Display the chart
plt.show()