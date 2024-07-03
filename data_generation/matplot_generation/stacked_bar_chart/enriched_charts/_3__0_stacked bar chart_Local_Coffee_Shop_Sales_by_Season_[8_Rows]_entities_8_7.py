
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
fruits = [50, 60, 70, 80, 90, 100, 110]
vegetables = [70, 80, 90, 100, 110, 120, 130]
whole_grains = [30, 40, 50, 60, 70, 80, 90]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.7

bars1 = ax.bar(years, fruits, width=bar_width, color='#FF6347', edgecolor='white', label='Fruits')
bars2 = ax.bar(years, vegetables, width=bar_width, bottom=fruits, color='#3CB371', edgecolor='white', label='Vegetables')
bars3 = ax.bar(years, whole_grains, width=bar_width, bottom=[i+j for i,j in zip(fruits, vegetables)], color='#1E90FF', edgecolor='white', label='Whole Grains')

# Labels and Title
ax.set_ylabel('Sales (in millions)')
ax.set_title('Sales of Healthy Foods from 2015 to 2021', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adding numerical labels to each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 0), 
                    textcoords='offset points',
                    ha='center', va='center', color='white', fontsize=9, fontweight='bold')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()