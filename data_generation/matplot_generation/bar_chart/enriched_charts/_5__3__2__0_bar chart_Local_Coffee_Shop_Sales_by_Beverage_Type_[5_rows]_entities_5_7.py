
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025,
    2026, 2027, 2028, 2029, 2030
]
calories_burned = [
    2200, 2300, 2400, 2500, 2600,
    2700, 2800, 2900, 3000, 3100,
    3200, 3300, 3400, 3500, 3600,
    3700, 3800, 3900, 4000, 4100
]

# Plot configuration
plt.figure(figsize=(10, 14))
bars = plt.bar(years, calories_burned, width=0.5, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#FFBD33', '#33FFBD', '#A133FF', '#FF33B8',
    '#FF8C33', '#33FF8C', '#5733FF', '#FF3333',
    '#FF5733', '#33FF57', '#3357FF', '#FF3399',
    '#FF9933', '#33FF99', '#3399FF', '#FF6699'
])

# Axes labels and title
plt.ylabel('Calories Burned')
plt.xlabel('Year')
plt.title('Annual Calorie Burn (2011-2030)', pad=20)

# Y-axis limit to truncate the chart
plt.ylim(2000, 4200)

# Show the plot
plt.show()