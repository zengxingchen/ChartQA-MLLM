
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024
]
stars = [
    100, 110, 120, 130, 140, 
    150, 160, 170, 180, 190, 
    200, 210, 220, 230, 240
]
milky_way = [
    50, 55, 60, 65, 70, 
    75, 80, 85, 90, 95, 
    100, 105, 110, 115, 120
]
constellations = [
    40, 42, 44, 46, 48, 
    50, 52, 54, 56, 58, 
    60, 62, 64, 66, 68
]
space_exploration = [
    30, 32, 34, 36, 38, 
    40, 42, 44, 46, 48, 
    50, 52, 54, 56, 58
]

# Configuration for the figure size
plt.figure(figsize=(14, 8))

# Stacked bar chart
bar_width = 0.6
plt.bar(years, stars, width=bar_width, color='#1e90ff', edgecolor='white', label='Stars')
plt.bar(years, milky_way, width=bar_width, bottom=stars, color='#32cd32', edgecolor='white', label='Milky Way')
plt.bar(years, constellations, width=bar_width, bottom=[i+j for i,j in zip(stars, milky_way)], color='#ff8c00', edgecolor='white', label='Constellations')
plt.bar(years, space_exploration, width=bar_width, bottom=[i+j+k for i,j,k in zip(stars, milky_way, constellations)], color='#ff1493', edgecolor='white', label='Space Exploration')

# Adding labels and title
plt.ylabel('Investment (in millions)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.title('Annual Investment in Astronomy & Space Exploration from 2010 to 2024', fontsize=16, pad=20)

# Show legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Adding numerical labels
for year, star, milky, const, space in zip(years, stars, milky_way, constellations, space_exploration):
    plt.text(year, star / 2, str(star), ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    plt.text(year, star + milky / 2, str(milky), ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    plt.text(year, star + milky + const / 2, str(const), ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    plt.text(year, star + milky + const + space / 2, str(space), ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Display the chart
plt.show()