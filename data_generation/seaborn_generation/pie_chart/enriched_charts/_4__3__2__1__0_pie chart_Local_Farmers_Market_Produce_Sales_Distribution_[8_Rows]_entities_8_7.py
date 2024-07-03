
import matplotlib.pyplot as plt

# Data
food_items = ["Fruits", "Vegetables", "Grains", "Proteins", "Dairy", "Sweets", "Beverages", "Snacks", "Nuts"]
number_of_calories = [50, 40, 70, 60, 30, 20, 25, 35, 45]

# Colors
colors = [
    "#FF9999",  # Fruits
    "#66B2FF",  # Vegetables
    "#99FF99",  # Grains
    "#FFCC99",  # Proteins
    "#FFD700",  # Dairy
    "#FFB6C1",  # Sweets
    "#FF6347",  # Beverages
    "#8B4513",  # Snacks
    "#32CD32",  # Nuts
]

# Create pie chart
plt.figure(figsize=(12, 10))  # width and height in inches
plt.pie(number_of_calories, labels=food_items, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Daily Calorie Intake by Food Category', pad=40)

# Show plot
plt.show()