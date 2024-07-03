
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['History', 'Literature', 'Food', 'Culture', 'Health', 'Art', 'Technology', 'Science', 'Business', 'Finance'],
    'SegmentA': [30, 35, 25, 15, 20, 25, 30, 20, 25, 30],
    'SegmentB': [20, 25, 30, 25, 30, 20, 25, 30, 25, 20],
    'SegmentC': [25, 20, 20, 30, 25, 30, 20, 25, 30, 25],
    'SegmentD': [25, 20, 25, 30, 25, 25, 25, 25, 20, 25]
}

categories = data['Category']
segments = ['SegmentA', 'SegmentB', 'SegmentC', 'SegmentD']

normalized_data = {
    segment: np.array(data[segment]) / np.sum([data[s] for s in segments], axis=0) * 100 
    for segment in segments
}

segments_stack = np.row_stack(tuple(normalized_data[segment] for segment in segments))

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.65
x_pos = np.arange(len(categories))

for idx, (segment, color) in enumerate(zip(segments, ['#FF5733', '#33A1FF', '#FFC300', '#DAF7A6'])):
    if idx == 0:
        ax.bar(x_pos, segments_stack[idx], width=bar_width, color=color, edgecolor='white')
    else:
        ax.bar(x_pos, segments_stack[idx], width=bar_width, bottom=np.sum(segments_stack[:idx], axis=0), 
               color=color, edgecolor='white')

ax.set_xticks(x_pos)
ax.set_xticklabels(categories, rotation=45, ha='right')

ax.set_title('Interests in Various Categories', pad=20)
ax.set_ylabel('Percentage')
ax.set_ylim(0, 100)
ax.legend(segments, loc='upper right', bbox_to_anchor=(1.2, 1),
          fancybox=True, shadow=True, ncol=1)

plt.tight_layout()
plt.show()