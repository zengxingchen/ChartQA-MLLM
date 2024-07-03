
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
attendance = [
    32000, 35000, 37500, 42000, 46000,
    50000, 53000, 56000, 59000, 60000,
    62000, 65000
]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, attendance, height=0.7, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#33FFF6', '#FF8333', '#FF33DA', '#FFBD33',
    '#338BFF', '#33FF83', '#BD33FF', '#57FF33'
])

# Axes labels and title
plt.xlabel('Attendance')
plt.ylabel('Year')
plt.title('Annual Sports Event Attendance (2011-2022)', pad=20)

# Set y-axis limit
plt.xlim(30000, 70000)

# Show the plot
plt.show()