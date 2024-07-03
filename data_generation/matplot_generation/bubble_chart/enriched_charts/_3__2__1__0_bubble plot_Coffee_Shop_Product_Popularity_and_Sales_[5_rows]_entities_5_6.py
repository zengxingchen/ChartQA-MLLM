
import matplotlib.pyplot as plt

artists = [
    'The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna', 'Elton John', 
    'Led Zeppelin', 'Pink Floyd', 'Rihanna', 'Eminem', 'Taylor Swift', 
    'Whitney Houston', 'Queen', 'Celine Dion', 'AC/DC', 'Mariah Carey', 
    'The Rolling Stones', 'Beyoncé', 'Billy Joel', 'Garth Brooks', 'U2', 
    'Katy Perry', 'Adele', 'Bruno Mars', 'Justin Bieber', 'Drake', 
    'Ariana Grande', 'Post Malone', 'Shakira'
]

album_sales = [
    600000000, 500000000, 350000000, 300000000, 300000000, 300000000, 250000000, 
    250000000, 230000000, 200000000, 200000000, 200000000, 200000000, 200000000, 
    200000000, 200000000, 150000000, 150000000, 150000000, 150000000, 100000000, 
    100000000, 80000000, 80000000, 60000000, 50000000, 50000000, 50000000
]

number_of_albums = [
    23, 60, 10, 14, 31, 9, 15, 8, 11, 10, 7, 15, 27, 17, 15, 30, 6, 13, 12, 14, 
    5, 4, 3, 6, 5, 5, 4, 11
]

popularity = [
    98, 95, 97, 93, 92, 91, 90, 89, 88, 94, 87, 86, 85, 84, 83, 82, 81, 80, 79, 
    78, 77, 76, 75, 74, 73, 72, 71, 70
]

bubble_size = [pop * 10 for pop in popularity]

plt.figure(figsize=(20, 14))

plt.scatter(album_sales, number_of_albums, s=bubble_size,
            color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', 
                   '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', '#FF5733', '#33FF57', 
                   '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', 
                   '#33FFF3', '#FF3357', '#33FF3F', '#FF5733', '#33FF57', '#3357FF', '#FFFF33'],
            alpha=0.7, edgecolors='w', linewidth=2)

plt.title('Top Music Artists by Album Sales and Number of Albums', pad=20)
plt.xlabel('Album Sales')
plt.ylabel('Number of Albums')

for i, artist in enumerate(artists):
    plt.text(album_sales[i], number_of_albums[i], artist, ha='center', va='center', fontsize=9)

plt.show()