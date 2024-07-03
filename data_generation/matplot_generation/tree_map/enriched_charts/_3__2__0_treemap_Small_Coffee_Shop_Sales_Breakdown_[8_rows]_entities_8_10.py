
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
categories = [
    'Tuition', 'Books', 'Supplies', 'Transportation', 'Housing', 'Food', 'Utilities',
    'Internet', 'Clothing', 'Healthcare', 'Fitness', 'Entertainment', 'Savings',
    'Miscellaneous', 'Scholarships', 'Loans', 'Grants', 'Events'
]
amounts = [
    1500, 400, 200, 300, 1000, 600, 150, 100, 200, 250, 100, 300, 500, 150,
    600, 700, 400, 200
]

# Color Scheme in HEX
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#A0A0FF',
    '#FFD700', '#FFB6C1', '#C0C0C0', '#8A2BE2', '#5F9EA0', '#7FFF00',
    '#DC143C', '#7B68EE', '#FFA07A', '#00FA9A', '#D2691E', '#FF4500'
]

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(16, 8))

# Creating the treemap
squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Annual Education Expenses Breakdown', fontsize=18)

# Removing the axes for better aesthetic
plt.axis('off')

# Display the plot
plt.show()