
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
values = [10, 12, 15, 20, 25, 30, 28, 35, 40, 45, 
          50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 
          100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]

plt.figure(figsize=(14, 7))

# Area chart
plt.fill_between(years, values, color='#4682B4', alpha=0.7)

# Headline and labels
plt.title('Annual Reading Progress: Books Read Over Time', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Books Read', fontsize=14)

# Annotations
plt.annotate('Reading Marathon', xy=(2015, 75), xytext=(2012, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Show plot
plt.show()