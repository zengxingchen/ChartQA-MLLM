
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Group I', 'Group J', 
                 'Group K', 'Group L', 'Group M', 'Group N', 'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T', 
                 'Group U', 'Group V', 'Group W', 'Group X', 'Group Y', 'Group Z'],
    'Adventure': [20, 25, 30, 20, 25, 20, 25, 30, 20, 25, 30, 20, 25, 30, 25, 20, 25, 30, 25, 20, 25, 30, 25, 30, 25, 20],
    'Beach': [30, 20, 25, 25, 30, 15, 20, 25, 30, 20, 25, 25, 30, 15, 20, 30, 20, 25, 30, 30, 20, 25, 30, 20, 20, 30],
    'City': [25, 30, 20, 30, 15, 30, 15, 20, 25, 30, 20, 30, 15, 25, 30, 25, 30, 20, 15, 25, 30, 20, 15, 25, 30, 25],
    'Nature': [15, 15, 15, 15, 20, 25, 30, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    'Wildlife': [10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 10, 15, 15, 15, 20, 15, 15, 15, 20, 15, 15, 15]
}

categories = data['Category']
adventure = data['Adventure']
beach = data['Beach']
city = data['City']
nature = data['Nature']
wildlife = data['Wildlife']

ind = np.arange(len(categories))
width = 0.8

fig, ax = plt.subplots(figsize=(12, 14))

p1 = ax.bar(ind, adventure, width, color='#1f77b4')
p2 = ax.bar(ind, beach, width, bottom=adventure, color='#ff7f0e')
p3 = ax.bar(ind, city, width, bottom=np.array(adventure) + np.array(beach), color='#2ca02c')
p4 = ax.bar(ind, nature, width, bottom=np.array(adventure) + np.array(beach) + np.array(city), color='#d62728')
p5 = ax.bar(ind, wildlife, width, bottom=np.array(adventure) + np.array(beach) + np.array(city) + np.array(nature), color='#9467bd')

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Travel Preferences Among Different Groups')
ax.set_xticks(ind)
ax.set_xticklabels(categories, rotation=90)
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Adventure', 'Beach', 'City', 'Nature', 'Wildlife'), loc='upper right')

plt.show()