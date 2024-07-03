
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
business_entrepreneurship = [12, 18, 22, 28, 32, 37, 42, 47, 52, 57]
economics_finance = [18, 24, 28, 32, 28, 25, 30, 25, 20, 15]
science_nature = [25, 23, 21, 17, 18, 20, 18, 16, 19, 22]
art_design = [20, 18, 17, 12, 14, 18, 14, 12, 13, 10]
entertainment_leisure = [25, 17, 12, 11, 8, 6, 4, 6, 6, 6]

# Plot
bar_width = 0.35
fig, ax = plt.subplots(figsize=(10, 12))
categories_pos = np.arange(len(categories))

ax.bar(categories_pos, business_entrepreneurship, bar_width, label='Business & Entrepreneurship', color='#4e79a7')
ax.bar(categories_pos, economics_finance, bar_width, bottom=business_entrepreneurship, label='Economics & Finance', color='#f28e2b')
ax.bar(categories_pos, science_nature, bar_width, bottom=np.array(business_entrepreneurship)+np.array(economics_finance), label='Science & Nature', color='#e15759')
ax.bar(categories_pos, art_design, bar_width, bottom=np.array(business_entrepreneurship)+np.array(economics_finance)+np.array(science_nature), label='Art & Design', color='#76b7b2')
ax.bar(categories_pos, entertainment_leisure, bar_width, bottom=np.array(business_entrepreneurship)+np.array(economics_finance)+np.array(science_nature)+np.array(art_design), label='Entertainment & Leisure', color='#59a14f')

# Labels and Title
ax.set_ylabel('Percentage')
ax.set_title('Interest in Various Topics Over Time', pad=20)
ax.set_xticks(categories_pos)
ax.set_xticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()