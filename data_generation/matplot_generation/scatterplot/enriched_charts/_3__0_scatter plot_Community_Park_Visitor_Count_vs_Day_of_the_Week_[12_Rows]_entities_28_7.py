
import matplotlib.pyplot as plt

# Data
artists = [
    "The Beatles", "Elvis Presley", "Michael Jackson", "Madonna", "Led Zeppelin",
    "Pink Floyd", "Whitney Houston", "Elton John", "Mariah Carey", "Queen",
    "Prince", "Adele", "Taylor Swift", "Beyoncé", "Drake",
    "Kanye West", "Coldplay", "Eminem", "Lady Gaga", "Rihanna",
    "Katy Perry", "Justin Timberlake", "Britney Spears", "Usher", "Bruno Mars"
]
albums = [
    "Abbey Road", "Elvis: As Recorded at Madison Square Garden", "Thriller", "Like a Virgin", "Led Zeppelin IV",
    "The Dark Side of the Moon", "Whitney", "Goodbye Yellow Brick Road", "Daydream", "A Night at the Opera",
    "Purple Rain", "21", "Fearless", "Lemonade", "Views",
    "The College Dropout", "A Rush of Blood to the Head", "The Marshall Mathers LP", "The Fame", "Good Girl Gone Bad",
    "Teenage Dream", "FutureSex/LoveSounds", "...Baby One More Time", "Confessions", "Doo-Wops & Hooligans"
]
sales = [5, 7, 10, 9, 8, 6, 4, 8, 7, 5, 6, 9, 8, 7, 10, 9, 8, 10, 7, 6, 9, 8, 7, 6, 5]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(
    range(len(sales)),
    sales,
    alpha=0.7,
    c=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Top 25 Best-Selling Music Albums by Artist', pad=20)
ax.set_xlabel('Albums', labelpad=15)
ax.set_ylabel('Sales (Millions)', labelpad=15)

# Adding the album names as labels next to each point
for i, album in enumerate(albums):
    ax.annotate(album, (i, sales[i]), fontsize=8)

plt.xticks(range(len(sales)), artists, rotation=90)
plt.tight_layout()
plt.show()