
import matplotlib.pyplot as plt

# Data
fashion_categories = ["Clothing", "Footwear", "Jewelry", "Cosmetics", "Accessories", "Personal Care", "Luxury Goods", "Watches", "Bags"]
expenditure = [120, 80, 40, 70, 30, 50, 60, 20, 30]

# Colors
colors = [
    "#4E79A7",  # Clothing
    "#F28E2B",  # Footwear
    "#E15759",  # Jewelry
    "#76B7B2",  # Cosmetics
    "#59A14F",  # Accessories
    "#EDC949",  # Personal Care
    "#AF7AA1",  # Luxury Goods
    "#FF9DA7",  # Watches
    "#9C755F",  # Bags
]

# Create pie chart
plt.figure(figsize=(10, 8))  # width and height in inches
plt.pie(expenditure, labels=fashion_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Expenditure on Fashion Categories in 2023', pad=20)

# Show plot
plt.show()