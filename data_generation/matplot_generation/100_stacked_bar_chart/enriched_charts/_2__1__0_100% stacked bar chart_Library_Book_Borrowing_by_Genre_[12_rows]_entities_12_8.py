import matplotlib.pyplot as plt
import numpy as np

categories = ['Trekking', 'Safari', 'Mountain Climbing', 'Scuba Diving', 'Paragliding', 'Wildlife Watching', 'Sky Diving', 'Rafting', 'Kayaking', 'Camping']
data = {
    '2019': [20, 15, 30, 35, 10, 15, 10, 25, 20, 30],
    '2020': [25, 20, 35, 20, 15, 25, 15, 20, 25, 35],
    '2021': [30, 25, 30, 15, 20, 25, 20, 20, 30, 25]
}

labels = list(data.keys())
data = np.array(list(data.values()))
data_cum = data.cumsum(axis=0)

category_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B2', '#FF6666', '#66FFB2', '#9999FF', '#B2FF66', '#FFB266']

fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.5

for i, (colname, color) in enumerate(zip(labels, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Travel & Adventure Activities Popularity Over Years', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05))

plt.tight_layout()
plt.show()