
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
Basketball = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
Soccer = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
Tennis = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
Swimming = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

bar_width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(years, Basketball, width=bar_width, label='Basketball', color='#1f77b4')
ax.bar(years, Soccer, bottom=Basketball, width=bar_width, label='Soccer', color='#ff7f0e')
ax.bar(years, Tennis, bottom=Basketball+Soccer, width=bar_width, label='Tennis', color='#2ca02c')
ax.bar(years, Swimming, bottom=Basketball+Soccer+Tennis, width=bar_width, label='Swimming', color='#d62728')

ax.set_ylabel('Number of Participants (in thousands)')
ax.set_title('Annual Sports Participation (2010-2019)', pad=20)
ax.set_xticks(years)
ax.set_xticklabels(years)
ax.legend(ncol=4, bbox_to_anchor=(0.5, -0.15), loc='upper center')

# Adding numerical labels
for i in range(len(years)):
    y_offset = Basketball[i] / 2
    ax.text(years[i], y_offset, Basketball[i], ha='center', va='bottom')
    y_offset += Soccer[i] / 2 + Basketball[i]
    ax.text(years[i], y_offset, Soccer[i], ha='center', va='bottom')
    y_offset += Tennis[i] / 2 + Soccer[i]
    ax.text(years[i], y_offset, Tennis[i], ha='center', va='bottom')
    y_offset += Swimming[i] / 2 + Tennis[i]
    ax.text(years[i], y_offset, Swimming[i], ha='center', va='bottom')

plt.tight_layout()
plt.show()