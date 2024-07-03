
import matplotlib.pyplot as plt
import numpy as np

categories = ['Movies', 'TV Shows', 'Theater', 'Concerts', 'Festivals', 'Gaming', 'Sports', 'Reading', 'Cooking', 'Traveling']
books = [25, 35, 20, 30, 40, 25, 30, 35, 40, 45]
magazines = [30, 25, 35, 20, 25, 30, 35, 25, 30, 25]
online_articles = [20, 30, 25, 20, 30, 35, 25, 30, 20, 30]
newspapers = [25, 20, 20, 30, 15, 10, 10, 10, 10, 5]

data = np.array([books, magazines, online_articles, newspapers])
data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(10, 12))

category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(['Books', 'Magazines', 'Online Articles', 'Newspapers'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    rects = ax.barh(categories, widths, left=starts, height=0.5, label=colname, color=color)

ax.legend(ncol=len(category_colors), bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')
plt.title('Entertainment Preferences by Category', pad=20)
plt.show()