
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
fiction = [50, 60, 70, 80, 90, 100, 110]
non_fiction = [70, 75, 80, 85, 90, 95, 100]
poetry = [30, 35, 40, 45, 50, 55, 60]
drama = [20, 25, 30, 35, 40, 45, 50]

# Stacking data
non_fiction_bottom = [fiction[i] for i in range(len(fiction))]
poetry_bottom = [non_fiction_bottom[i] + non_fiction[i] for i in range(len(non_fiction))]
drama_bottom = [poetry_bottom[i] + poetry[i] for i in range(len(poetry))]

# Setting figure size
plt.figure(figsize=(14, 8))

# Plotting data
bar_height = 0.5
plt.barh(years, fiction, height=bar_height, color='#4c72b0', edgecolor='white', label='Fiction')
plt.barh(years, non_fiction, left=non_fiction_bottom, height=bar_height, color='#55a868', edgecolor='white', label='Non-Fiction')
plt.barh(years, poetry, left=poetry_bottom, height=bar_height, color='#c44e52', edgecolor='white', label='Poetry')
plt.barh(years, drama, left=drama_bottom, height=bar_height, color='#8172b2', edgecolor='white', label='Drama')

# Adding numerical labels
for i in range(len(years)):
    plt.text(fiction[i] / 2, i, str(fiction[i]), va='center', ha='center', color='white', fontsize=10)
    plt.text(non_fiction_bottom[i] + non_fiction[i] / 2, i, str(non_fiction[i]), va='center', ha='center', color='white', fontsize=10)
    plt.text(poetry_bottom[i] + poetry[i] / 2, i, str(poetry[i]), va='center', ha='center', color='white', fontsize=10)
    plt.text(drama_bottom[i] + drama[i] / 2, i, str(drama[i]), va='center', ha='center', color='white', fontsize=10)

# Adding titles and labels
plt.xlabel('Books Sold (in Thousands)')
plt.ylabel('Year')
plt.title('Annual Book Sales by Genre (2015-2021)', pad=20)
plt.legend(loc='upper right')

# Display the plot
plt.show()