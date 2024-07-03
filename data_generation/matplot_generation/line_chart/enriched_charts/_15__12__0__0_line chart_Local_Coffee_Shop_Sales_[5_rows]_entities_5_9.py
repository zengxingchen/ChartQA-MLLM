
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023
]
enrolment = [
    1000, 1050, 1100, 1150, 1200, 1250,
    1300, 1350, 1400, 1450, 1500, 1550,
    1600, 1650, 1700, 1750, 1800, 1850,
    1900, 1950, 2000, 2050, 2100, 2150
]

plt.figure(figsize=(16, 10))
plt.plot(years, enrolment, marker='o', color="#1E90FF")

for year, enrl in zip(years, enrolment):
    plt.text(year, enrl + 20, f'{enrl}', ha='center', color='#FF1493')

plt.gca().invert_yaxis()
plt.title("Annual Student Enrolment Over the Years", pad=20)
plt.xlabel("Year")
plt.ylabel("Enrolment (number of students)")

plt.tight_layout()
plt.show()