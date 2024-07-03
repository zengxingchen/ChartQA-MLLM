
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025,
    2026, 2027, 2028, 2029, 2030
]
new_science_discoveries = [
    5, 7, 10, 15, 12,
    18, 22, 25, 30, 28,
    35, 40, 45, 50, 55,
    60, 65, 70, 75, 80
]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, new_science_discoveries, height=0.7, color=[
    '#1B998B', '#2D3047', '#FFFD82', '#FF9B71',
    '#E84855', '#34A0A4', '#6A0572', '#FFD166',
    '#EF476F', '#118AB2', '#073B4C', '#06D6A0',
    '#26547C', '#EF476F', '#FFD166', '#06D6A0',
    '#118AB2', '#073B4C', '#E84855', '#FF9B71'
])

# Axes labels and title
plt.xlabel('Number of New Discoveries')
plt.ylabel('Year')
plt.title('Annual New Science Discoveries (2011-2030)', pad=20)

# Show the plot
plt.show()