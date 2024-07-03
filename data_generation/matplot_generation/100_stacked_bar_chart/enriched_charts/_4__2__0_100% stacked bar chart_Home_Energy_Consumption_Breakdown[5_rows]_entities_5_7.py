
import matplotlib.pyplot as plt
import numpy as np

categories = ['Exercise & Fitness', 'Mental Health', 'Nutrition', 'Sleep Quality', 'Stress Management', 'Social Interaction', 'Hygiene', 'Disease Prevention', 'Addiction Recovery', 'Health Education']
option1 = [35, 45, 30, 50, 40, 25, 35, 40, 25, 45]
option2 = [25, 35, 40, 30, 20, 45, 35, 30, 40, 25]
option3 = [40, 20, 30, 20, 40, 30, 30, 30, 35, 30]

data = np.array([option1, option2, option3])
data_cum = data.cumsum(axis=0)

category_colors = ['#FF6347', '#4682B4', '#3CB371']
bar_width = 0.85
fig_width, fig_height = 12, 8

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.set_xlim(0, np.sum(data, axis=0).max())
ax.set_ylim(0, len(categories))
ax.xaxis.set_visible(False)
ax.invert_yaxis()

for i, (colname, color) in enumerate(zip(['Option 1', 'Option 2', 'Option 3'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.legend(ncol=3, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')
ax.set_title('Health & Wellness Initiatives', pad=20)

plt.show()