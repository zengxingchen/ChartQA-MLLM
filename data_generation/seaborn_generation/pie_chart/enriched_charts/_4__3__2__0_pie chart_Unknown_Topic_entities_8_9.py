
import matplotlib.pyplot as plt

# Data points
categories = ['Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Water']
percentages = [20.0, 35.0, 15.0, 10.0, 5.0, 15.0]
colors = ['#4B0082', '#00FF7F', '#FF4500', '#4682B4', '#FFD700', '#8B0000']

# Create a pie chart
plt.figure(figsize=(16, 10))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)

# Chart title
plt.title('Macronutrient Distribution in a Balanced Diet', pad=20)

# Display the chart
plt.show()