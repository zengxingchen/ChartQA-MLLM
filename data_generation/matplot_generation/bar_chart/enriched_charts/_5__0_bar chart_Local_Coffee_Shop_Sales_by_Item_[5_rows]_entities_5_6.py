
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2010, 2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020, 2021,
    2022, 2023
]
space_missions = [
    50, 55, 60, 70, 90, 100,
    110, 130, 145, 150, 165, 170,
    185, 200
]

# Changing figure size
plt.figure(figsize=(12, 9))

# Plotting - vertical bar chart
bar_width = 0.5
plt.bar(years, space_missions, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1a55FF', '#e41a1c', '#377eb8', '#4daf4a'
], width=bar_width)

# Customize chart
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Space Missions', fontsize=14)
plt.title('Number of Space Missions Over the Years', fontsize=16, pad=20)

# Set y-axis limits
plt.ylim(40, 210)

# Resize bar width
plt.xticks(years, [str(year) for year in years], fontsize=10)

# Show plot
plt.show()