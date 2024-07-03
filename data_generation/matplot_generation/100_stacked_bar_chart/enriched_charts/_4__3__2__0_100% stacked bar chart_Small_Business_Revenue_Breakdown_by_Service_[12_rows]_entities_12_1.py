
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N', 'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T']
meditation = [15, 20, 25, 22, 18, 27, 25, 28, 26, 30, 23, 21, 19, 27, 29, 25, 26, 28, 23, 21]
yoga = [35, 30, 25, 33, 27, 23, 25, 22, 24, 20, 33, 29, 31, 23, 21, 25, 24, 22, 27, 29]
therapy = [50, 50, 50, 45, 55, 50, 50, 50, 50, 50, 44, 50, 50, 50, 50, 50, 50, 50, 50, 50]

# Colors
colors = ['#003f5c', '#58508d', '#bc5090']

# Plotting
fig, ax = plt.subplots(figsize=(12, 10))
width = 0.7  # width of the bars

meditation_perc = np.array(meditation) / np.array(meditation).sum() * 100
yoga_perc = np.array(yoga) / np.array(yoga).sum() * 100
therapy_perc = np.array(therapy) / np.array(therapy).sum() * 100

bars1 = ax.bar(categories, meditation_perc, color=colors[0], edgecolor='grey', width=width)
bars2 = ax.bar(categories, yoga_perc, bottom=meditation_perc, color=colors[1], edgecolor='grey', width=width)
bars3 = ax.bar(categories, therapy_perc, bottom=meditation_perc + yoga_perc, color=colors[2], edgecolor='grey', width=width)

# Adding the legend and title
ax.legend(['Meditation', 'Yoga', 'Therapy'], loc='upper right', bbox_to_anchor=(1.1, 1.05))
ax.set_title('Mental Health Activities Distribution among Different Groups', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Groups')

plt.show()