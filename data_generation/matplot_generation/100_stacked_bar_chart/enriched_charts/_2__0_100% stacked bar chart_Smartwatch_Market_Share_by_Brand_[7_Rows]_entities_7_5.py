
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Group A': [20, 15, 25, 20, 30, 25, 30, 20, 25],
    'Group B': [25, 30, 20, 35, 25, 30, 20, 25, 30],
    'Group C': [30, 35, 30, 25, 20, 20, 25, 35, 25],
    'Group D': [25, 20, 25, 20, 25, 25, 25, 20, 20]
}

categories = data['Category']
group_A = data['Group A']
group_B = data['Group B']
group_C = data['Group C']
group_D = data['Group D']

barWidth = 0.7
r = np.arange(len(categories))

plt.figure(figsize=(12, 8))

plt.barh(r, group_A, color='#FF5733', edgecolor='white', height=barWidth, label='Group A')
plt.barh(r, group_B, color='#33FF57', edgecolor='white', height=barWidth, left=group_A, label='Group B')
plt.barh(r, group_C, color='#3357FF', edgecolor='white', height=barWidth, left=np.add(group_A, group_B), label='Group C')
plt.barh(r, group_D, color='#FFFF33', edgecolor='white', height=barWidth, left=np.add(np.add(group_A, group_B), group_C), label='Group D')

plt.xlabel('Percentage')
plt.ylabel('Year')
plt.title('Annual Performance of Groups from 2015 to 2023')
plt.yticks(r, categories)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))

plt.show()