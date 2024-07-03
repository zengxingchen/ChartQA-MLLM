
import matplotlib.pyplot as plt

# Data
categories = ['Classical Music', 'Pop Music', 'Jazz', 'Rock', 'Hip Hop', 'Country', 'EDM', 'Opera', 'Reggae', 'Blues']
age_0_14 = [5, 20, 10, 15, 25, 30, 35, 3, 18, 10]
age_15_64 = [45, 60, 50, 55, 60, 55, 50, 47, 62, 55]
age_65_plus = [50, 20, 40, 30, 15, 15, 15, 50, 20, 35]

# Normalize the data to sum up to 100%
totals = [i+j+k for i, j, k in zip(age_0_14, age_15_64, age_65_plus)]
age_0_14 = [i / j * 100 for i, j in zip(age_0_14, totals)]
age_15_64 = [i / j * 100 for i, j in zip(age_15_64, totals)]
age_65_plus = [i / j * 100 for i, j in zip(age_65_plus, totals)]

# Plotting
fig, ax = plt.subplots(figsize=(8, 12))  # Change width and height of the chart

bar_height = 0.7  # change bar width
index = range(len(categories))

p1 = plt.bar(index, age_0_14, bar_height, color='#74C476', edgecolor='white')
p2 = plt.bar(index, age_15_64, bar_height, bottom=age_0_14, color='#31A354', edgecolor='white')
p3 = plt.bar(index, age_65_plus, bar_height, bottom=[i + j for i, j in zip(age_0_14, age_15_64)], color='#006D2C', edgecolor='white')

plt.ylabel('Percentage')
plt.title('Age Distribution by Music Genre')
plt.xticks(index, categories, rotation=45, ha='right')
plt.yticks([0, 25, 50, 75, 100])
plt.legend((p1[0], p2[0], p3[0]), ('Age 0-14', 'Age 15-64', 'Age 65+'))

# Remove the x-axis line
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()