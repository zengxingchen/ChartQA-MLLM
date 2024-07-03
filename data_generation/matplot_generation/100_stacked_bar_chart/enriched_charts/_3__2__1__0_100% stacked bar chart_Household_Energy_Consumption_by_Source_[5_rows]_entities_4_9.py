
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'France', 'Japan', 'Germany', 'Australia', 'Canada', 'UK', 'China', 'India', 'Brazil'],
    'Car': [30, 25, 20, 35, 40, 30, 25, 20, 15, 30],
    'Train': [25, 35, 30, 20, 15, 20, 25, 25, 30, 20],
    'Plane': [15, 10, 20, 10, 20, 25, 20, 30, 25, 20],
    'Bike': [10, 15, 5, 20, 10, 10, 10, 5, 5, 10],
    'Bus': [20, 15, 25, 15, 15, 15, 20, 20, 25, 20]
}

categories = ['Car', 'Train', 'Plane', 'Bike', 'Bus']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33']

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.5

for i, cat in enumerate(categories):
    starts = np.zeros(len(data['Country']))
    for j in range(i):
        starts += np.array(data[categories[j]])
    ax.barh(data['Country'], data[cat], left=starts, height=width, label=cat, color=colors[i])

ax.set_xlabel('Percentage')
ax.set_title('Modes of Transportation Used by Tourists in Various Countries')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()