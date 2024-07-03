
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2018', '2019', '2020', '2021', '2022', '2023']
depression = [20, 22, 25, 27, 30, 28]
anxiety = [25, 28, 30, 35, 33, 38]
diabetes = [15, 18, 20, 22, 25, 30]
hypertension = [40, 32, 25, 16, 12, 10]

# Stack data
data = np.array([depression, anxiety, diabetes, hypertension])
data_cum = data.cumsum(axis=0)

# Category names
categories = ['Depression', 'Anxiety', 'Diabetes', 'Hypertension']
category_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.bar(years, widths, bottom=starts, width=bar_width, label=colname, color=color)

# Add labels and title
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Different Health Issues Reported Over Years', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.0))

plt.tight_layout()
plt.show()