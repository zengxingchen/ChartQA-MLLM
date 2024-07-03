
import matplotlib.pyplot as plt
import numpy as np

# Data
departments = ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Toys']
Q1_Sales = np.array([15000, 10000, 5000, 8000, 4000])
Q2_Sales = np.array([20000, 15000, 10000, 5000, 7000])
Q3_Sales = np.array([25000, 20000, 15000, 6000, 8000])
Q4_Sales = np.array([30000, 15000, 20000, 9000, 5000])

ind = np.arange(len(Q1_Sales))  # the x locations for the departments
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(figsize=(14, 8))

p1 = ax.barh(ind, Q1_Sales, width, color='#FFD700')
p2 = ax.barh(ind, Q2_Sales, width, left=Q1_Sales, color='#C0C0C0')
p3 = ax.barh(ind, Q3_Sales, width, left=Q1_Sales + Q2_Sales, color='#FF4500')
p4 = ax.barh(ind, Q4_Sales, width, left=Q1_Sales + Q2_Sales + Q3_Sales, color='#DA70D6')

ax.set_xlabel('Sales ($)')
ax.set_title('Store Sales by Department and Quarter')
ax.set_yticks(ind)
ax.set_yticklabels(departments)
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Q1', 'Q2', 'Q3', 'Q4'))
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
ax.bar_label(p4, label_type='center')

plt.show()