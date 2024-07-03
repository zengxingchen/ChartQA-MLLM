
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'France', 'Japan', 'Germany', 'Australia', 'Canada', 'UK', 'China', 'India', 'Brazil'],
    'Running': [25, 20, 15, 30, 35, 25, 20, 15, 20, 30],
    'Swimming': [15, 25, 20, 15, 20, 25, 20, 25, 15, 20],
    'Cycling': [20, 15, 25, 20, 15, 20, 25, 20, 25, 15],
    'Walking': [30, 25, 20, 25, 20, 20, 20, 25, 20, 20],
    'Yoga': [10, 15, 20, 10, 10, 10, 15, 15, 20, 15]
}

categories = ['Running', 'Swimming', 'Cycling', 'Walking', 'Yoga']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33']

fig, ax = plt.subplots(figsize=(10, 12))
width = 0.7

for i, cat in enumerate(categories):
    starts = np.zeros(len(data['Country']))
    for j in range(i):
        starts += np.array(data[categories[j]])
    ax.bar(data['Country'], data[cat], bottom=starts, width=width, label=cat, color=colors[i])

ax.set_ylabel('Percentage')
ax.set_title('Types of Physical Activities Done by People in Various Countries')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()