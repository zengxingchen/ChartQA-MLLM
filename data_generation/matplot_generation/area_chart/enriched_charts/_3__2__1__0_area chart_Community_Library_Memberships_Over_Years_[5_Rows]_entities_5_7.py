
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
             2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,
             2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040],
    'Revenue': [450, 480, 510, 530, 600, 640, 700, 750, 800, 850,
                900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
                1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700,
                2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700,
                3800]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Year'], df['Revenue'], color='#1f77b4', alpha=0.6)
plt.plot(df['Year'], df['Revenue'], color='#ff7f0e', alpha=0.8)

plt.title('Revenue Growth Over the Years (2000-2040)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in millions)', fontsize=14)

for i in range(len(df)):
    plt.text(df['Year'][i], df['Revenue'][i] + 50, str(df['Revenue'][i]), ha='center', va='bottom')

plt.grid(True)
plt.show()