
import matplotlib.pyplot as plt
import numpy as np

categories = ['Mental Health', 'Physical Health', 'Nutrition', 'Exercise', 'Sleep', 'Stress Management']
group1 = [35, 40, 20, 25, 30, 25]
group2 = [30, 25, 35, 25, 20, 30]
group3 = [25, 20, 30, 30, 25, 20]
group4 = [10, 15, 15, 20, 25, 25]

barWidth = 0.85

r = np.arange(len(categories))

plt.figure(figsize=(12, 8))

plt.barh(r, group1, color='#FF5733', edgecolor='grey', height=barWidth, label='Group 1')
plt.barh(r, group2, color='#33FF57', edgecolor='grey', height=barWidth, label='Group 2', left=group1)
plt.barh(r, group3, color='#3357FF', edgecolor='grey', height=barWidth, label='Group 3', left=np.array(group1)+np.array(group2))
plt.barh(r, group4, color='#F1C40F', edgecolor='grey', height=barWidth, label='Group 4', left=np.array(group1)+np.array(group2)+np.array(group3))

plt.xlabel('Percentage')
plt.title('Distribution of Health & Psychology Aspects', pad=20)
plt.yticks(r, categories)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()