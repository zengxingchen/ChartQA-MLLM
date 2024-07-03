import matplotlib.pyplot as plt
import numpy as np

categories = ['Literature', 'Science', 'History', 'Travel', 'Health', 'Business', 'Sports', 'Music', 'Technology', 'Art']
books = [20, 35, 25, 30, 40, 25, 20, 30, 35, 40]
magazines = [30, 20, 25, 35, 20, 30, 35, 25, 25, 20]
online_articles = [25, 30, 25, 20, 25, 25, 30, 30, 30, 30]
newspapers = [25, 15, 25, 15, 15, 20, 15, 15, 10, 10]

data = np.array([books, magazines, online_articles, newspapers])
data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(12, 7))

category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(['Books', 'Magazines', 'Online Articles', 'Newspapers'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    rects = ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=color)

ax.legend(ncol=len(category_colors), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Reading Preferences by Category', pad=20)
plt.show()