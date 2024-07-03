
import matplotlib.pyplot as plt

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024]
happiness_index = [5.4, 5.6, 5.7, 5.9, 6.0, 6.2, 6.3, 6.5, 6.8, 6.9, 
                   7.0, 7.2, 7.4, 7.5, 7.7, 7.9, 8.0, 8.2, 8.4, 8.5, 
                   8.7, 8.9, 9.0, 9.2, 9.3]

plt.figure(figsize=(14, 8))
plt.fill_between(years, happiness_index, color='#4682B4', alpha=0.7)

plt.title('Global Happiness Index Over Time', fontsize=18, pad=25)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Happiness Index', fontsize=15)

plt.annotate('Notable Increase', xy=(2012, 7.4), xytext=(2015, 6.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=13)

plt.show()