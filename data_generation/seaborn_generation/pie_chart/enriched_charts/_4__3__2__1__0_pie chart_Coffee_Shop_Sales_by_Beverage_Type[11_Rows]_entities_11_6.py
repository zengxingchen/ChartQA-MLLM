
import matplotlib.pyplot as plt

# Data
hobbies = ['Reading', 'Traveling', 'Cooking', 'Painting', 'Gardening', 'Photography', 'Writing', 'Music']
percentages = [22, 18, 15, 12, 10, 8, 6, 9]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76D7C4']

# Pie chart
plt.figure(figsize=(12, 8))
plt.pie(percentages, labels=hobbies, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

# Title
plt.title('Popular Hobbies Among Adults', pad=40)

# Display the chart
plt.show()