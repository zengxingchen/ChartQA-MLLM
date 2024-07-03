import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
opera = [25, 30, 35, 40, 45, 50, 55, 60]
ballet = [20, 25, 30, 35, 25, 20, 15, 10]
symphony = [35, 30, 25, 20, 20, 15, 20, 25]
theater = [20, 15, 10, 5, 10, 15, 10, 5]

# Convert to percentages
total = np.array(opera) + np.array(ballet) + np.array(symphony) + np.array(theater)
opera = np.array(opera) / total * 100
ballet = np.array(ballet) / total * 100
symphony = np.array(symphony) / total * 100
theater = np.array(theater) / total * 100

# Stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
bars1 = plt.barh(years, opera, color='#FF9999', edgecolor='white', height=bar_width)
bars2 = plt.barh(years, ballet, left=opera, color='#66B3FF', edgecolor='white', height=bar_width)
bars3 = plt.barh(years, symphony, left=opera+ballet, color='#99FF99', edgecolor='white', height=bar_width)
bars4 = plt.barh(years, theater, left=opera+ballet+symphony, color='#FFCC99', edgecolor='white', height=bar_width)

plt.xlabel('Percentage')
plt.ylabel('Year')
plt.title('Performing Arts Attendance by Year')
plt.legend(['Opera', 'Ballet', 'Symphony', 'Theater'], loc='upper left')

plt.show()