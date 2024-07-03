
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
cities = ['City A', 'City B', 'City C', 'City D', 'City E', 'City F', 'City G', 'City H', 'City I', 'City J']
books = [22, 18, 16, 20, 24, 14, 18, 16, 22, 20]
magazines = [15, 25, 20, 18, 22, 17, 19, 24, 20, 18]
newspapers = [9, 11, 14, 12, 10, 16, 18, 14, 12, 15]
journals = [6, 9, 8, 7, 12, 10, 8, 12, 9, 11]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(10, 12))  # Set width and height of the chart
bars1 = ax.barh(cities, books, label='Books', color='#1E90FF', edgecolor='white', height=0.6)
bars2 = ax.barh(cities, magazines, label='Magazines', color='#FF6347', edgecolor='white', height=0.6, left=books)
bars3 = ax.barh(cities, newspapers, label='Newspapers', color='#32CD32', edgecolor='white', height=0.6, left=[i+j for i, j in zip(books, magazines)])
bars4 = ax.barh(cities, journals, label='Journals', color='#FFD700', edgecolor='white', height=0.6, left=[i+j+k for i, j, k in zip(books, magazines, newspapers)])

# Labeling and customization
ax.set_xlabel('Number of Publications')
ax.set_ylabel('Cities')
ax.set_title('Publications Distribution Across Different Cities')
ax.legend(loc='lower right')

# Adding numerical labels
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        width = bar.get_width()
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='center')

# Display the chart
plt.show()