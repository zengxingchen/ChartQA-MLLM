import matplotlib.pyplot as plt
import numpy as np

categories = ['Urban', 'Suburban', 'Rural']
years = ['1990', '2000', '2010', '2020']
data = np.array([
    [45, 50, 55, 60],  # Urban
    [35, 30, 25, 20],  # Suburban
    [20, 20, 20, 20]   # Rural
])

data_cum = data.cumsum(axis=0)
category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig, ax = plt.subplots(figsize=(10, 6))

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(years, widths, left=starts, height=0.8, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Urban, Suburban, and Rural Population Distribution Over Time', pad=20)
ax.legend(loc='upper right')

plt.show()