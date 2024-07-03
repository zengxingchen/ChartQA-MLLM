
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
]
publication_count = [
    300, 320, 360, 390, 450, 510,
    590, 680, 770, 860, 960, 1050,
    1150, 1260, 1370
]

# Changing figure size
plt.figure(figsize=(14, 8))

# Plotting - horizontal bar chart
bar_height = 0.6
plt.barh(years, publication_count, color=[
    '#4B0082', '#FF4500', '#FFD700', '#00BFFF', '#32CD32',
    '#FF69B4', '#DAA520', '#8B0000', '#00CED1', '#FF6347',
    '#2E8B57', '#D2691E', '#00FF7F', '#4682B4', '#DC143C'
], height=bar_height)

# Customize chart
plt.ylabel('Year', fontsize=14)
plt.xlabel('Number of Publications', fontsize=14)
plt.title('Annual Scientific Publications in Various Fields', fontsize=16)

# Setting y-axis limit to start from 200
plt.xlim(200, 1400)

# Resize bar width
plt.yticks(years, [str(year) for year in years], fontsize=10)

# Show plot
plt.show()