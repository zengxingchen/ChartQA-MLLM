import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Mathematics', 'Science', 'History', 'Geography', 'Art', 'Physical Education', 'Language', 'Music', 'Technology', 'Literature'],
    'Group A': [30, 25, 20, 35, 40, 45, 25, 20, 30, 25],
    'Group B': [40, 35, 50, 30, 25, 30, 40, 45, 35, 50],
    'Group C': [30, 40, 30, 35, 35, 25, 35, 35, 35, 25]
}

categories = data['Category']
group_a = data['Group A']
group_b = data['Group B']
group_c = data['Group C']

barWidth = 0.85
bars = np.add(group_a, group_b).tolist()

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(categories, group_a, color='#FF5733', edgecolor='grey', height=barWidth)
ax.barh(categories, group_b, left=group_a, color='#33FF57', edgecolor='grey', height=barWidth)
ax.barh(categories, group_c, left=bars, color='#3357FF', edgecolor='grey', height=barWidth)

plt.xlabel('Percentage')
plt.title('Student Preferences by Subject', pad=20)
plt.legend(['Group A', 'Group B', 'Group C'], loc='upper right', bbox_to_anchor=(1.1, 1))

plt.show()