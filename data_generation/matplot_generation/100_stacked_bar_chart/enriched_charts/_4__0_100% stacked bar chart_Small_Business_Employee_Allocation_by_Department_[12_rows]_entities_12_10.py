import matplotlib.pyplot as plt
import numpy as np

data = [
    [300, 200, 150, 100],
    [320, 210, 160, 110],
    [340, 220, 170, 120],
    [360, 230, 180, 130],
    [380, 240, 190, 140],
    [400, 250, 200, 150],
    [420, 260, 210, 160],
    [440, 270, 220, 170],
    [460, 280, 230, 180],
    [480, 290, 240, 190],
    [500, 300, 250, 200]
]

percent_data = np.array(data) / np.sum(data, axis=1)[:, None]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

plt.figure(figsize=(12, 8))

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

bar_width = 0.6

bottom = np.zeros(len(years))

for idx, (colname, color) in enumerate(zip(['Science', 'Technology', 'Engineering', 'Mathematics'], colors)):
    plt.bar(years, percent_data[:, idx], bottom=bottom, color=color, edgecolor='white', width=bar_width, label=colname)
    bottom += percent_data[:, idx]

plt.ylabel('Percentage of Students')
plt.title('Student Enrollment in STEM Fields (2010-2020)')
plt.xticks(ticks=np.arange(len(years)), labels=years, rotation=45)

plt.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

plt.ylim(0, 1)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()