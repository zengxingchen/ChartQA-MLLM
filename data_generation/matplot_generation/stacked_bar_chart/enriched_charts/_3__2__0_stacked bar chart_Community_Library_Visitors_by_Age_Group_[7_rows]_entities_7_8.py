
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
Healthcare = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
Education = np.array([120, 125, 130, 140, 150, 160, 170, 180, 190, 200])
Defense = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
Infrastructure = np.array([170, 180, 190, 200, 210, 220, 230, 240, 250, 260])

bar_height = 0.5
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(years, Healthcare, height=bar_height, label='Healthcare', color='#3498db')
ax.barh(years, Education, left=Healthcare, height=bar_height, label='Education', color='#e74c3c')
ax.barh(years, Defense, left=Healthcare+Education, height=bar_height, label='Defense', color='#2ecc71')
ax.barh(years, Infrastructure, left=Healthcare+Education+Defense, height=bar_height, label='Infrastructure', color='#9b59b6')

ax.set_xlabel('Government Expenditure (in billions)')
ax.set_title('Annual Government Expenditure by Sector (2010-2019)', pad=20)
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend(ncol=2, bbox_to_anchor=(1.05, 1), loc='upper left')

for i in range(len(years)):
    x_offset = Healthcare[i] / 2
    ax.text(x_offset, years[i], Healthcare[i], ha='center', va='center')
    x_offset += Education[i] / 2 + Healthcare[i]
    ax.text(x_offset, years[i], Education[i], ha='center', va='center')
    x_offset += Defense[i] / 2 + Education[i]
    ax.text(x_offset, years[i], Defense[i], ha='center', va='center')
    x_offset += Infrastructure[i] / 2 + Defense[i]
    ax.text(x_offset, years[i], Infrastructure[i], ha='center', va='center')

plt.tight_layout()
plt.show()