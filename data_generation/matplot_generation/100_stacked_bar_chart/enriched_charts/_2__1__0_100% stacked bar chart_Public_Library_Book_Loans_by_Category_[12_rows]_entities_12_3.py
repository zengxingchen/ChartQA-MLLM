
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Europe', 'Asia', 'America', 'Africa', 'Australia', 'Antarctica']
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
values = np.array([
    [20, 25, 15, 10, 15, 15],
    [30, 20, 20, 10, 10, 10],
    [15, 20, 25, 15, 10, 15],
    [10, 15, 20, 15, 25, 15],
    [25, 20, 20, 20, 10, 5],
    [5, 10, 15, 20, 20, 30]
])

# Normalize the values to percentages
percentages = values / values.sum(axis=1)[:, None] * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.6

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#33FFF2']

# Plotting each age group
bottom = np.zeros(len(categories))
for i in range(len(age_groups)):
    ax.barh(categories, percentages[:, i], left=bottom, height=bar_width, color=colors[i], label=age_groups[i])
    bottom += percentages[:, i]

# Title and labels
ax.set_title('Popularity of Travel Destinations by Age Group', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Destinations')

# Legend
ax.legend(title='Age Groups', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()