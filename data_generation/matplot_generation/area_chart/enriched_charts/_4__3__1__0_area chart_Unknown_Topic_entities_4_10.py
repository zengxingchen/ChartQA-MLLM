
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024]
smart_homes = [5, 7, 9, 12, 16, 20, 25, 30, 35, 42, 
               50, 60, 70, 85, 100, 120, 140, 160, 185, 210, 
               240, 270, 300, 330, 360]

plt.figure(figsize=(16, 8))

# Area chart
plt.fill_between(years, smart_homes, color='#32CD32', alpha=0.8)

# Headline and labels
plt.title('Growth of Smart Homes Over the Years', fontsize=20, pad=30, loc='left')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Smart Homes (in thousands)', fontsize=16)

# Annotations
plt.annotate('Significant Increase', xy=(2014, 100), xytext=(2010, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=14)

# Show plot
plt.show()