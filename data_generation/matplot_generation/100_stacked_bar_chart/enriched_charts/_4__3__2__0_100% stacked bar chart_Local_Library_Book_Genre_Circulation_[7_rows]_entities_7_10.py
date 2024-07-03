
import matplotlib.pyplot as plt
import numpy as np

categories = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E', 'Region F', 'Region G', 'Region H']
running_scores = [70, 65, 85, 60, 75, 80, 90, 55]
cycling_scores = [50, 55, 65, 60, 70, 75, 80, 50]
swimming_scores = [80, 75, 90, 70, 85, 95, 100, 65]

data = np.array([running_scores, cycling_scores, swimming_scores])
data_cum = data.cumsum(axis=0)

colors = ["#3498db", "#e74c3c", "#2ecc71"]

fig, ax = plt.subplots(figsize=(12, 8))
category_labels = categories
bar_width = 0.6

for i, (colname, color) in enumerate(zip(['Running', 'Cycling', 'Swimming'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(category_labels, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Physical Activity Participation by Region')
ax.legend(loc='upper left')
plt.show()