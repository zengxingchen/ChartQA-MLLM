import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023
]
revenue = [
    50, 52, 54, 57, 59, 60,
    63, 65, 67, 70, 68, 71,
    73, 75, 78, 80, 83, 85,
    88, 90, 92, 94, 97, 100
]

plt.figure(figsize=(14, 9))
plt.plot(years, revenue, marker='o', color="#FF6347")

for year, rev in zip(years, revenue):
    plt.text(year, rev + 1, f'{rev}M', ha='center', color='#20B2AA')

plt.title("Annual Revenue Over the Years", pad=20)
plt.xlabel("Year")
plt.ylabel("Revenue (in millions)")

plt.tight_layout()
plt.show()