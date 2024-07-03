
import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
north_america = np.array([15000, 18000, 17000, 20000])
europe = np.array([12000, 13000, 14000, 16000])
asia = np.array([10000, 11000, 12000, 13000])
south_america = np.array([7000, 8000, 9000, 10000])

total_revenue = north_america + europe + asia + south_america
north_america_percentage = (north_america / total_revenue) * 100
europe_percentage = (europe / total_revenue) * 100
asia_percentage = (asia / total_revenue) * 100
south_america_percentage = (south_america / total_revenue) * 100

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

bar_positions = np.arange(len(quarters))

rects1 = ax.bar(bar_positions, north_america_percentage, bar_width, color='#1f77b4', label='North America')
rects2 = ax.bar(bar_positions, europe_percentage, bar_width, bottom=north_america_percentage, color='#ff7f0e', label='Europe')
rects3 = ax.bar(bar_positions, asia_percentage, bar_width, bottom=north_america_percentage + europe_percentage, color='#2ca02c', label='Asia')
rects4 = ax.bar(bar_positions, south_america_percentage, bar_width, bottom=north_america_percentage + europe_percentage + asia_percentage, color='#d62728', label='South America')

ax.set_ylabel('Percentage (%)')
ax.set_title('Quarterly Revenue Distribution by Region')
ax.set_xticks(bar_positions)
ax.set_xticklabels(quarters)
ax.set_ylim(0, 100)

ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()