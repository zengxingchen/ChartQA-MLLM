
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
pop = [12, 18, 14, 20, 16]
rock = [9, 8, 12, 15, 10]
jazz = [5, 3, 7, 4, 8]
classical = [7, 6, 10, 5, 11]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(12, 8))  # Set width and height of the chart
bars1 = ax.barh(stores, pop, label='Pop', color='#4caf50', edgecolor='black', height=0.6)
bars2 = ax.barh(stores, rock, label='Rock', color='#f44336', edgecolor='black', height=0.6, left=pop)
bars3 = ax.barh(stores, jazz, label='Jazz', color='#2196f3', edgecolor='black', height=0.6, left=[i+j for i, j in zip(pop, rock)])
bars4 = ax.barh(stores, classical, label='Classical', color='#ffeb3b', edgecolor='black', height=0.6, left=[i+j+k for i, j, k in zip(pop, rock, jazz)])

# Labeling and customization
ax.set_ylabel('Stores')
ax.set_xlabel('Sales (Thousands of Dollars)')
ax.set_title('Music Sales by Genre Across Different Stores', pad=20)
ax.legend(loc='lower right')

# Adding numerical labels to each bar
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        width = bar.get_width()
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                f'{int(width)}', ha='center', va='center', color='black', fontsize=10)

# Display the chart
plt.show()