
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
             2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
             2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Electric_Car_Sales': [500, 600, 750, 800, 950, 1100, 1300, 1500, 1700, 1900, 
                           2100, 2300, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 
                           6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 
                           11000, 12000, 13000, 14000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Year'], df['Electric_Car_Sales'], color='#32CD32', alpha=0.7)
plt.plot(df['Year'], df['Electric_Car_Sales'], color='#FF4500', alpha=0.9)

plt.title('Annual Electric Car Sales (1992-2023)', fontsize=18)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Electric Car Sales', fontsize=15)
plt.annotate('Rapid growth in recent years', xy=(2018, 9500), xytext=(2010, 11000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()