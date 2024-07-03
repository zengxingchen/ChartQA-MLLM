
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
             2021, 2022, 2023, 2024, 2025],
    'Population': [1200, 1250, 1300, 1400, 1550, 1600, 1700, 1800, 1900, 2000,
                   2100, 2200, 2300, 2400, 2550, 2650, 2750, 2900, 3050, 3200,
                   3350, 3450, 3600, 3750, 3900, 4050]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Year'], df['Population'], color='#2ca02c', alpha=0.6)
plt.plot(df['Year'], df['Population'], color='#d62728', alpha=0.8)

plt.title('Population Growth Over the Years (2000-2025)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (in thousands)', fontsize=12)

for i in range(len(df)):
    plt.text(df['Year'][i], df['Population'][i] + 50, str(df['Population'][i]), ha='center', va='bottom')

plt.grid(True)
plt.show()