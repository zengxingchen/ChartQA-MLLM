
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022
]
average_bpm = [
    80, 82, 78, 76, 74, 70,
    68, 72, 75, 77, 79, 74,
    73, 71, 69, 65, 63, 61,
    60, 59, 58, 56, 55
]

plt.figure(figsize=(12, 8))
plt.plot(years, average_bpm, marker='s', color="#20B2AA")

for year, bpm in zip(years, average_bpm):
    plt.text(year, bpm + 1, f'{bpm} bpm', ha='center', color='#DC143C')

plt.title("Annual Average Heart Rate Trend Over Time", pad=20)
plt.xlabel("Year")
plt.ylabel("Average Heart Rate (bpm)")

plt.gca().invert_yaxis()  # Inverting y-axis

plt.tight_layout()
plt.show()