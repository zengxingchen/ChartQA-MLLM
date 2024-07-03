
import matplotlib.pyplot as plt

# Data for stacked bar chart
topics = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J']
classics = [15, 22, 14, 19, 25, 20, 23, 18, 21, 16]
modern_literature = [12, 18, 11, 16, 20, 17, 19, 14, 16, 13]
poetry = [8, 10, 7, 9, 13, 11, 12, 9, 10, 7]
drama = [10, 15, 9, 13, 18, 14, 16, 11, 14, 10]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(10, 12))  # Set width and height of the chart
bars1 = ax.bar(topics, classics, label='Classics', color='#1f77b4', edgecolor='white', width=0.6)
bars2 = ax.bar(topics, modern_literature, label='Modern Literature', color='#ff7f0e', edgecolor='white', width=0.6, bottom=classics)
bars3 = ax.bar(topics, poetry, label='Poetry', color='#2ca02c', edgecolor='white', width=0.6, bottom=[i+j for i, j in zip(classics, modern_literature)])
bars4 = ax.bar(topics, drama, label='Drama', color='#d62728', edgecolor='white', width=0.6, bottom=[i+j+k for i, j, k in zip(classics, modern_literature, poetry)])

# Labeling and customization
ax.set_xlabel('Stores')
ax.set_ylabel('Books Sold (Thousands)')
ax.set_title('Literature Sales by Store', pad=20)
ax.legend(loc='upper left')

# Adding numerical labels
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Display the chart
plt.show()