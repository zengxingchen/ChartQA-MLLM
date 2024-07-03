
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
philosophy_ethics = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
history_archaeology = [20, 25, 30, 35, 25, 20, 25, 20, 15, 10]
literature_writing = [30, 20, 10, 15, 20, 25, 20, 15, 20, 15]
science_nature = [25, 25, 25, 15, 15, 10, 10, 15, 10, 15]
entertainment_leisure = [15, 15, 15, 10, 10, 10, 5, 5, 5, 5]

# Plot
bar_width = 0.5
fig, ax = plt.subplots(figsize=(12, 8))
categories_pos = np.arange(len(categories))

ax.barh(categories_pos, philosophy_ethics, bar_width, label='Philosophy & Ethics', color='#1f77b4')
ax.barh(categories_pos, history_archaeology, bar_width, left=philosophy_ethics, label='History & Archaeology', color='#ff7f0e')
ax.barh(categories_pos, literature_writing, bar_width, left=np.array(philosophy_ethics)+np.array(history_archaeology), label='Literature & Writing', color='#2ca02c')
ax.barh(categories_pos, science_nature, bar_width, left=np.array(philosophy_ethics)+np.array(history_archaeology)+np.array(literature_writing), label='Science & Nature', color='#d62728')
ax.barh(categories_pos, entertainment_leisure, bar_width, left=np.array(philosophy_ethics)+np.array(history_archaeology)+np.array(literature_writing)+np.array(science_nature), label='Entertainment & Leisure', color='#9467bd')

# Labels and Title
ax.set_xlabel('Percentage')
ax.set_title('Interest in Various Academic Topics Over Time', pad=20)
ax.set_yticks(categories_pos)
ax.set_yticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()