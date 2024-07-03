import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
books_sold = [
    500, 620, 790, 850, 900,
    1020, 1100, 1250, 1400, 1600,
    1750, 1950
]

# Plot configuration
plt.figure(figsize=(10, 12))
bars = plt.bar(years, books_sold, width=0.4, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#FFBD33', '#33FFBD', '#A133FF', '#FF33B8',
    '#FF8C33', '#33FF8C', '#5733FF', '#FF3333'
])

# Axes labels and title
plt.ylabel('Number of Books Sold')
plt.xlabel('Year')
plt.title('Annual Book Sales (2011-2022)', pad=20)

# Show the plot
plt.show()