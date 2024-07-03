
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
fiction = [45.2, 46.3, 47.5, 48.6, 49.2, 50.1, 51.3, 52.0, 53.1]
non_fiction = [35.1, 34.5, 33.9, 33.2, 32.7, 32.0, 31.3, 30.7, 30.0]
science = [10.3, 10.5, 10.7, 11.0, 11.2, 11.4, 11.6, 11.8, 12.0]
biography = [4.7, 4.8, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6]
others = [4.7, 3.9, 2.9, 2.1, 1.7, 1.2, 0.4, 0.0, 0.0]

# Colors
colors_fiction = '#4c72b0'
colors_non_fiction = '#55a868'
colors_science = '#c44e52'
colors_biography = '#8172b3'
colors_others = '#ccb974'

# Stacking data
bars_fiction = plt.bar(years, fiction, color=colors_fiction, edgecolor='white', width=0.6)
bars_non_fiction = plt.bar(years, non_fiction, bottom=fiction, color=colors_non_fiction, edgecolor='white', width=0.6)
bars_science = plt.bar(years, science, bottom=[i+j for i,j in zip(fiction, non_fiction)], color=colors_science, edgecolor='white', width=0.6)
bars_biography = plt.bar(years, biography, bottom=[i+j+k for i,j,k in zip(fiction, non_fiction, science)], color=colors_biography, edgecolor='white', width=0.6)
bars_others = plt.bar(years, others, bottom=[i+j+k+l for i,j,k,l in zip(fiction, non_fiction, science, biography)], color=colors_others, edgecolor='white', width=0.6)

# Customizing the plot
plt.ylabel('Market Share (%)')
plt.title('Book Genre Market Share Over Years')
plt.xticks(years, rotation=45)
plt.yticks(range(0, 101, 10))
plt.ylim(0, 100)
plt.tight_layout()

# Adjusting size of the chart
fig = plt.gcf()
fig.set_size_inches(10, 6)

# Show the figure
plt.show()