import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing', 'Education', 'Transportation', 'Energy'],
    'Segment A': [30, 25, 20, 35, 40, 50, 45, 55],
    'Segment B': [40, 50, 30, 45, 30, 25, 35, 20],
    'Segment C': [30, 25, 50, 20, 30, 25, 20, 25]
}

categories = data['Category']
segments = ['Segment A', 'Segment B', 'Segment C']
values = np.array([data[segment] for segment in segments])

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.85

left = np.zeros(len(categories))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, segment in enumerate(segments):
    ax.barh(categories, values[i], left=left, height=bar_width, label=segment, color=colors[i])
    left += values[i]

ax.set_xlabel('Percentage')
ax.set_title('Segment Distribution Across Various Industries')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))

plt.tight_layout()
plt.show()