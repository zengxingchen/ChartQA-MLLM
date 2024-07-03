
import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'China', 'India', 'Germany', 'UK', 'France', 'Japan', 'Australia', 'Brazil', 'Canada']
years = ['2010', '2011', '2012', '2013', '2014']
data = [
    [25, 27, 24, 23, 22],
    [20, 21, 22, 23, 25],
    [15, 14, 15, 16, 17],
    [10, 9, 10, 11, 12],
    [8, 7, 8, 8, 9],
    [6, 6, 7, 6, 7],
    [7, 7, 6, 7, 6],
    [5, 6, 5, 5, 4],
    [4, 3, 3, 4, 5],
    [3, 3, 3, 3, 3]
]

data = np.array(data)
data_percentage = data / data.sum(axis=0) * 100

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FF9633', '#33A1FF', '#A1FF33', '#FF3333']

# Plot
fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.85
bars = np.arange(len(years))

bottoms = np.zeros(len(years))

for i in range(len(countries)):
    ax.barh(bars, data_percentage[i], left=bottoms, color=colors[i], edgecolor='white', height=bar_width)
    bottoms += data_percentage[i]

ax.set_xlabel('Percentage')
ax.set_ylabel('Years')
ax.set_title('Renewable Energy Consumption by Country Over Years')
ax.set_yticks(bars)
ax.set_yticklabels(years)
ax.legend(countries, loc='upper right', bbox_to_anchor=(1.15, 1.0))

plt.show()