
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024]
values = [15, 18, 20, 22, 30, 35, 45, 40, 50, 55, 
          65, 70, 80, 75, 85, 90, 95, 100, 110, 105, 
          115, 120, 125, 130, 135]

plt.figure(figsize=(12, 6))

# Area chart
plt.fill_between(years, values, color='#FF6347', alpha=0.7)

# Headline and labels
plt.title('Advancements in Renewable Energy Capacity Over Time', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Capacity (GW)', fontsize=14)

# Annotations
plt.annotate('Significant Increase', xy=(2010, 65), xytext=(2012, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Show plot
plt.show()