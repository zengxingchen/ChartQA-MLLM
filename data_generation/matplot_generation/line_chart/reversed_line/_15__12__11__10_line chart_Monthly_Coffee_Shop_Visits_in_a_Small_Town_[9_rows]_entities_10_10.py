
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Fiction': 100, 'Non-Fiction': 120, 'Mystery': 90, 'Sci-Fi': 110, 'Romance': 130},
    {'Month': 'February', 'Fiction': 98, 'Non-Fiction': 118, 'Mystery': 92, 'Sci-Fi': 108, 'Romance': 128},
    {'Month': 'March', 'Fiction': 95, 'Non-Fiction': 115, 'Mystery': 95, 'Sci-Fi': 105, 'Romance': 125},
    {'Month': 'April', 'Fiction': 93, 'Non-Fiction': 113, 'Mystery': 97, 'Sci-Fi': 103, 'Romance': 123},
    {'Month': 'May', 'Fiction': 90, 'Non-Fiction': 110, 'Mystery': 100, 'Sci-Fi': 100, 'Romance': 120},
    {'Month': 'June', 'Fiction': 88, 'Non-Fiction': 108, 'Mystery': 102, 'Sci-Fi': 98, 'Romance': 118},
    {'Month': 'July', 'Fiction': 85, 'Non-Fiction': 105, 'Mystery': 105, 'Sci-Fi': 95, 'Romance': 115},
    {'Month': 'August', 'Fiction': 83, 'Non-Fiction': 103, 'Mystery': 107, 'Sci-Fi': 93, 'Romance': 113},
    {'Month': 'September', 'Fiction': 80, 'Non-Fiction': 100, 'Mystery': 110, 'Sci-Fi': 90, 'Romance': 110},
    {'Month': 'October', 'Fiction': 78, 'Non-Fiction': 98, 'Mystery': 112, 'Sci-Fi': 88, 'Romance': 108},
    {'Month': 'November', 'Fiction': 75, 'Non-Fiction': 95, 'Mystery': 115, 'Sci-Fi': 85, 'Romance': 105},
    {'Month': 'December', 'Fiction': 73, 'Non-Fiction': 93, 'Mystery': 117, 'Sci-Fi': 83, 'Romance': 103}
]

months = [entry['Month'] for entry in data]

plt.figure(figsize=(16, 8))
genres = list(data[0].keys())[1:]

line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#0000FF', '#FF0000', '#00FF00', '#FFFF00', '#FF00FF']

for i, genre in enumerate(genres):
    values = [entry[genre] for entry in data]
    plt.plot(months, values, label=genre, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

plt.title('Monthly Sales of Different Book Genres', pad=20, loc='left')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.gca().invert_yaxis()

plt.grid(True)
plt.legend(title='Genres', loc='upper right')

plt.show()