
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021
]
revenue = [
    1.2, 1.5, 1.8, 2.1, 2.3, 2.7,
    3.0, 3.5, 3.8, 4.1, 4.4, 4.6,
    4.9, 5.2, 5.5, 5.7, 6.0, 6.2,
    6.5, 6.8, 7.0, 7.3
]

# Changing figure size
plt.figure(figsize=(12, 8))

# Plotting - horizontal bar chart
bar_height = 0.4
plt.barh(years, revenue, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#9edae5', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#ff9896',
    '#c49c94', '#ffbb78', '#98df8a', '#c5b0d5', '#ffbb78',
    '#aec7e8', '#c7c7c7'
], height=bar_height)

# Customize chart
plt.xlabel('Revenue (in Millions)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Annual Revenue from 2000 to 2021', fontsize=16, pad=20)

# Set y-axis limit to start from a specific value
plt.ylim(1998, 2023)

# Show plot
plt.show()