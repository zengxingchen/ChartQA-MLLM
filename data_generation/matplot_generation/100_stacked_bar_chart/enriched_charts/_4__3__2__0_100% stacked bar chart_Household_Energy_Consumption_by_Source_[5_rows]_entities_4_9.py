
import matplotlib.pyplot as plt
import numpy as np

categories = ['Solar', 'Wind', 'Geothermal', 'Biomass', 'Tidal', 'Wave', 'Hydrogen']
renewable = [30, 25, 20, 35, 40, 25, 30]
non_renewable = [20, 25, 30, 25, 20, 35, 30]
nuclear = [10, 10, 15, 20, 10, 15, 20]
hydropower = [40, 40, 35, 20, 30, 25, 20]

barWidth = 0.7
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(r, renewable, color='#FFA07A', edgecolor='white', width=barWidth, label='Renewable Energy')
ax.bar(r, non_renewable, bottom=renewable, color='#20B2AA', edgecolor='white', width=barWidth, label='Non-Renewable Energy')
ax.bar(r, nuclear, bottom=np.add(renewable, non_renewable), color='#778899', edgecolor='white', width=barWidth, label='Nuclear Energy')
ax.bar(r, hydropower, bottom=np.add(np.add(renewable, non_renewable), nuclear), color='#6495ED', edgecolor='white', width=barWidth, label='Hydropower')

ax.set_ylabel('Percentage')
ax.set_title('Energy Sources Distribution', pad=20)
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(loc='upper right', bbox_to_anchor=(1.2,1))

plt.tight_layout()
plt.show()