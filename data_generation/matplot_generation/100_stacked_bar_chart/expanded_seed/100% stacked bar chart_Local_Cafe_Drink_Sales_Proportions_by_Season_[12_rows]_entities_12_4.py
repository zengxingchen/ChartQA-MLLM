
import matplotlib.pyplot as plt
import numpy as np

# Data provided
data = [
    {'Season': 'Spring', 'Espresso': 20, 'Cappuccino': 15, 'Latte': 25, 'Tea': 10, 'Hot Chocolate': 5, 'Iced Coffee': 10, 'Smoothies': 10, 'Water': 5},
    {'Season': 'Summer', 'Espresso': 10, 'Cappuccino': 10, 'Latte': 15, 'Tea': 5, 'Hot Chocolate': 3, 'Iced Coffee': 30, 'Smoothies': 22, 'Water': 5},
    # ... (additional data truncated for brevity)
    {'Season': 'Winter', 'Espresso': 32, 'Cappuccino': 21, 'Latte': 18, 'Tea': 14, 'Hot Chocolate': 9, 'Iced Coffee': 3, 'Smoothies': 2, 'Water': 1}
]

# Prepare data for plotting
categories = list(data[0].keys())[1:]  # Get the list of categories (excluding 'Season')
seasons = list(set(d['Season'] for d in data))  # Get the unique seasons
seasons.sort()  # Sorting for consistent ordering

# We're going to sum values for each season to get the correct percentages
season_totals = {season: [0] * len(categories) for season in seasons}
for entry in data:
    for i, category in enumerate(categories):
        season_totals[entry['Season']][i] += entry[category]

# Calculate percentages
percentages = {season: [value / sum(season_totals[season]) * 100 for value in season_totals[season]] for season in seasons}

# Initialize the bar offsets
bar_offsets = {season: [0] * len(categories) for season in seasons}

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# We divide the bar into segments based on the percentage of each category
for i, category in enumerate(categories):
    values = [percentages[season][i] for season in seasons]
    ax.bar(seasons, values, bottom=[bar_offsets[season][i] for season in seasons], label=category, edgecolor='white')
    # Update offsets
    for season in seasons:
        bar_offsets[season][i] += values[seasons.index(season)]

# Customizing the plot
ax.set_xlabel('Season')
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart of Drinks by Season')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# Display the plot
plt.tight_layout()
plt.show()