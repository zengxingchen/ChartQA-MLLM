
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Entertainment', 'Insurance', 'Clothing', 'Savings', 'Miscellaneous']
amounts = [1200, 300, 600, 250, 150, 200, 100, 400, 200]

# Color Scheme in HEX
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#A0A0FF', '#FFD700', '#FFB6C1', '#C0C0C0']

# Creating a figure to accomodate a larger treemap
fig, ax = plt.subplots(1, figsize=(12, 6))

# Creating the treemap
squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Monthly Expenses Distribution')

# Removing the axes for better aesthetic
plt.axis('off')

# Display the plot
plt.show()