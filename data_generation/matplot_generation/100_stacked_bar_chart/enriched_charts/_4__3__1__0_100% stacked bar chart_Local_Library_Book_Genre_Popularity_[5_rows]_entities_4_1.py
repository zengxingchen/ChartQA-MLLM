
import matplotlib.pyplot as plt
import numpy as np

categories = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
agriculture = np.array([20, 22, 25, 27, 28, 30, 32, 35, 37, 38, 40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57])
industry = np.array([30, 28, 26, 25, 24, 23, 22, 21, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7])
services = np.array([40, 41, 42, 40, 40, 38, 37, 35, 34, 34, 33, 33, 32, 31, 31, 30, 29, 28, 28, 27, 26])
technology = np.array([10, 9, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

bar_width = 0.7
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(categories, agriculture, color='#4CAF50', edgecolor='white', width=bar_width)
ax.bar(categories, industry, bottom=agriculture, color='#FF9800', edgecolor='white', width=bar_width)
ax.bar(categories, services, bottom=agriculture+industry, color='#2196F3', edgecolor='white', width=bar_width)
ax.bar(categories, technology, bottom=agriculture+industry+services, color='#9C27B0', edgecolor='white', width=bar_width)

ax.set_title('Sector Distribution Over Time (2010-2030)', fontsize=16, pad=20)
ax.set_ylabel('Percentage', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

ax.legend(['Agriculture', 'Industry', 'Services', 'Technology'], loc='upper left')

plt.tight_layout()
plt.show()