
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
AI_Robotics = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
Blockchain = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
Renewable_Energy = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110])
Virtual_Reality = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

bar_width = 0.25
fig, ax = plt.subplots(figsize=(16, 12))

ax.barh(years, AI_Robotics, height=bar_width, label='AI & Robotics', color='#1f77b4')
ax.barh(years, Blockchain, left=AI_Robotics, height=bar_width, label='Blockchain', color='#ff7f0e')
ax.barh(years, Renewable_Energy, left=AI_Robotics+Blockchain, height=bar_width, label='Renewable Energy', color='#2ca02c')
ax.barh(years, Virtual_Reality, left=AI_Robotics+Blockchain+Renewable_Energy, height=bar_width, label='Virtual Reality', color='#d62728')

ax.set_xlabel('Investments in Billion $')
ax.set_title('Investments in Future Technologies (2010-2024)', pad=30)
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years)
ax.legend(ncol=1, loc='upper right', bbox_to_anchor=(1, 1))

# Adding numerical labels
for i in range(len(years)):
    ax.text(AI_Robotics[i] / 2, i, str(AI_Robotics[i]), ha='center', va='center', color='white', fontsize=10)
    ax.text(AI_Robotics[i] + Blockchain[i] / 2, i, str(Blockchain[i]), ha='center', va='center', color='white', fontsize=10)
    ax.text(AI_Robotics[i] + Blockchain[i] + Renewable_Energy[i] / 2, i, str(Renewable_Energy[i]), ha='center', va='center', color='white', fontsize=10)
    ax.text(AI_Robotics[i] + Blockchain[i] + Renewable_Energy[i] + Virtual_Reality[i] / 2, i, str(Virtual_Reality[i]), ha='center', va='center', color='white', fontsize=10)

plt.tight_layout()
plt.show()