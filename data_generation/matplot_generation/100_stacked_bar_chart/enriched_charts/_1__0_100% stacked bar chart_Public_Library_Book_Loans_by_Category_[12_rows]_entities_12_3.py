
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
basketball = [30, 25, 20, 15, 10, 20, 25, 30]
soccer = [20, 30, 25, 20, 15, 30, 20, 25]
tennis = [10, 15, 20, 25, 30, 25, 20, 15]
swimming = [25, 20, 15, 30, 20, 15, 25, 20]
running = [15, 10, 20, 10, 25, 10, 10, 10]

# Normalize data to 100%
data = np.array([basketball, soccer, tennis, swimming, running])
data = data / data.sum(axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.5
index = np.arange(len(years))

p1 = ax.bar(index, data[0], bar_width, color='#1f77b4', edgecolor='white', label='Basketball')
p2 = ax.bar(index, data[1], bar_width, bottom=data[0], color='#ff7f0e', edgecolor='white', label='Soccer')
p3 = ax.bar(index, data[2], bar_width, bottom=data[0] + data[1], color='#2ca02c', edgecolor='white', label='Tennis')
p4 = ax.bar(index, data[3], bar_width, bottom=data[0] + data[1] + data[2], color='#d62728', edgecolor='white', label='Swimming')
p5 = ax.bar(index, data[4], bar_width, bottom=data[0] + data[1] + data[2] + data[3], color='#9467bd', edgecolor='white', label='Running')

ax.set_xlabel('Year')
ax.set_ylabel('Participation Percentage')
ax.set_title('Participation in Different Sports (2015-2022)')
ax.set_xticks(index)
ax.set_xticklabels(years)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()