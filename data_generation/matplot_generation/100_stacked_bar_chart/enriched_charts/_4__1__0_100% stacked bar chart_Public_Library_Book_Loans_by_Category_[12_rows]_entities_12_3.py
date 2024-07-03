
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
math = [50, 45, 40, 35, 30, 25, 20, 15]
science = [20, 25, 30, 25, 20, 30, 25, 30]
history = [10, 15, 10, 15, 25, 15, 20, 25]
art = [5, 5, 10, 10, 10, 5, 15, 10]
music = [10, 5, 5, 10, 5, 10, 10, 10]
pe = [5, 5, 5, 5, 10, 15, 10, 10]

# Normalize data to 100%
data = np.array([math, science, history, art, music, pe])
data = data / data.sum(axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6
index = np.arange(len(years))

p1 = ax.bar(index, data[0], bar_width, color='#3366cc', edgecolor='white', label='Math')
p2 = ax.bar(index, data[1], bar_width, bottom=data[0], color='#dc3912', edgecolor='white', label='Science')
p3 = ax.bar(index, data[2], bar_width, bottom=data[0] + data[1], color='#ff9900', edgecolor='white', label='History')
p4 = ax.bar(index, data[3], bar_width, bottom=data[0] + data[1] + data[2], color='#109618', edgecolor='white', label='Art')
p5 = ax.bar(index, data[4], bar_width, bottom=data[0] + data[1] + data[2] + data[3], color='#990099', edgecolor='white', label='Music')
p6 = ax.bar(index, data[5], bar_width, bottom=data[0] + data[1] + data[2] + data[3] + data[4], color='#0099c6', edgecolor='white', label='Physical Education')

ax.set_xlabel('Year')
ax.set_ylabel('Percentage of Students')
ax.set_title('Student Participation in Different Subjects (2015-2022)', pad=20)
ax.set_xticks(index)
ax.set_xticklabels(years)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

plt.show()