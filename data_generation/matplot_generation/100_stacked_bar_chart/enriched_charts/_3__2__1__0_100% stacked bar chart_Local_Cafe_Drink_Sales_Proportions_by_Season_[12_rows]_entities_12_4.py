
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028'],
    'Reading': [35, 40, 30, 25, 20, 45, 35, 30, 25, 20],
    'Writing': [25, 20, 30, 35, 30, 15, 25, 30, 35, 30],
    'Math': [25, 30, 20, 20, 30, 25, 25, 20, 20, 30],
    'Science': [15, 10, 20, 20, 20, 15, 15, 20, 20, 20]
}

categories = data['Category']
reading = data['Reading']
writing = data['Writing']
math = data['Math']
science = data['Science']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5

bar_positions = np.arange(len(categories))

ax.barh(bar_positions, reading, color='#1f77b4', edgecolor='black', height=bar_width, label='Reading')
ax.barh(bar_positions, writing, color='#ff7f0e', edgecolor='black', height=bar_width, left=reading, label='Writing')
ax.barh(bar_positions, math, color='#2ca02c', edgecolor='black', height=bar_width, left=np.add(reading, writing), label='Math')
ax.barh(bar_positions, science, color='#d62728', edgecolor='black', height=bar_width, left=np.add(reading, np.add(writing, math)), label='Science')

ax.set_yticks(bar_positions)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage')
ax.set_title('Student Performance Over Years', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

plt.tight_layout()
plt.show()