
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Mathematics': [15, 20, 25, 30, 35],
    'Physics': [20, 25, 30, 35, 25],
    'Chemistry': [25, 20, 30, 25, 20],
    'Biology': [30, 35, 20, 15, 25],
    'Computer Science': [10, 15, 20, 25, 30],
    'English': [20, 15, 10, 10, 15]
}

labels = data['Year']
math = data['Mathematics']
physics = data['Physics']
chemistry = data['Chemistry']
biology = data['Biology']
comp_sci = data['Computer Science']
english = data['English']

width = 0.75
bar_width = 0.6
fig, ax = plt.subplots(figsize=(12, 8))

bar1 = np.add(math, physics).tolist()
bar2 = np.add(bar1, chemistry).tolist()
bar3 = np.add(bar2, biology).tolist()
bar4 = np.add(bar3, comp_sci).tolist()

ax.bar(labels, math, color='#FF5733', edgecolor='white', width=bar_width, label='Mathematics')
ax.bar(labels, physics, bottom=math, color='#33FF57', edgecolor='white', width=bar_width, label='Physics')
ax.bar(labels, chemistry, bottom=bar1, color='#3357FF', edgecolor='white', width=bar_width, label='Chemistry')
ax.bar(labels, biology, bottom=bar2, color='#FF33A1', edgecolor='white', width=bar_width, label='Biology')
ax.bar(labels, comp_sci, bottom=bar3, color='#A133FF', edgecolor='white', width=bar_width, label='Computer Science')
ax.bar(labels, english, bottom=bar4, color='#FFC300', edgecolor='white', width=bar_width, label='English')

ax.set_ylabel('Percentage (%)')
ax.set_title('Student Subject Preferences (2018-2022)', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.show()