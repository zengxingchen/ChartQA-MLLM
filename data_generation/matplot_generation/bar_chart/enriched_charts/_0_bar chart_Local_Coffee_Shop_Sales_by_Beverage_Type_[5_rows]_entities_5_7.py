
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
sales = [
    100, 150, 200, 300, 400,
    550, 750, 950, 1200, 1500,
    1800, 2200
]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, sales, height=0.5, color=[
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9',
    '#92A8D1', '#955251', '#B565A7', '#009B77',
    '#DD4124', '#D65076', '#45B8AC', '#EFC050',
])

# Axes labels and title
plt.xlabel('Number of Electric Vehicles Sold')
plt.ylabel('Year')
plt.title('Electric Vehicle Sales by Year (2011-2022)')

# Show the plot
plt.show()