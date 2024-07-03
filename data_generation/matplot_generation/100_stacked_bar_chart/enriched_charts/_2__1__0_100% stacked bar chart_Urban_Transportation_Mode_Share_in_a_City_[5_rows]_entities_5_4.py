import matplotlib.pyplot as plt
import numpy as np

categories = ['Running', 'Cycling', 'Swimming', 'Hiking', 'Yoga']
category_A = np.array([10, 20, 30, 25, 15])
category_B = np.array([15, 25, 20, 20, 20])
category_C = np.array([20, 15, 25, 15, 25])
category_D = np.array([25, 25, 15, 30, 10])
category_E = np.array([30, 15, 10, 10, 30])

data = np.vstack([category_A, category_B, category_C, category_D, category_E])
data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.4

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#B2FF66']

for i, (colname, color) in enumerate(zip(['Category A', 'Category B', 'Category C', 'Category D', 'Category E'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Participation in Various Physical Activities')
ax.legend(ncol=5, bbox_to_anchor=(0.5, -0.1), loc='upper center')

plt.show()