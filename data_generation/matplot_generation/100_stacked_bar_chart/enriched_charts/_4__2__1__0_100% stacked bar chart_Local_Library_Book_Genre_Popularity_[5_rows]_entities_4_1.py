
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E', 'Company F', 'Company G', 'Company H', 'Company I', 'Company J']
marketing = [20, 25, 30, 15, 10, 20, 25, 30, 15, 10]
sales = [30, 35, 20, 25, 30, 40, 30, 25, 35, 25]
development = [25, 30, 25, 35, 40, 25, 20, 20, 25, 40]
hr = [10, 5, 10, 15, 15, 10, 15, 10, 15, 15]
finance = [15, 5, 15, 10, 5, 5, 10, 15, 10, 10]

# Stack data
data = np.array([marketing, sales, development, hr, finance])
data_cum = data.cumsum(axis=0)

# Color codes
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.75

# Create vertical stacked bar chart
for i, (colname, color) in enumerate(zip(['Marketing', 'Sales', 'Development', 'HR', 'Finance'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_xlabel('Company')
ax.set_title('Distribution of Focus Areas in Various Departments')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()