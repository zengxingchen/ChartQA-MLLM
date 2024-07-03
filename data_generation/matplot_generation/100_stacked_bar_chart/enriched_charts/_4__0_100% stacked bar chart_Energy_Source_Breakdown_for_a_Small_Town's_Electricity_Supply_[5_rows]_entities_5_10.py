
import matplotlib.pyplot as plt

years = ['2019', '2020', '2021', '2022', '2023', '2024']
book_genres = {
    'Science Fiction': [20, 22, 24, 25, 27, 29],
    'Fantasy': [30, 28, 26, 25, 23, 21],
    'Mystery': [25, 24, 23, 22, 21, 20],
    'Romance': [15, 16, 17, 18, 19, 20],
    'Horror': [10, 10, 10, 10, 10, 10]
}

totals = [sum(values) for values in zip(*book_genres.values())]
data_percentage = {genre: [value / total * 100 for value, total in zip(values, totals)]
                   for genre, values in book_genres.items()}

colors = {
    'Science Fiction': '#FF5733',
    'Fantasy': '#33FF57',
    'Mystery': '#3357FF',
    'Romance': '#FF33A1',
    'Horror': '#8C33FF'
}

prev_values = [0] * len(years)
fig, ax = plt.subplots(figsize=(12, 6))

for genre, values in data_percentage.items():
    ax.bar(
        years,
        values,
        bottom=prev_values,
        color=colors[genre],
        edgecolor='white',
        width=0.6
    )
    prev_values = [pv + v for pv, v in zip(prev_values, values)]

ax.set_ylabel('Percentage')
ax.set_title('Book Genre Distribution Over the Years')
ax.set_ylim(0, 100)

genre_patches = [plt.Rectangle((0, 0), 1, 1, color=colors[genre]) for genre in book_genres]
ax.legend(genre_patches, book_genres.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()