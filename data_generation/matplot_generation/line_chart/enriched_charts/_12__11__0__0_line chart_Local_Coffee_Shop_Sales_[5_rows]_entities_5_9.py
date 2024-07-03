
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022
]
attendance = [
    50, 52, 49, 53, 55, 58,
    57, 60, 62, 65, 64, 66,
    68, 70, 69, 71, 72, 74,
    75, 77, 80, 78, 81
]

plt.figure(figsize=(16, 12))
plt.plot(years, attendance, marker='o', color="#1E90FF")

for year, att in zip(years, attendance):
    plt.text(year, att + 1, f'{att}K', ha='center', color='#DC143C')

plt.title("Annual Attendance at Music Festival", pad=20, loc='left')
plt.xlabel("Year")
plt.ylabel("Attendance (in thousands)")

plt.tight_layout()
plt.show()