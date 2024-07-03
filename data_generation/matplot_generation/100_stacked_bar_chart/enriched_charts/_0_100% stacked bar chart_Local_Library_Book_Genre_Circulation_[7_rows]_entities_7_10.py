
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019']
windows = [88.0, 86.7, 85.4, 84.2, 83.0]
macos = [7.5, 7.8, 8.3, 8.9, 9.4]
linux = [2.0, 2.4, 2.7, 3.1, 3.6]
others = [2.5, 3.1, 3.6, 3.8, 4.0]

# Colors
colors_windows = '#1f77b4'
colors_macos = '#ff7f0e'
colors_linux = '#2ca02c'
colors_others = '#d62728'

# Stacking data
bars_windows = plt.barh(years, windows, color=colors_windows, edgecolor='white')
bars_macos = plt.barh(years, macos, left=windows, color=colors_macos, edgecolor='white')
bars_linux = plt.barh(years, linux, left=[i+j for i,j in zip(windows, macos)], color=colors_linux, edgecolor='white')
bars_others = plt.barh(years, others, left=[i+j+k for i,j,k in zip(windows, macos, linux)], color=colors_others, edgecolor='white')

# Customizing the plot
plt.xlabel('Market Share (%)')
plt.title('Operating System Market Share Over Years')
plt.yticks(years)
plt.xticks(range(0, 101, 10))
plt.xlim(0, 100)
plt.tight_layout()

# Adjusting size of the chart
fig = plt.gcf()
fig.set_size_inches(8, 5)  # width: 8, height: 5

# Show the figure
plt.show()