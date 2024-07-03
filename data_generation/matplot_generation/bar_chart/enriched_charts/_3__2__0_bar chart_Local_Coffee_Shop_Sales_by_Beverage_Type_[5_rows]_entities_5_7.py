
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025
]
calories_consumed = [
    2000, 2150, 2250, 2300, 2450,
    2600, 2750, 2900, 3050, 3150,
    3300, 3450, 3600, 3700, 3850
]

# Plot configuration
plt.figure(figsize=(12, 8))
bars = plt.barh(years, calories_consumed, height=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#FFBD33', '#33FFBD', '#A133FF', '#FF33B8',
    '#FF8C33', '#33FF8C', '#5733FF', '#FF3333',
    '#FF5733', '#33FF57', '#3357FF'
])

# Axes labels and title
plt.xlabel('Calories Consumed')
plt.ylabel('Year')
plt.title('Annual Calorie Consumption (2011-2025)', pad=20)

# Show the plot
plt.show()