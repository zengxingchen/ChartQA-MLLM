
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Classical': 60, 'Rock': 45, 'Jazz': 30, 'Pop': 50, 'Hip-Hop': 35},
    {'Month': 'February', 'Classical': 58, 'Rock': 47, 'Jazz': 32, 'Pop': 48, 'Hip-Hop': 37},
    {'Month': 'March', 'Classical': 55, 'Rock': 50, 'Jazz': 35, 'Pop': 45, 'Hip-Hop': 40},
    {'Month': 'April', 'Classical': 53, 'Rock': 52, 'Jazz': 38, 'Pop': 43, 'Hip-Hop': 42},
    {'Month': 'May', 'Classical': 50, 'Rock': 55, 'Jazz': 40, 'Pop': 40, 'Hip-Hop': 45},
    {'Month': 'June', 'Classical': 48, 'Rock': 58, 'Jazz': 42, 'Pop': 38, 'Hip-Hop': 47},
    {'Month': 'July', 'Classical': 45, 'Rock': 60, 'Jazz': 45, 'Pop': 35, 'Hip-Hop': 50},
    {'Month': 'August', 'Classical': 43, 'Rock': 62, 'Jazz': 48, 'Pop': 33, 'Hip-Hop': 52},
    {'Month': 'September', 'Classical': 40, 'Rock': 65, 'Jazz': 50, 'Pop': 30, 'Hip-Hop': 55},
    {'Month': 'October', 'Classical': 38, 'Rock': 67, 'Jazz': 52, 'Pop': 28, 'Hip-Hop': 57},
    {'Month': 'November', 'Classical': 35, 'Rock': 70, 'Jazz': 55, 'Pop': 25, 'Hip-Hop': 60},
    {'Month': 'December', 'Classical': 33, 'Rock': 72, 'Jazz': 57, 'Pop': 23, 'Hip-Hop': 62}
]

months = [entry['Month'] for entry in data]

plt.figure(figsize=(14, 10))
genres = list(data[0].keys())[1:]

line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#1a1aff', '#ff1a1a', '#33cc33', '#ffcc00', '#cc0099']

for i, genre in enumerate(genres):
    values = [entry[genre] for entry in data]
    plt.plot(months, values, label=genre, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

plt.title('Monthly Popularity of Music Genres', pad=20)
plt.xlabel('Month')
plt.ylabel('Popularity Index')

plt.grid(True)
plt.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1))

plt.show()