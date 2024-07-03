
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025,
    2026, 2027, 2028, 2029, 2030
]
new_books_published = [
    100, 120, 140, 180, 160,
    220, 250, 270, 310, 290,
    330, 360, 400, 420, 450,
    480, 500, 530, 550, 600
]

# Plot configuration
plt.figure(figsize=(10, 14))
bars = plt.bar(years, new_books_published, width=0.5, color=[
    '#4CAF50', '#FFC107', '#F44336', '#2196F3',
    '#9C27B0', '#FF9800', '#8BC34A', '#E91E63',
    '#3F51B5', '#FFEB3B', '#607D8B', '#CDDC39',
    '#00BCD4', '#FF5722', '#673AB7', '#03A9F4',
    '#795548', '#009688', '#FF5252', '#3F51B5'
])

# Axes labels and title
plt.ylabel('Number of New Books Published')
plt.xlabel('Year')
plt.title('Annual Number of New Books Published (2011-2030)', pad=20)

# Set y-axis limits to truncate the chart
plt.ylim(90, 620)

# Show the plot
plt.show()