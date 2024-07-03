import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
italian = [30, 35, 40, 45, 50, 55, 60, 65]
chinese = [25, 20, 15, 10, 10, 15, 20, 25]
mexican = [20, 25, 30, 35, 30, 25, 20, 15]
indian = [25, 20, 15, 10, 10, 5, 0, 5]

# Convert to percentages
total = np.array(italian) + np.array(chinese) + np.array(mexican) + np.array(indian)
italian = np.array(italian) / total * 100
chinese = np.array(chinese) / total * 100
mexican = np.array(mexican) / total * 100
indian = np.array(indian) / total * 100

# Stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.4
bars1 = plt.bar(years, italian, color='#FF5733', edgecolor='white', width=bar_width)
bars2 = plt.bar(years, chinese, bottom=italian, color='#33FF57', edgecolor='white', width=bar_width)
bars3 = plt.bar(years, mexican, bottom=italian+chinese, color='#3357FF', edgecolor='white', width=bar_width)
bars4 = plt.bar(years, indian, bottom=italian+chinese+mexican, color='#FF33A1', edgecolor='white', width=bar_width)

plt.ylabel('Percentage')
plt.xlabel('Year')
plt.title('Popularity of International Cuisines Over Years')
plt.legend(['Italian', 'Chinese', 'Mexican', 'Indian'], loc='upper right')

plt.show()