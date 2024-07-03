
import matplotlib.pyplot as plt
import numpy as np

# DataFrame-like data
data = {
    'Category': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
    'SegmentA': [20, 25, 30, 10, 15],
    'SegmentB': [10, 35, 20, 40, 30],
    'SegmentC': [30, 10, 25, 20, 25],
    'SegmentD': [40, 30, 25, 30, 30]
}

categories = data['Category']
segments = ['SegmentA', 'SegmentB', 'SegmentC', 'SegmentD']

# Normalize data
normalized_data = {
    segment: np.array(data[segment]) / np.sum([data[s] for s in segments], axis=0) * 100 
    for segment in segments
}

# Prepare plot data
segments_stack = np.row_stack(tuple(normalized_data[segment] for segment in segments))

fig, ax = plt.subplots(figsize=(10, 6))

bar_height = 0.75
y_pos = np.arange(len(categories))

for idx, (segment, color) in enumerate(zip(segments, ['#FF5733', '#33FF57', '#3357FF', '#57FF33'])):
    if idx == 0:
        ax.barh(y_pos, segments_stack[idx], height=bar_height, color=color, edgecolor='white')
    else:
        ax.barh(y_pos, segments_stack[idx], height=bar_height, left=np.sum(segments_stack[:idx], axis=0), 
                color=color, edgecolor='white')

ax.set_yticks(y_pos)
ax.set_yticklabels(categories)

ax.set_title('Product Segmentation Breakdown')
ax.set_xlabel('Percentage')
ax.set_xlim(0, 100)
ax.legend(segments, loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=len(segments))

plt.tight_layout()
plt.show()