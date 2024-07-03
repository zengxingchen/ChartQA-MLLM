
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
]
total_gdp_growth = [
    15.1, 15.8, 16.5, 17.0, 17.5, 18.2,
    18.9, 19.6, 20.3, 21.0, 22.0, 23.1,
    24.3, 25.6, 27.0
]

# Changing figure size
plt.figure(figsize=(14, 8))

# Plotting - horizontal bar chart
bar_width = 0.8
plt.barh(years, total_gdp_growth, color=[
    '#4B0082', '#8A2BE2', '#A52A2A', '#5F9EA0', '#D2691E',
    '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B',
    '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC'
], height=bar_width)

# Customize chart
plt.ylabel('Year', fontsize=14)
plt.xlabel('Total GDP Growth (Trillion USD)', fontsize=14)
plt.title('Total GDP Growth Over the Years', fontsize=16, pad=20)

# Resize bar width
plt.yticks(years, [str(year) for year in years], fontsize=10)

# Show plot
plt.show()