
import matplotlib.pyplot as plt
import numpy as np

# Data as nested lists
data = [
    [800, 600, 300, 200],
    [850, 500, 400, 250],
    [900, 700, 350, 150],
    [950, 550, 450, 300]
]

# Convert data for percentage stacking
percent_data = np.array(data) / np.sum(data, axis=1)[:, None]

# Colors for each category
colors = ['#FFD700', '#7CFC00', '#00BFFF', '#DC143C']

# Setup figure size
plt.figure(figsize=(10, 6))

# Months as categories on the y-axis
categories = ['January', 'February', 'March', 'April']

# Bar width
bar_width = 0.5

# Stacked bar chart logic
left = np.zeros(len(categories))  # start at zero

# Iterate through each expense category and plot
for idx, (colname, color) in enumerate(zip(['Housing', 'Food', 'Transportation', 'Entertainment'], colors)):
    plt.barh(categories, percent_data[:, idx], left=left, color=color, edgecolor='white', height=bar_width, label=colname)
    left += percent_data[:, idx]

# Add some text for labels, title and custom x-axis tick labels, etc.
plt.xlabel('Percentage of Expenses')
plt.title('Monthly Expenses by Category as a Percentage of Total')
plt.yticks(ticks=np.arange(len(categories)), labels=categories)

# Show grid lines for better readability
plt.grid(True, axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Add legend
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

# Set limits
plt.xlim(0, 1)

# To avoid the elements outside the plot area due to the bbox (legend)
plt.tight_layout(rect=[0,0,0.85,1])

# Show the plot
plt.show()