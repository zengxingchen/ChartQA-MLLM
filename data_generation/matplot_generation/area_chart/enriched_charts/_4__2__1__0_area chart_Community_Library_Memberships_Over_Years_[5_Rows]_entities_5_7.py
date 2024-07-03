
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
             2021, 2022, 2023, 2024, 2025],
    'Visitors': [500, 600, 750, 850, 920, 1000, 1100, 1150, 1200, 1300, 1400,
                 1550, 1700, 1800, 1900, 2100, 2250, 2400, 2600, 2800, 3000,
                 3200, 3400, 3600, 3800, 4000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
plt.fill_between(df['Year'], df['Visitors'], color='#1f77b4', alpha=0.5)
plt.plot(df['Year'], df['Visitors'], color='#ff7f0e', linewidth=2)

plt.title('Visitor Growth to National Parks (2000-2025)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Visitors (in thousands)', fontsize=14)

for i in range(len(df)):
    plt.text(df['Year'][i], df['Visitors'][i] + 50, str(df['Visitors'][i]), ha='center', va='bottom')

plt.grid(True)
plt.show()