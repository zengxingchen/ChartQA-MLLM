
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided table
produce = [
    'Apples', 'Bananas', 'Carrots', 'Dates', 'Eggplants', 
    'Figs', 'Grapes', 'Honeydew', 'Iceberg Lettuce', 
    'Jalapenos', 'Kiwis', 'Leeks', 'Mushrooms'
]

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
prices = {
    'Apples': [1.50, 1.40, 1.60, 1.55],
    'Bananas': [0.60, 0.70, 0.65, 0.75],
    'Carrots': [0.90, 0.85, 0.80, 0.95],
    'Dates': [1.80, 1.75, 1.90, 2.00],
    'Eggplants': [1.30, 1.25, 1.40, 1.35],
    'Figs': [2.10, 2.00, 2.20, 2.15],
    'Grapes': [2.30, 2.20, 2.40, 2.25],
    'Honeydew': [0.95, 1.00, 0.90, 1.05],
    'Iceberg Lettuce': [1.00, 0.90, 1.10, 1.00],
    'Jalapenos': [1.20, 1.15, 1.25, 1.30],
    'Kiwis': [1.50, 1.45, 1.55, 1.60],
    'Leeks': [1.40, 1.35, 1.45, 1.50],
    'Mushrooms': [2.00, 1.90, 2.10, 2.05]
}

num_produce = len(produce)
num_weeks = len(weeks)
index = np.arange(num_produce)   # the label locations
bar_width = 0.2  # the width of the bars
offset = bar_width * (num_weeks - 1) / 2

fig, ax = plt.subplots(figsize=(14, 8))

# Generate bars for each week
for i, week in enumerate(weeks):
    prices_week = [prices[item][i] for item in produce]
    ax.bar(index - offset + i * bar_width, prices_week, bar_width, label=week)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Produce')
ax.set_ylabel('Price per lb ($)')
ax.set_title('Produce prices per lb over four weeks')
ax.set_xticks(index)
ax.set_xticklabels(produce, rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()