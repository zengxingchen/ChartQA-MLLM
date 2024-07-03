
import matplotlib.pyplot as plt

years = [
    2010, 2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020, 2021,
    2022, 2023, 2024, 2025
]
art_pieces_created = [
    8, 10, 12, 14, 16, 18,
    20, 22, 24, 26, 28, 30,
    32, 34, 36, 38
]

plt.figure(figsize=(14, 10))

bar_width = 0.8
plt.bar(years, art_pieces_created, color=[
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c2f0c2', '#ff6666', '#6666ff', '#e6b3b3',
    '#d9d9d9', '#ffcc99', '#b3b3cc', '#ff99e6', '#c2c2f0',
    '#ff6666'
], width=bar_width)

plt.ylim(5, 40)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Art Pieces Created', fontsize=14)
plt.title('Annual Art Pieces Created Over the Years', fontsize=18)

plt.xticks(years, [str(year) for year in years], fontsize=12)

plt.show()