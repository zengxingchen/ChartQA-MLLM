
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Science Fiction', 'Fantasy', 'Mystery', 'Non-Fiction']
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
data = [
    [25, 35, 20, 20],
    [30, 25, 30, 15],
    [20, 30, 25, 25],
    [35, 25, 20, 20],
    [40, 20, 25, 15],
    [25, 30, 20, 25],
    [30, 25, 25, 20],
    [20, 35, 25, 20],
    [35, 20, 30, 15],
    [30, 25, 20, 25],
    [25, 30, 25, 20],
]

# Convert data to numpy array for easier manipulation
data = np.array(data)
data_cumsum = data.cumsum(axis=1)
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF']

fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the data
for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[:, i]
    starts = data_cumsum[:, i] - widths
    ax.barh(years, widths, left=starts, height=0.7, label=colname, color=color)

ax.set_title('Book Genre Popularity Over Time')
ax.legend(ncol=len(categories), bbox_to_anchor=(0.5, -0.1), loc='center', fontsize='small')
plt.xlabel('Percentage')
plt.ylabel('Year')
plt.show()