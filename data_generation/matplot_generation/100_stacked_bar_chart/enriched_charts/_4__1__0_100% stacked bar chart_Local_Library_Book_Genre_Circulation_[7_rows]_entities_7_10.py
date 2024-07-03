
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Classical Music', 'Pop Music', 'Rock Music', 'Jazz Music', 'Hip Hop']
years = ['2020', '2021', '2022']
data = np.array([
    [20, 30, 25],  # Classical Music
    [25, 20, 30],  # Pop Music
    [15, 25, 20],  # Rock Music
    [10, 10, 15],  # Jazz Music
    [30, 15, 10]   # Hip Hop
])

# Colors
colors = ['#ff6666', '#66b3ff', '#99ff66', '#ffcc66', '#c266ff']

# Stack data
data_cum = data.cumsum(axis=0)

# Bar chart
fig, ax = plt.subplots(figsize=(8, 12))
bar_width = 0.6

for i in range(len(categories)):
    ax.bar(years, data[i], bottom=data_cum[i] - data[i], width=bar_width, color=colors[i], label=categories[i])

# Add legend and labels
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
ax.set_ylabel('Percentage')
ax.set_xlabel('Years')
ax.set_title('Music Genre Popularity Over Years')

plt.tight_layout()
plt.show()