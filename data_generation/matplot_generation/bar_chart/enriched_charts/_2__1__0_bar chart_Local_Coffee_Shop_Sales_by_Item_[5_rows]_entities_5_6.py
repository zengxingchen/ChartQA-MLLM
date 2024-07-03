
import matplotlib.pyplot as plt

years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023
]
books_read = [
    15, 17, 22, 19, 25, 28,
    35, 30, 40, 50, 55, 60, 65
]

plt.figure(figsize=(12, 8))

bar_height = 0.6
plt.barh(years, books_read, color=[
    '#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
    '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
    '#008080', '#e6beff', '#9a6324'
], height=bar_height)

plt.xlabel('Number of Books Read', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Annual Books Read Over the Years', fontsize=16)

plt.yticks(years, [str(year) for year in years], fontsize=10)

plt.show()