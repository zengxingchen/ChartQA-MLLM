
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
libraries_visited = [
    50, 65, 78, 85, 92,
    110, 123, 140, 158, 170,
    180, 200
]

# Plot configuration
plt.figure(figsize=(12, 10))
bars = plt.bar(years, libraries_visited, width=0.6, color=[
    '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728',
    '#9467BD', '#8C564B', '#E377C2', '#7F7F7F',
    '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78'
])

# Axes labels and title
plt.ylabel('Number of Public Libraries Visited')
plt.xlabel('Year')
plt.title('Annual Public Libraries Visits (2011-2022)')

# Show the plot
plt.show()