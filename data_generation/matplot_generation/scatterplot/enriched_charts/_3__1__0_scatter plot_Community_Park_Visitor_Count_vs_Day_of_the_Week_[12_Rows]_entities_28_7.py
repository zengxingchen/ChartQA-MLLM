
import matplotlib.pyplot as plt

# Data
genres = [
    "Rock", "Jazz", "Pop", "Classical", "Hip-Hop", "Country", 
    "Electronic", "R&B", "Reggae", "Blues", "Metal", "Folk", 
    "Punk", "Soul", "Latin"
]
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 1965, 1975, 1985, 1995, 2005, 2015, 2025]
revenues = [300, 500, 700, 200, 900, 400, 800, 600, 350, 450, 650, 550, 750, 850, 950]

# Scatter plot
fig, ax = plt.subplots(figsize=(16, 10))  # Change the width and height of the chart
scatter = ax.scatter(
    years,
    revenues,
    alpha=0.8,
    c=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#ff6347', '#4682b4', '#ffa07a', '#20b2aa', '#8470ff'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Music Genres: Year Introduced vs Revenue', pad=20)
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Revenue (in millions)')

# Adding the genre names as labels next to each point
for i, genre in enumerate(genres):
    ax.annotate(genre, (years[i], revenues[i]), fontsize=8, ha='right')

plt.show()