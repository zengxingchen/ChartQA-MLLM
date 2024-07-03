
import matplotlib.pyplot as plt
import numpy as np

# Data
topics = ['Air Quality', 'Water Quality', 'Waste Management', 'Renewable Energy', 'Biodiversity', 'Climate Action', 'Urban Green Spaces', 'Sustainable Transport']
Q1 = np.array([12000, 15000, 11000, 17000, 14000, 13000, 10000, 16000])
Q2 = np.array([18000, 13000, 16000, 19000, 15000, 14000, 12000, 17000])
Q3 = np.array([14000, 16000, 15000, 20000, 17000, 18000, 13000, 18000])
Q4 = np.array([19000, 17000, 18000, 21000, 20000, 19000, 16000, 19000])

ind = np.arange(len(Q1))  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots(figsize=(16, 10))

p1 = ax.bar(ind, Q1, width, color='#1f77b4')
p2 = ax.bar(ind, Q2, width, bottom=Q1, color='#ff7f0e')
p3 = ax.bar(ind, Q3, width, bottom=Q1 + Q2, color='#2ca02c')
p4 = ax.bar(ind, Q4, width, bottom=Q1 + Q2 + Q3, color='#d62728')

ax.set_ylabel('Initiatives')
ax.set_title('Environmental Initiatives and Their Quarterly Progress')
ax.set_xticks(ind)
ax.set_xticklabels(topics, rotation=45, ha='right')
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Q1', 'Q2', 'Q3', 'Q4'))
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
ax.bar_label(p4, label_type='center')

plt.show()