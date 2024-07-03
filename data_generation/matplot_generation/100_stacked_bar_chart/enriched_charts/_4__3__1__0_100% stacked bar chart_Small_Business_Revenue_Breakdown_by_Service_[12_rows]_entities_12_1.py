
import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
categories = ['USA', 'UK', 'Germany', 'France', 'Italy', 'Canada', 'Australia', 'Japan', 'India', 'China']
Dogs = [20, 15, 25, 20, 20, 18, 22, 25, 20, 15]
Cats = [25, 20, 15, 30, 10, 22, 18, 15, 30, 25]
Birds = [30, 25, 20, 15, 10, 28, 25, 20, 10, 20]
Fish = [10, 25, 20, 15, 30, 18, 15, 25, 20, 25]
Hamsters = [8, 10, 10, 12, 15, 9, 12, 5, 10, 5]
Rabbits = [7, 5, 10, 8, 15, 5, 8, 10, 10, 10]

# Stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))
bar_width = 0.8

bar1 = np.add(Dogs, Cats).tolist()
bar2 = np.add(bar1, Birds).tolist()
bar3 = np.add(bar2, Fish).tolist()
bar4 = np.add(bar3, Hamsters).tolist()

ax.bar(categories, Dogs, color='#1f77b4', edgecolor='white', width=bar_width)
ax.bar(categories, Cats, bottom=Dogs, color='#ff7f0e', edgecolor='white', width=bar_width)
ax.bar(categories, Birds, bottom=bar1, color='#2ca02c', edgecolor='white', width=bar_width)
ax.bar(categories, Fish, bottom=bar2, color='#d62728', edgecolor='white', width=bar_width)
ax.bar(categories, Hamsters, bottom=bar3, color='#9467bd', edgecolor='white', width=bar_width)
ax.bar(categories, Rabbits, bottom=bar4, color='#8c564b', edgecolor='white', width=bar_width)

# Adding labels and title
ax.set_ylabel('Percentage')
ax.set_title('Popularity of Pets by Country in 2024', pad=20)

# Adding legend
ax.legend(['Dogs', 'Cats', 'Birds', 'Fish', 'Hamsters', 'Rabbits'], loc='upper right')

plt.tight_layout()
plt.show()