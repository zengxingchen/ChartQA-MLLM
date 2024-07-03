
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
smartphones = np.array([25, 30, 35, 40, 45, 50, 55, 60])
tablets = np.array([20, 22, 24, 26, 28, 30, 32, 34])
laptops = np.array([30, 28, 26, 24, 22, 20, 18, 16])
desktops = np.array([25, 20, 15, 10, 5, 0, 0, 0])

# Normalize the data to sum up to 100%
total = smartphones + tablets + laptops + desktops
smartphones_percent = smartphones / total * 100
tablets_percent = tablets / total * 100
laptops_percent = laptops / total * 100
desktops_percent = desktops / total * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, smartphones_percent, color='#FF5733', edgecolor='white', width=0.6)
ax.bar(years, tablets_percent, bottom=smartphones_percent, color='#33FF57', edgecolor='white', width=0.6)
ax.bar(years, laptops_percent, bottom=smartphones_percent + tablets_percent, color='#3357FF', edgecolor='white', width=0.6)
ax.bar(years, desktops_percent, bottom=smartphones_percent + tablets_percent + laptops_percent, color='#F39C12', edgecolor='white', width=0.6)

# Add some text for labels and custom y-axis tick labels
ax.set_ylabel('Percentage')
ax.set_title('Market Share of Device Types from 2015 to 2022')
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
ax.set_ylim(0, 100)

# Adding legend
ax.legend(['Smartphones', 'Tablets', 'Laptops', 'Desktops'], loc='upper left', bbox_to_anchor=(1.05, 1), fancybox=True, shadow=True)

# Show the percentages on the bars
for i in range(len(years)):
    ax.text(i, smartphones_percent[i]/2, f'{smartphones_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(i, smartphones_percent[i] + tablets_percent[i]/2, f'{tablets_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(i, smartphones_percent[i] + tablets_percent[i] + laptops_percent[i]/2, f'{laptops_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(i, smartphones_percent[i] + tablets_percent[i] + laptops_percent[i] + desktops_percent[i]/2, f'{desktops_percent[i]:.1f}%', va='center', ha='center', color='white')

# Display the plot
plt.tight_layout()
plt.show()