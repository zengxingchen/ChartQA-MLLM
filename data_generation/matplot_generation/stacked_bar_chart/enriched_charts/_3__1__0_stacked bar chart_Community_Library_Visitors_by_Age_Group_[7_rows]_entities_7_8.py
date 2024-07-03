
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
cloud_computing = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
ai_ml = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
blockchain = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
iot = np.array([3, 5, 8, 10, 15, 20, 25, 30, 35, 40, 45])

bar_height = 0.6
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(years, cloud_computing, height=bar_height, label='Cloud Computing', color='#1f77b4')
ax.barh(years, ai_ml, left=cloud_computing, height=bar_height, label='AI & Machine Learning', color='#ff7f0e')
ax.barh(years, blockchain, left=cloud_computing+ai_ml, height=bar_height, label='Blockchain', color='#2ca02c')
ax.barh(years, iot, left=cloud_computing+ai_ml+blockchain, height=bar_height, label='IoT', color='#d62728')

ax.set_xlabel('Adoption Rate (%)')
ax.set_title('Adoption Rates of Emerging Technologies (2010-2020)', pad=20)
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years)
ax.legend(ncol=1, loc='lower right', bbox_to_anchor=(1, 0))

# Adding numerical labels
for i, year in enumerate(years):
    ax.text(cloud_computing[i]/2, i, str(cloud_computing[i]), va='center', ha='center', color='white', weight='bold')
    ax.text(cloud_computing[i] + ai_ml[i]/2, i, str(ai_ml[i]), va='center', ha='center', color='white', weight='bold')
    ax.text(cloud_computing[i] + ai_ml[i] + blockchain[i]/2, i, str(blockchain[i]), va='center', ha='center', color='white', weight='bold')
    ax.text(cloud_computing[i] + ai_ml[i] + blockchain[i] + iot[i]/2, i, str(iot[i]), va='center', ha='center', color='white', weight='bold')

plt.tight_layout()
plt.show()