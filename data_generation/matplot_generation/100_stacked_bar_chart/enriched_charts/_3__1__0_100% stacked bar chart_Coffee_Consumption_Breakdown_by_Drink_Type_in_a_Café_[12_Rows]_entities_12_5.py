
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [25, 24, 23, 22, 20, 18],
    [15, 16, 15, 14, 13, 12],
    [10, 10, 12, 14, 16, 18],
    [5, 6, 7, 8, 9, 10],
    [20, 21, 22, 23, 24, 25],
    [10, 11, 12, 13, 14, 15],
    [15, 12, 9, 6, 4, 2]
])

categories = ["Cardiovascular Diseases", "Respiratory Diseases", "Infectious Diseases", "Diabetes", "Cancer", "Mental Health Disorders", "Others"]
years = ["2015", "2016", "2017", "2018", "2019", "2020"]

data = data / data.sum(axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.8
bottom = np.zeros(len(years))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

for i in range(len(categories)):
    ax.bar(years, data[i], bar_width, bottom=bottom, color=colors[i], label=categories[i])
    bottom += data[i]

ax.set_title('Distribution of Disease Types Over Years (2015-2020)', fontsize=14, pad=20)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Proportion', fontsize=12)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()