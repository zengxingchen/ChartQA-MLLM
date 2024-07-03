
import matplotlib.pyplot as plt
import numpy as np

categories = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'South Africa', 'Russia', 'Mexico', 'South Korea', 'Italy']
reading = [25, 22, 28, 30, 32, 25, 35, 30, 32, 28, 30, 25, 32, 25, 28]
gaming = [30, 25, 18, 20, 22, 30, 15, 25, 20, 22, 18, 25, 22, 30, 22]
traveling = [20, 23, 25, 20, 25, 25, 25, 20, 25, 25, 25, 25, 20, 20, 25]
music = [25, 30, 29, 30, 21, 20, 25, 25, 23, 25, 27, 25, 26, 25, 25]

data = np.array([reading, gaming, traveling, music])
data_cum = data.cumsum(axis=0)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 8))

ax.invert_xaxis()
ax.yaxis.set_visible(False)
ax.set_ylim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(['Reading', 'Gaming', 'Traveling', 'Music'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    rects = ax.bar(categories, heights, bottom=starts, width=0.7, label=colname, color=color)

ax.legend(ncol=4, bbox_to_anchor=(0.5, 1.02), loc='center', fontsize='small')
ax.set_title('Preferred Hobbies by Country', pad=20)

plt.show()