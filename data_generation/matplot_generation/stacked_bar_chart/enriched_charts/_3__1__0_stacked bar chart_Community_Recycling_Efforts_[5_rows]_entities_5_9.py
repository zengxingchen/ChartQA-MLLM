
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sector_a = [100, 110, 120, 130]
sector_b = [150, 160, 170, 180]
sector_c = [200, 210, 220, 230]
sector_d = [120, 130, 140, 150]

x = np.arange(len(quarters))  # the label locations
height = 0.6  # the height of the bars

fig, ax = plt.subplots(figsize=(14, 8))  # Changing width and height of the chart

# Stacked horizontal bar chart
ax.barh(x, sector_a, height, label='Sector A', color='#FF6347')
ax.barh(x, sector_b, height, left=sector_a, label='Sector B', color='#4682B4')
ax.barh(x, sector_c, height, left=np.add(sector_a, sector_b), label='Sector C', color='#3CB371')
ax.barh(x, sector_d, height, left=np.add(np.add(sector_a, sector_b), sector_c), label='Sector D', color='#FFD700')

# Add some text for labels and custom x-axis tick labels
ax.set_xlabel('Revenue (Million $)')
ax.set_title('Quarterly Revenue by Business Sector', pad=20)
ax.set_yticks(x)
ax.set_yticklabels(quarters)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adding numerical labels to each bar
for i in range(len(quarters)):
    ax.text(sector_a[i] / 2, i, str(sector_a[i]), va='center', ha='center', color='white')
    ax.text(sector_a[i] + sector_b[i] / 2, i, str(sector_b[i]), va='center', ha='center', color='white')
    ax.text(sector_a[i] + sector_b[i] + sector_c[i] / 2, i, str(sector_c[i]), va='center', ha='center', color='white')
    ax.text(sector_a[i] + sector_b[i] + sector_c[i] + sector_d[i] / 2, i, str(sector_d[i]), va='center', ha='center', color='white')

plt.show()