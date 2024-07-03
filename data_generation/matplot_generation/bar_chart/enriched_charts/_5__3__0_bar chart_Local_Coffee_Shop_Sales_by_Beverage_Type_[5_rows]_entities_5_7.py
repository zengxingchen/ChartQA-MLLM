
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024
]
life_expectancy = [
    70.5, 70.8, 71.0, 71.3, 71.6,
    71.9, 72.2, 72.5, 72.8, 73.1,
    73.4, 73.6, 73.9, 74.2
]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, life_expectancy, height=0.4, color=[
    '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728',
    '#9467BD', '#8C564B', '#E377C2', '#7F7F7F',
    '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78',
    '#98DF8A', '#FF9896'
])

# Set y-axis limits to truncate the chart
plt.xlim(70, 75)

# Axes labels and title
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Year')
plt.title('Average Life Expectancy (2011-2024)')

# Show the plot
plt.show()