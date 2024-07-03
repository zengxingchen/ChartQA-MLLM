
import matplotlib.pyplot as plt
import numpy as np

# Data from the chart table
data = [
    {'Quarter': 'Q1 2021', ' Product Sales': ' 30%', ' Consulting': ' 20%', ' Installation': ' 25%', ' Maintenance': ' 10%', ' Training': ' 10%', ' Custom Work': ' 5%'},
    # ... (include all the other data points here)
    {'Quarter': 'Q4 2023', ' Product Sales': ' 46%', ' Consulting': ' 12%', ' Installation': ' 17%', ' Maintenance': ' 9%', ' Training': ' 11%', ' Custom Work': ' 5%'}
]

# Extract categories and convert percentages to numbers
categories = [' Product Sales', ' Consulting', ' Installation', ' Maintenance', ' Training', ' Custom Work']
quarters = [entry['Quarter'] for entry in data]
dataset = {category: [float(entry[category].strip('%')) for entry in data] for category in categories}

# Stack data for 100% stacking
bottoms = np.zeros(len(data))

# Colors for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Start plotting
fig, ax = plt.subplots(figsize=(14, 7))

for i, (category, color) in enumerate(zip(categories, colors)):
    values = dataset[category]
    ax.bar(quarters, values, label=category.strip(), bottom=bottoms, color=color)
    # Update the bottoms for the next stack
    bottoms += np.array(values)

# Y-axis should show percentage
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels([f"{i}%" for i in range(0, 101, 10)])

# Rotating the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Title and labels
ax.set_title('Quarterly Revenue by Service Type (100% Stacked Bar Chart)')
ax.set_xlabel('Quarter')
ax.set_ylabel('Percentage')

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add value labels on top of each bar stack
for i, quarter in enumerate(quarters):
    y_offset = 0
    for j, category in enumerate(categories):
        value = dataset[category][i]
        if value:
            ax.text(i, y_offset + value/2, f"{value}%", ha='center', va='center', color='white', fontsize=7)
        y_offset += value

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()