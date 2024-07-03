
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Investments', 'Savings', 'Expenses', 'Debt']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

data = np.array([
    [40, 30, 20, 10],  # Investments
    [20, 25, 30, 25],  # Savings
    [30, 35, 35, 35],  # Expenses
    [10, 10, 15, 30],  # Debt
])

# Convert data to percentages
data_percentage = data / data.sum(axis=0) * 100

# Colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
width = 0.75  # Bar width

for i in range(len(categories)):
    bottom = np.sum(data_percentage[:i], axis=0)
    ax.barh(quarters, data_percentage[i], left=bottom, height=width, color=colors[i], label=categories[i])

# Customizations
ax.set_xlabel('Percentage')
ax.set_title('Quarterly Financial Distribution', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.show()