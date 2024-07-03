
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'],
    'Advertising': [40, 35, 30, 45, 35, 30, 40, 35, 30, 45, 40, 35, 30, 45, 40, 35],
    'Subscription': [25, 30, 35, 20, 30, 30, 25, 30, 35, 20, 25, 30, 35, 20, 25, 30],
    'Merchandise': [20, 25, 25, 20, 25, 30, 20, 25, 25, 20, 20, 25, 25, 20, 20, 25],
    'Other': [15, 10, 10, 15, 10, 10, 15, 10, 10, 15, 15, 10, 10, 15, 15, 10]
}

years = data['Year']
advertising = data['Advertising']
subscription = data['Subscription']
merchandise = data['Merchandise']
other = data['Other']

fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.75

bar_positions = np.arange(len(years))

ax.bar(bar_positions, advertising, color='#1f77b4', edgecolor='black', width=bar_width, label='Advertising')
ax.bar(bar_positions, subscription, color='#ff7f0e', edgecolor='black', width=bar_width, bottom=advertising, label='Subscription')
ax.bar(bar_positions, merchandise, color='#2ca02c', edgecolor='black', width=bar_width, bottom=np.add(advertising, subscription), label='Merchandise')
ax.bar(bar_positions, other, color='#d62728', edgecolor='black', width=bar_width, bottom=np.add(advertising, np.add(subscription, merchandise)), label='Other')

ax.set_xticks(bar_positions)
ax.set_xticklabels(years, rotation=45)
ax.set_ylabel('Percentage')
ax.set_title('Revenue Distribution Over Years', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()