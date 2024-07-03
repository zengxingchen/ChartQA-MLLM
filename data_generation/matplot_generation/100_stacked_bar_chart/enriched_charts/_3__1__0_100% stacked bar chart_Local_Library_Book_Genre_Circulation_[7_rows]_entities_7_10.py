
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2018', '2019', '2020', '2021', '2022', '2023']
math = [25, 20, 30, 35, 25, 30]
science = [35, 30, 25, 20, 30, 25]
english = [15, 25, 20, 25, 30, 20]
history = [25, 25, 25, 20, 15, 25]

# Stack data
data = np.array([math, science, english, history])
data_cum = data.cumsum(axis=0)

# Category names
categories = ['Math', 'Science', 'English', 'History']
category_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.5

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(years, widths, left=starts, height=bar_width, label=colname, color=color)

# Add labels and title
ax.set_xlabel('Percentage')
ax.set_title('Student Performance in Different Subjects Over Years', pad=20)
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 1.05))

plt.tight_layout()
plt.show()