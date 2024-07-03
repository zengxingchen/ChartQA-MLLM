
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021
]
electric_cars = [
    50982, 120000, 225000, 405000, 740000, 1250000,
    2000000, 3120000, 4700000, 7700000, 10000000
]

# Changing figure size
plt.figure(figsize=(14, 8))

# Plotting - horizontal bar chart
bar_width = 0.6
plt.barh(years, electric_cars, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF'
], height=bar_width)

# Customize chart
plt.xlabel('Number of Electric Cars', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Electric Car Adoption Over the Years', fontsize=16)

# Resize bar height
plt.yticks(years, [str(year) for year in years], fontsize=10)

# Show plot
plt.show()