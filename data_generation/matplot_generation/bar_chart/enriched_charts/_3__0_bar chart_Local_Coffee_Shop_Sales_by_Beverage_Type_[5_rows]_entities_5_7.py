
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024
]
population = [
    7.03, 7.1, 7.18, 7.26, 7.34,
    7.42, 7.5, 7.58, 7.66, 7.74,
    7.82, 7.9, 7.98, 8.06
]

# Plot configuration
plt.figure(figsize=(10, 12))
bars = plt.bar(years, population, width=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8',
    '#A833FF', '#33FFA8', '#FF8C33', '#3380FF',
    '#FF33D6', '#D633FF', '#33FF8C', '#FF3333',
    '#33FFD6', '#FF33FF'
])

# Axes labels and title
plt.ylabel('Population (millions)')
plt.xlabel('Year')
plt.title('World Population Growth by Year (2011-2024)')

# Show the plot
plt.show()