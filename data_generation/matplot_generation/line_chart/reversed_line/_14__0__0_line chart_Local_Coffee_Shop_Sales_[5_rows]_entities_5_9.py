
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020
]
pollution_level = [
    55, 53, 58, 52, 49, 47,
    51, 46, 44, 45, 43, 42,
    40, 39, 37, 35, 33, 32,
    30, 28, 25
]

plt.figure(figsize=(14, 10))
plt.plot(years, pollution_level, marker='o', color="#FF6347")

for year, level in zip(years, pollution_level):
    plt.text(year, level + 1, f'{level}', ha='center', color='#2E8B57')

plt.title("Pollution Levels Over the Years", pad=20)
plt.xlabel("Year")
plt.ylabel("Pollution Level")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()