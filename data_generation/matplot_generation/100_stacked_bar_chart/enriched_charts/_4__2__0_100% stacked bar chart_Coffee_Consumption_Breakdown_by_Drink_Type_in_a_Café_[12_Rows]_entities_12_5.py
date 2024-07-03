
import matplotlib.pyplot as plt
import numpy as np

categories = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
type_A = [15, 20, 18, 25, 22, 26, 24, 28, 25, 23, 27, 25, 20, 26]
type_B = [30, 25, 22, 20, 27, 24, 30, 25, 28, 26, 22, 24, 28, 24]
type_C = [25, 30, 35, 30, 28, 20, 22, 25, 23, 28, 30, 28, 25, 27]
type_D = [30, 25, 25, 25, 23, 30, 24, 22, 24, 23, 21, 23, 27, 23]

type_A = np.array(type_A)
type_B = np.array(type_B)
type_C = np.array(type_C)
type_D = np.array(type_D)

data = np.vstack([type_A, type_B, type_C, type_D])

fig, ax = plt.subplots(figsize=(10, 12))

colors = ['#FF7F50', '#6495ED', '#FFD700', '#ADFF2F']

width = 0.8
bars = ax.bar(categories, type_A, color=colors[0], edgecolor='black', width=width)
bars = ax.bar(categories, type_B, bottom=type_A, color=colors[1], edgecolor='black', width=width)
bars = ax.bar(categories, type_C, bottom=type_A + type_B, color=colors[2], edgecolor='black', width=width)
bars = ax.bar(categories, type_D, bottom=type_A + type_B + type_C, color=colors[3], edgecolor='black', width=width)

ax.set_ylabel('Percentage')
ax.set_title('Annual Distribution of Fitness Activities (2010-2023)', pad=20)
ax.legend(['Type A', 'Type B', 'Type C', 'Type D'], loc='upper left')

plt.tight_layout()
plt.show()