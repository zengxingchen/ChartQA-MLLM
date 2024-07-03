
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [1992, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
             2018, 2019, 2020, 2021, 2022, 2023],
    'Exoplanets_Discovered': [2, 3, 6, 8, 12, 18, 21, 34, 54, 78, 107, 123, 148, 176, 
                              202, 231, 258, 290, 321, 357, 403, 457, 505, 570, 620, 
                              677, 739, 803, 870, 940]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Year'], df['Exoplanets_Discovered'], color='#1f77b4', alpha=0.6)
plt.plot(df['Year'], df['Exoplanets_Discovered'], color='#ff7f0e', alpha=0.8)

plt.title('Number of Exoplanets Discovered Each Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Exoplanets Discovered', fontsize=14)
plt.annotate('First exoplanet discovery', xy=(1992, 2), xytext=(1992, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()