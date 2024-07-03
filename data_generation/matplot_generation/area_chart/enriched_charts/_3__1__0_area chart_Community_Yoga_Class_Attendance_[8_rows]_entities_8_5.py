
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
             2020, 2021, 2022, 2023],
    'Discoveries': [5, 8, 12, 15, 19, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 
                    95, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['Discoveries'], color='#4CAF50', alpha=0.6)
plt.plot(df['Year'], df['Discoveries'], color='#FF5733', alpha=0.8)

plt.title('Number of Significant Archaeological Discoveries Each Year', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Discoveries', fontsize=14)
plt.annotate('Significant discovery in 2000', xy=(2000, 35), xytext=(2000, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()