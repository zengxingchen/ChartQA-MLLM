
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021
]
life_expectancy = [
    66.8, 67.1, 67.3, 67.6, 68.0, 68.4,
    68.7, 69.0, 69.3, 69.7, 70.1, 70.4,
    70.8, 71.1, 71.4, 71.7, 72.0, 72.3,
    72.6, 72.9, 73.2, 73.5
]

# Changing figure size
plt.figure(figsize=(10, 12))

# Plotting - vertical bar chart
bar_width = 0.5
plt.bar(years, life_expectancy, color=[
    '#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f',
    '#edc949', '#af7aa1', '#ff9da7', '#9c755f', '#bab0ab',
    '#6b6ecf', '#b07aa1', '#f28e2b', '#ff9da7', '#4e79a7',
    '#e15759', '#59a14f', '#76b7b2', '#af7aa1', '#edc949',
    '#6b6ecf', '#bab0ab'
], width=bar_width)

# Customize chart
plt.xlabel('Year', fontsize=14)
plt.ylabel('Life Expectancy (Years)', fontsize=14)
plt.title('Global Life Expectancy Over the Years', fontsize=16, pad=20)

# Resize bar width
plt.xticks(years, [str(year) for year in years], fontsize=10, rotation=45)

# Show plot
plt.show()