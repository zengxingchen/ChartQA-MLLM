
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024]
population = [10, 12, 15, 20, 25, 30, 35, 40, 50, 60, 
              70, 80, 90, 100, 110, 115, 120, 125, 130, 140, 
              150, 155, 160, 165, 170]

plt.figure(figsize=(14, 7))

# Area chart
plt.fill_between(years, population, color='#1E90FF', alpha=0.7)

# Headline and labels
plt.title('Population Growth Over the Years', fontsize=18, pad=25)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population (in millions)', fontsize=15)

# Annotations
plt.annotate('Rapid Growth Period', xy=(2013, 100), xytext=(2010, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Show plot
plt.show()