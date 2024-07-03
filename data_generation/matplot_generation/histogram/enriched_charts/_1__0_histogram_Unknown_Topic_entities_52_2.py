import matplotlib.pyplot as plt

ages = [
    4, 8, 12, 15, 18, 13, 9, 6, 4, 2
]

fig, ax = plt.subplots(figsize=(10, 6))

bin_height = 1
n, bins, patches = ax.hist(ages, bins=range(len(ages) + bin_height), color='#FF6347', edgecolor='#FF4500', alpha=0.75, rwidth=0.8, orientation='vertical')

ax.set_title('Age Distribution in a Sample Population', fontsize=18)
ax.set_ylabel('Frequency', fontsize=14)
ax.set_xlabel('Age Groups', fontsize=14)

ax.set_xticks(range(len(ages)))
ax.set_xticklabels(['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'])

plt.subplots_adjust(bottom=0.15)
plt.show()