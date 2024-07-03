
import matplotlib.pyplot as plt

# Data to plot
labels = 'Meal Preparation', 'Grocery Shopping', 'Cooking', 'Eating Out', 'Reading Recipes', 'Food Photography'
sizes = [30, 20, 25, 15, 5, 5]
colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FF69B4', '#8A2BE2']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Daily Activities Related to Food & Nutrition', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()