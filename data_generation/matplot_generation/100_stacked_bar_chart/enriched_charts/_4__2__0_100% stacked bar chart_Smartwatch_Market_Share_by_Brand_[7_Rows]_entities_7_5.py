import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Group A': [15, 20, 25, 20, 30, 25, 20, 25, 30, 20],
    'Group B': [25, 30, 20, 25, 35, 30, 25, 20, 30, 25],
    'Group C': [35, 25, 30, 25, 20, 30, 35, 30, 20, 35],
    'Group D': [25, 25, 25, 30, 15, 15, 20, 25, 20, 20]
}

categories = data['Category']
group_A = data['Group A']
group_B = data['Group B']
group_C = data['Group C']
group_D = data['Group D']

barWidth = 0.7
r = np.arange(len(categories))

plt.figure(figsize=(10, 15))

plt.bar(r, group_A, color='#FF5733', edgecolor='white', width=barWidth, label='Group A')
plt.bar(r, group_B, color='#33FF57', edgecolor='white', width=barWidth, bottom=group_A, label='Group B')
plt.bar(r, group_C, color='#3357FF', edgecolor='white', width=barWidth, bottom=np.add(group_A, group_B), label='Group C')
plt.bar(r, group_D, color='#FFFF33', edgecolor='white', width=barWidth, bottom=np.add(np.add(group_A, group_B), group_C), label='Group D')

plt.ylabel('Percentage')
plt.xlabel('City')
plt.title('Population Distribution by Group in Various Cities')
plt.xticks(r, categories, rotation=45, ha='right')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()