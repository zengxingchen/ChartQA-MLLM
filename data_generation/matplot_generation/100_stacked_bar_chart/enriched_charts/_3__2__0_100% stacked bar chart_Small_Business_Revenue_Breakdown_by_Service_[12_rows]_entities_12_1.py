
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N', 'Group O']
running = [20, 25, 30, 22, 18, 27, 25, 28, 26, 30, 23, 21, 19, 27, 29]
swimming = [30, 35, 25, 33, 27, 23, 25, 22, 24, 30, 33, 29, 31, 23, 21]
cycling = [50, 40, 45, 45, 55, 50, 50, 50, 50, 40, 44, 50, 50, 50, 50]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
width = 0.5  # width of the bars

running_perc = np.array(running) / np.array(running).sum() * 100
swimming_perc = np.array(swimming) / np.array(swimming).sum() * 100
cycling_perc = np.array(cycling) / np.array(cycling).sum() * 100

bars1 = ax.barh(categories, running_perc, color=colors[0], edgecolor='grey', height=width)
bars2 = ax.barh(categories, swimming_perc, left=running_perc, color=colors[1], edgecolor='grey', height=width)
bars3 = ax.barh(categories, cycling_perc, left=running_perc + swimming_perc, color=colors[2], edgecolor='grey', height=width)

# Adding the legend and title
ax.legend(['Running', 'Swimming', 'Cycling'], loc='lower right', bbox_to_anchor=(1, 0.5))
ax.set_title('Sports Activity Distribution among Groups', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Groups')

plt.show()