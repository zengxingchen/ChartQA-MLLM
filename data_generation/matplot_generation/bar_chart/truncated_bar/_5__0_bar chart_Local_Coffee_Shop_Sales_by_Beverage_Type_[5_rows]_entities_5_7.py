
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
books_read = [
    5, 8, 15, 20, 28,
    35, 40, 42, 47, 53,
    60, 65
]

# Plot configuration
plt.figure(figsize=(10, 12))
bars = plt.bar(years, books_read, width=0.4, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
])

# Set y-axis limits
plt.ylim(0, 70)

# Axes labels and title
plt.ylabel('Number of Books Read')
plt.xlabel('Year')
plt.title('Annual Book Reading Trends (2011-2022)')

# Show the plot
plt.show()