import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 18, 22, 24, 26, 28],
    [15, 17, 20, 22, 25, 27],
    [10, 12, 15, 18, 20, 22],
    [25, 23, 20, 18, 15, 12],
    [20, 18, 22, 24, 26, 28],
    [10, 12, 14, 16, 18, 20]
])

categories = ["History", "Geography", "Physics", "Mathematics", "Computer Science", "Art"]
years = ["2015", "2016", "2017", "2018", "2019", "2020"]

data = data / data.sum(axis=0)

fig, ax = plt.subplots(figsize=(8, 10))

bar_width = 0.7
bottom = np.zeros(len(years))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF3', '#FF8633']

for i in range(len(categories)):
    ax.bar(years, data[i], bar_width, bottom=bottom, color=colors[i], label=categories[i])
    bottom += data[i]

ax.set_title('Distribution of Subjects Over Years (2015-2020)', fontsize=14, pad=20)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Proportion', fontsize=12)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

plt.show()