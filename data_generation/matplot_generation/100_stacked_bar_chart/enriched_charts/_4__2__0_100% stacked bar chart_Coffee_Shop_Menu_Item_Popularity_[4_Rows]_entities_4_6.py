
import matplotlib.pyplot as plt
import numpy as np

categories = ['Philosophy', 'Ethics', 'Culture', 'Society', 'Health', 'Psychology', 'Environment', 'Climate Change', 
              'Travel', 'Adventure', 'History', 'Archaeology', 'Economics', 'Finance', 'Food', 'Nutrition', 'Sports', 
              'Fitness', 'Business', 'Entrepreneurship', 'Literature', 'Writing', 'Music', 'Performing Arts', 
              'Astronomy', 'Space Exploration', 'Politics', 'Governance', 'Entertainment', 'Leisure', 'Education', 
              'Learning', 'Fashion', 'Beauty', 'Science', 'Nature', 'Future Technologies', 'Society Impact', 
              'Art', 'Design']

subcategory1 = [25, 35, 40, 50, 30, 40, 20, 30, 35, 45, 30, 25, 40, 45, 30, 20, 35, 25, 45, 50, 30, 25, 40, 30, 45, 
                20, 35, 50, 25, 30, 45, 35, 25, 20, 30, 40, 45, 30, 50, 35]
subcategory2 = [45, 40, 35, 30, 50, 30, 30, 25, 40, 25, 35, 45, 30, 25, 50, 30, 30, 40, 30, 25, 35, 40, 30, 50, 25, 
                30, 30, 25, 35, 40, 30, 30, 35, 30, 50, 30, 25, 35, 25, 30]
subcategory3 = [30, 25, 25, 20, 20, 30, 50, 45, 25, 30, 35, 30, 30, 30, 20, 50, 35, 35, 25, 25, 35, 35, 30, 20, 30, 
                50, 35, 25, 40, 30, 25, 35, 40, 50, 20, 30, 30, 35, 25, 35]

barWidth = 0.5
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(16, 10))

ax.bar(r, subcategory1, color='#FF6347', edgecolor='grey', width=barWidth, label='Subcategory 1')
ax.bar(r, subcategory2, bottom=subcategory1, color='#4682B4', edgecolor='grey', width=barWidth, label='Subcategory 2')
ax.bar(r, subcategory3, bottom=np.array(subcategory1) + np.array(subcategory2), color='#32CD32', edgecolor='grey', width=barWidth, label='Subcategory 3')

ax.set_ylabel('Percentage')
ax.set_title('Research Focus Distribution in Various Fields', pad=20)
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=90)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()