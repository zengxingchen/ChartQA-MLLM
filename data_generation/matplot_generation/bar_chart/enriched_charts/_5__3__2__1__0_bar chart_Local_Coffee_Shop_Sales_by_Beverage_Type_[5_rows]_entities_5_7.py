
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025,
    2026, 2027, 2028, 2029, 2030
]
courses = [
    5, 8, 11, 18, 14,
    22, 24, 29, 33, 32,
    38, 45, 49, 55, 58,
    64, 68, 72, 77, 83
]

# Plot configuration
plt.figure(figsize=(12, 8))
bars = plt.barh(years, courses, height=0.5, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#ff9896', '#c5b0d5',
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d',
    '#9edae5', '#ffbb78', '#98df8a', '#ff9896'
])

# Axes labels and title
plt.xlabel('Number of Courses')
plt.ylabel('Year')
plt.title('Annual Number of Online Courses Offered (2011-2030)', pad=20)
plt.xlim(0, 90)  # Truncated y-axis

# Show the plot
plt.show()