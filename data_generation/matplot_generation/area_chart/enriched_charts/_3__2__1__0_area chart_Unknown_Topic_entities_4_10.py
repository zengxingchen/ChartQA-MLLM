
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
values = [150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 
          350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 
          550, 570, 590, 610, 630, 650, 670, 690, 710, 730, 750]

plt.figure(figsize=(16, 8))

# Area chart
plt.fill_between(years, values, color='#FF6347', alpha=0.7)

# Headline and labels
plt.title('Company Revenue Growth Over Time', fontsize=18, pad=25)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in Millions)', fontsize=14)

# Annotations
plt.annotate('Significant Growth', xy=(2018, 510), xytext=(2015, 450),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Show plot
plt.show()