
import matplotlib.pyplot as plt

years = ['2016', '2017', '2018', '2019', '2020']
domestic_fiction = [15, 17, 16, 19, 18]
historical_fiction = [18, 20, 21, 23, 22]
mystery = [22, 24, 25, 26, 27]
science_fiction = [20, 22, 21, 24, 25]
romance = [25, 23, 23, 21, 20]

colors = ['#4B0082', '#FF4500', '#32CD32', '#1E90FF', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.7

ax.bar(years, domestic_fiction, color=colors[0], edgecolor='white', width=bar_width, label='Domestic Fiction')
ax.bar(years, historical_fiction, bottom=domestic_fiction, color=colors[1], edgecolor='white', width=bar_width, label='Historical Fiction')
ax.bar(years, mystery, bottom=[i+j for i,j in zip(domestic_fiction, historical_fiction)], color=colors[2], edgecolor='white', width=bar_width, label='Mystery')
ax.bar(years, science_fiction, bottom=[i+j+k for i,j,k in zip(domestic_fiction, historical_fiction, mystery)], color=colors[3], edgecolor='white', width=bar_width, label='Science Fiction')
ax.bar(years, romance, bottom=[i+j+k+l for i,j,k,l in zip(domestic_fiction, historical_fiction, mystery, science_fiction)], color=colors[4], edgecolor='white', width=bar_width, label='Romance')

ax.set_ylabel('Percentage (%)')
ax.set_title('Popular Book Genres by Year (2016-2020)')

ax.legend(loc='upper right')

plt.show()