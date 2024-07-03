
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
             2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
             2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Discoveries_Made': [5, 8, 12, 15, 18, 20, 24, 28, 32, 37, 42, 48, 
                         55, 63, 70, 78, 85, 92, 100, 110, 120, 130, 145, 160, 
                         175, 190, 205, 225, 240, 255, 275, 290]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Year'], df['Discoveries_Made'], color='#FF6347', alpha=0.7)
plt.plot(df['Year'], df['Discoveries_Made'], color='#4682B4', alpha=0.9)

plt.title('Number of Astronomical Discoveries Each Year', fontsize=18, loc='center')
plt.xlabel('Year', fontsize=15)
plt.ylabel('Discoveries Made', fontsize=15)
plt.annotate('Significant rise in discoveries', xy=(2015, 160), xytext=(2015, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()