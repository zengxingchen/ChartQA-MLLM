
import matplotlib.pyplot as plt

# Data
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica']
age_0_14 = [40, 25, 15, 20, 30, 25, 22]
age_15_64 = [55, 65, 60, 60, 60, 63, 68]
age_65_plus = [5, 10, 25, 20, 10, 12, 10]

# Normalize the data to sum up to 100%
totals = [i+j+k for i, j, k in zip(age_0_14, age_15_64, age_65_plus)]
age_0_14 = [i / j * 100 for i, j in zip(age_0_14, totals)]
age_15_64 = [i / j * 100 for i, j in zip(age_15_64, totals)]
age_65_plus = [i / j * 100 for i, j in zip(age_65_plus, totals)]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8)) # Change width and height of the chart

bar_width = 0.5 # change bar width
index = range(len(continents))

p1 = plt.barh(index, age_0_14, bar_width, color='#FFC300', edgecolor='white')
p2 = plt.barh(index, age_15_64, bar_width, left=age_0_14, color='#FF5733', edgecolor='white')
p3 = plt.barh(index, age_65_plus, bar_width, left=[i + j for i, j in zip(age_0_14, age_15_64)], color='#C70039', edgecolor='white')

plt.xlabel('Percentage')
plt.title('Age Distribution by Continent')
plt.yticks(index, continents)
plt.xticks([0, 25, 50, 75, 100])
plt.legend((p1[0], p2[0], p3[0]), ('Age 0-14', 'Age 15-64', 'Age 65+'))

# Remove the y-axis line
ax.spines['left'].set_visible(False)

plt.show()