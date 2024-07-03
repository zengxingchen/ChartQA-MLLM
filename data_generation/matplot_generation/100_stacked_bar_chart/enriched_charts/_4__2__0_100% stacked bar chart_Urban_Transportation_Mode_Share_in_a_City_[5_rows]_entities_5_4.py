
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
urban_population = [40, 42, 45, 47, 50, 52, 54, 55, 58, 60, 62, 63, 65, 66, 68, 69, 70, 72, 73, 75, 77, 78, 80, 82]
rural_population = [30, 28, 27, 26, 24, 23, 22, 21, 20, 18, 17, 16, 15, 14, 13, 12, 12, 11, 10, 9, 8, 7, 6, 5]
suburban_population = [30, 30, 28, 27, 26, 25, 24, 24, 22, 22, 21, 21, 20, 20, 19, 19, 18, 17, 17, 16, 15, 15, 14, 13]

# Width and height of the chart
fig, ax = plt.subplots(figsize=(12, 9))

# Stacked bar chart
bar_width = 0.7
r = np.arange(len(years))

p1 = plt.bar(r, urban_population, color='#FF6347', edgecolor='white', width=bar_width)
p2 = plt.bar(r, rural_population, bottom=urban_population, color='#4682B4', edgecolor='white', width=bar_width)
p3 = plt.bar(r, suburban_population, bottom=np.array(urban_population) + np.array(rural_population), color='#32CD32', edgecolor='white', width=bar_width)

# Customizing the axes and title
plt.ylabel('Population Percentage')
plt.xlabel('Year')
plt.title('Population Distribution Over Years', loc='center')
plt.xticks(r, years, rotation=90)
plt.legend(['Urban Population', 'Rural Population', 'Suburban Population'], loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.tight_layout()
plt.show()