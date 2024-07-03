
import matplotlib.pyplot as plt
import numpy as np

# Dataset
groups = ['Kids', 'Teens', 'Adults']
apples = [30, 25, 20]
bananas = [40, 30, 20]
oranges = [20, 25, 40]
grapes = [10, 20, 20]

# Calculating the cumulative sums
cum_apples = np.array(apples)
cum_bananas = cum_apples + np.array(bananas)
cum_oranges = cum_bananas + np.array(oranges)

# Converting to percentages
total = [sum(x) for x in zip(apples, bananas, oranges, grapes)]
apples_pct = [i / j * 100 for i, j in zip(apples, total)]
bananas_pct = [i / j * 100 for i, j in zip(bananas, total)]
oranges_pct = [i / j * 100 for i, j in zip(oranges, total)]
grapes_pct = [i / j * 100 for i, j in zip(grapes, total)]

# Colors
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']

# Setting the bar width
bar_width = 0.5

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(groups, apples_pct, color=colors[0], edgecolor='white', height=bar_width, label='Apples')
ax.barh(groups, bananas_pct, left=apples_pct, color=colors[1], edgecolor='white', height=bar_width, label='Bananas')
ax.barh(groups, oranges_pct, left=[i+j for i,j in zip(apples_pct, bananas_pct)], color=colors[2], edgecolor='white', height=bar_width, label='Oranges')
ax.barh(groups, grapes_pct, left=[i+j+k for i,j,k in zip(apples_pct, bananas_pct, oranges_pct)], color=colors[3], edgecolor='white', height=bar_width, label='Grapes')

# Adding labels and title
ax.set_xlabel('Percentage')
ax.set_title('Favorite Fruits by Age Group')
plt.xticks(np.arange(0, 101, 10))
plt.legend()

# Display the plot
plt.show()