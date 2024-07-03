
import matplotlib.pyplot as plt
import numpy as np

# Data
departments = ['Psychiatry', 'Psychology', 'Counseling', 'Rehabilitation', 'Wellness']
Q1_Sessions = np.array([120, 100, 90, 80, 70])
Q2_Sessions = np.array([150, 120, 110, 100, 90])
Q3_Sessions = np.array([200, 180, 140, 120, 110])
Q4_Sessions = np.array([250, 220, 170, 160, 130])

ind = np.arange(len(Q1_Sessions))  # the x locations for the groups
width = 0.6       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(figsize=(12, 10))

p1 = ax.bar(ind, Q1_Sessions, width, color='#1E90FF')
p2 = ax.bar(ind, Q2_Sessions, width, bottom=Q1_Sessions, color='#32CD32')
p3 = ax.bar(ind, Q3_Sessions, width, bottom=Q1_Sessions + Q2_Sessions, color='#FFD700')
p4 = ax.bar(ind, Q4_Sessions, width, bottom=Q1_Sessions + Q2_Sessions + Q3_Sessions, color='#FF6347')

ax.set_ylabel('Number of Sessions')
ax.set_title('Therapy Sessions by Department and Quarter')
ax.set_xticks(ind)
ax.set_xticklabels(departments, rotation=45, ha='right')
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Q1', 'Q2', 'Q3', 'Q4'), loc='upper left')
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
ax.bar_label(p4, label_type='center')

plt.show()