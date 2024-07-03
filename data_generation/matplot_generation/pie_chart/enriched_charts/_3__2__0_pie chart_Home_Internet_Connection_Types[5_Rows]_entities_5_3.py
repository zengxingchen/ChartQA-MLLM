
import matplotlib.pyplot as plt

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Protein', 'Dairy', 'Sweets']
popularity = [28.3, 24.5, 17.2, 14.9, 10.8, 4.3]
colors = ['#FFA07A', '#20B2AA', '#9370DB', '#FFD700', '#8B0000', '#FF4500']

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(popularity, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popularity of Food Groups in 2023', y=1.05)

# Display the chart
plt.show()