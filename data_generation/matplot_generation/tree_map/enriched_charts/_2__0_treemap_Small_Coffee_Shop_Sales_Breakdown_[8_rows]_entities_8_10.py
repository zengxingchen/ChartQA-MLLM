
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
categories = [
    'Rent', 'Utilities', 'Groceries', 'Transportation', 'Entertainment',
    'Insurance', 'Clothing', 'Savings', 'Miscellaneous', 'Healthcare',
    'Education', 'Subscriptions', 'Dining Out', 'Charity', 'Fitness',
    'Travel', 'Gifts', 'Pets'
]
amounts = [
    1200, 300, 600, 250, 150, 200, 100, 400, 200, 450, 500, 100, 350, 150,
    300, 600, 200, 250
]

# Color Scheme in HEX
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#A0A0FF',
    '#FFD700', '#FFB6C1', '#C0C0C0', '#8A2BE2', '#5F9EA0', '#7FFF00',
    '#DC143C', '#7B68EE', '#FFA07A', '#00FA9A', '#D2691E', '#FF4500'
]

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(14, 7))

# Creating the treemap
squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Monthly Household Budget Breakdown')

# Removing the axes for better aesthetic
plt.axis('off')

# Display the plot
plt.show()