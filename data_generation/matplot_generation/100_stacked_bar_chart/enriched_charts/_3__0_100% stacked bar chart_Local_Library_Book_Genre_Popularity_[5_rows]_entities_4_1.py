import matplotlib.pyplot as plt
import numpy as np

categories = ['Math', 'Science', 'History', 'English', 'Art', 'Music', 'Physical Education', 'Foreign Language', 'Computer Science', 'Social Studies']
online = [40, 55, 65, 50, 70, 60, 45, 35, 75, 50]
in_person = [60, 45, 35, 50, 30, 40, 55, 65, 25, 50]

barWidth = 0.6
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(r, online, color='#FF5733', edgecolor='grey', height=barWidth, label='Online')
ax.barh(r, in_person, left=online, color='#33FF57', edgecolor='grey', height=barWidth, label='In-Person')

ax.set_xlabel('Percentage')
ax.set_title('Education Methods Distribution', pad=20)
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))

plt.tight_layout()
plt.show()