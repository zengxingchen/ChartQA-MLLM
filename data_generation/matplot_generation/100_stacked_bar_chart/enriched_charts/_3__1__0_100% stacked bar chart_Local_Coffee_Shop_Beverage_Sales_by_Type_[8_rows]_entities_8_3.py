
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Primary', 'Primary', 'Primary', 'Secondary', 'Secondary', 'Secondary', 'Tertiary', 'Tertiary', 'Tertiary']
years = ['2015', '2016', '2017', '2015', '2016', '2017', '2015', '2016', '2017']
group_A = [25, 20, 30, 20, 25, 20, 15, 20, 25]
group_B = [25, 30, 20, 30, 25, 30, 35, 25, 25]
group_C = [25, 25, 30, 25, 25, 30, 30, 35, 25]
group_D = [25, 25, 20, 25, 25, 20, 20, 20, 25]

# Create plot
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.5

# Stacked bar chart
ind = np.arange(len(categories))
p1 = plt.barh(ind, group_A, bar_width, color='#1f77b4')
p2 = plt.barh(ind, group_B, bar_width, left=group_A, color='#ff7f0e')
p3 = plt.barh(ind, group_C, bar_width, left=np.add(group_A, group_B), color='#2ca02c')
p4 = plt.barh(ind, group_D, bar_width, left=np.add(np.add(group_A, group_B), group_C), color='#d62728')

# Labels, title and axis formatting
plt.xlabel('Percentage')
plt.ylabel('Education Level')
plt.title('Distribution of Education Levels Over Years')
plt.yticks(ind, ['Primary 2015', 'Primary 2016', 'Primary 2017', 'Secondary 2015', 'Secondary 2016', 'Secondary 2017', 'Tertiary 2015', 'Tertiary 2016', 'Tertiary 2017'])
plt.xticks(np.arange(0, 101, 10))

# Legend
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Group A', 'Group B', 'Group C', 'Group D'), loc='upper right')

# Adjust layout to fit the title and legend
plt.tight_layout()

# Display the chart
plt.show()