import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Art', 'Design', 'Literature', 'Music', 'Theater', 'Film', 'Photography']
segment_A = [20, 25, 30, 20, 25, 35, 20]
segment_B = [30, 35, 25, 25, 20, 25, 30]
segment_C = [25, 20, 20, 35, 30, 20, 25]
segment_D = [25, 20, 25, 20, 25, 20, 25]

# Convert data to percentages
totals = np.array(segment_A) + np.array(segment_B) + np.array(segment_C) + np.array(segment_D)
segment_A = np.array(segment_A) / totals * 100
segment_B = np.array(segment_B) / totals * 100
segment_C = np.array(segment_C) / totals * 100
segment_D = np.array(segment_D) / totals * 100

# Stacked bar chart
barWidth = 0.5
r = range(len(categories))

plt.figure(figsize=(12, 7))

plt.barh(r, segment_A, color='#FF5733', edgecolor='white', height=barWidth, label='Segment A')
plt.barh(r, segment_B, left=segment_A, color='#33FF57', edgecolor='white', height=barWidth, label='Segment B')
plt.barh(r, segment_C, left=segment_A + segment_B, color='#3357FF', edgecolor='white', height=barWidth, label='Segment C')
plt.barh(r, segment_D, left=segment_A + segment_B + segment_C, color='#FF33A6', edgecolor='white', height=barWidth, label='Segment D')

# Customizing the plot
plt.xlabel('Percentage')
plt.title('Distribution of Segments in Art & Design', pad=20)
plt.yticks(r, categories)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()