
import matplotlib.pyplot as plt

# Data
food_categories = ["Vegetables", "Fruits", "Grains", "Meat", "Dairy", "Seafood", "Sweets", "Beverages", "Nuts and Seeds"]
amount_consumed = [25, 18, 30, 15, 20, 10, 5, 12, 8]

# Colors
colors = [
    "#4CAF50",  # Vegetables
    "#FF9800",  # Fruits
    "#9C27B0",  # Grains
    "#F44336",  # Meat
    "#3F51B5",  # Dairy
    "#00BCD4",  # Seafood
    "#E91E63",  # Sweets
    "#795548",  # Beverages
    "#FFEB3B",  # Nuts and Seeds
]

# Create pie chart
plt.figure(figsize=(12, 10))  # width and height in inches
plt.pie(amount_consumed, labels=food_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Weekly Food Consumption by Category (in kg)', pad=20)

# Show plot
plt.show()