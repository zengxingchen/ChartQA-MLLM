
import matplotlib.pyplot as plt

genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Thriller', 'Horror', 'Non-Fiction', 'Historical Fiction', 'Young Adult', 'Children', 'Classic', 'Biography', 'Self-Help', 'Poetry', 'Graphic Novel', 'Dystopian', 'Adventure', 'Crime', 'Drama', 'Satire']
popularity = [8.5, 7.8, 6.9, 7.2, 8.0, 5.8, 6.5, 7.0, 7.5, 6.8, 8.3, 7.1, 5.9, 6.2, 7.6, 7.9, 8.1, 6.7, 6.6, 5.5]
ratings = [4.7, 4.5, 4.2, 4.3, 4.6, 3.9, 4.1, 4.2, 4.4, 4.0, 4.8, 4.3, 3.8, 4.0, 4.5, 4.6, 4.7, 4.1, 4.0, 3.7]
users = [120000, 95000, 80000, 70000, 110000, 50000, 60000, 65000, 85000, 45000, 75000, 55000, 35000, 30000, 40000, 100000, 115000, 57000, 52000, 25000]

fig, ax = plt.subplots(figsize=(16, 12))

sizes = [users_count / 200 for users_count in users]

colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733', '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6']

for (genre, pop, rating, size, color) in zip(genres, popularity, ratings, sizes, colors):
    ax.scatter(pop, rating, s=size, label=genre, alpha=0.6, edgecolors='w', color=color)

plt.title('Popularity and Ratings of Book Genres', pad=20, loc='center')
plt.xlabel('Popularity (out of 10)')
plt.ylabel('Average Ratings (out of 5)')

handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper right", title="Genres")

plt.show()