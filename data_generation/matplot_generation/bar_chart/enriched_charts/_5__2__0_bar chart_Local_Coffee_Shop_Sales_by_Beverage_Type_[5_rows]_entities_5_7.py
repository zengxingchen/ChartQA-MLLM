
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
tickets_sold = [
    1500, 1620, 1790, 1850, 1900,
    2020, 2100, 2250, 2400, 2600,
    2750, 2950
]

# Plot configuration
plt.figure(figsize=(12, 8))
bars = plt.barh(years, tickets_sold, height=0.5, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#FFBD33', '#33FFBD', '#A133FF', '#FF33B8',
    '#FF8C33', '#33FF8C', '#5733FF', '#FF3333'
])

# Axes labels and title
plt.xlabel('Number of Concert Tickets Sold')
plt.ylabel('Year')
plt.title('Annual Concert Ticket Sales (2011-2022)', pad=20)

# Set y-axis limit
plt.xlim(1400, 3000)

# Show the plot
plt.show()