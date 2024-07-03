
import matplotlib.pyplot as plt
import numpy as np

categories = ['Pop', 'Pop', 'Pop', 'Rock', 'Rock', 'Rock', 'Classical', 'Classical', 'Classical', 'Jazz', 'Jazz', 'Jazz']
years = ['2015', '2016', '2017', '2015', '2016', '2017', '2015', '2016', '2017', '2015', '2016', '2017']
group_A = [15, 20, 25, 30, 35, 20, 25, 20, 30, 25, 20, 25]
group_B = [25, 20, 30, 20, 25, 30, 20, 25, 20, 30, 35, 20]
group_C = [35, 40, 25, 25, 20, 25, 30, 25, 25, 25, 20, 30]
group_D = [25, 20, 20, 25, 20, 25, 25, 30, 25, 20, 25, 25]

fig, ax = plt.subplots(figsize=(12, 9))
bar_width = 0.6

ind = np.arange(len(categories))
p1 = plt.bar(ind, group_A, bar_width, color='#1f77b4')
p2 = plt.bar(ind, group_B, bar_width, bottom=group_A, color='#ff7f0e')
p3 = plt.bar(ind, group_C, bar_width, bottom=np.add(group_A, group_B), color='#2ca02c')
p4 = plt.bar(ind, group_D, bar_width, bottom=np.add(np.add(group_A, group_B), group_C), color='#d62728')

plt.ylabel('Percentage')
plt.xlabel('Music Genre and Year')
plt.title('Music Genre Popularity Over Years')
plt.xticks(ind, ['Pop 2015', 'Pop 2016', 'Pop 2017', 'Rock 2015', 'Rock 2016', 'Rock 2017', 'Classical 2015', 'Classical 2016', 'Classical 2017', 'Jazz 2015', 'Jazz 2016', 'Jazz 2017'], rotation=45, ha='right')
plt.yticks(np.arange(0, 101, 10))

plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Group A', 'Group B', 'Group C', 'Group D'), loc='upper left')

plt.tight_layout()
plt.show()