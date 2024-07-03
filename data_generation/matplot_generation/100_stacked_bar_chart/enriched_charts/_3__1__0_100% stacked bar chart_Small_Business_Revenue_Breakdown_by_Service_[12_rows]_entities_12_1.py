
import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
categories = ['Red Dresses', 'Blue Dresses', 'Green Dresses', 'Yellow Dresses', 'Purple Dresses']
USA = [30, 25, 20, 15, 10]
UK = [20, 30, 25, 10, 15]
Germany = [25, 20, 30, 15, 10]
France = [15, 15, 15, 30, 25]
Italy = [10, 10, 10, 30, 40]

# Stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

bar1 = np.add(USA, UK).tolist()
bar2 = np.add(bar1, Germany).tolist()
bar3 = np.add(bar2, France).tolist()

ax.barh(categories, USA, color='#FF6347', edgecolor='white', height=bar_width)
ax.barh(categories, UK, left=USA, color='#4682B4', edgecolor='white', height=bar_width)
ax.barh(categories, Germany, left=bar1, color='#3CB371', edgecolor='white', height=bar_width)
ax.barh(categories, France, left=bar2, color='#FFD700', edgecolor='white', height=bar_width)
ax.barh(categories, Italy, left=bar3, color='#800080', edgecolor='white', height=bar_width)

# Adding labels and title
ax.set_xlabel('Percentage')
ax.set_title('Popularity of Dress Colors by Country in 2024')

# Adding legend
ax.legend(['USA', 'UK', 'Germany', 'France', 'Italy'], loc='lower right')

plt.tight_layout()
plt.show()