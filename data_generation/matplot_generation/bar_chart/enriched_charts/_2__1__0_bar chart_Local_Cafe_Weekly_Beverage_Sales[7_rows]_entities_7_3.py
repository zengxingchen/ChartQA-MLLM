
import matplotlib.pyplot as plt

genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Documentary', 'Thriller', 'Animation', 'Musical', 'Western']
number_of_movies = [25, 30, 20, 15, 18, 22, 19, 12, 17, 14, 9, 5]

colors = ['#FF6347', '#FFD700', '#8A2BE2', '#FF4500', '#32CD32', '#DC143C', '#00CED1', '#9400D3', '#FF1493', '#4682B4', '#20B2AA', '#7B68EE']

plt.figure(figsize=(12, 8))
plt.barh(genres, number_of_movies, color=colors, edgecolor='black', height=0.5)

plt.xlabel('Number of Movies', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.title('Number of Movies per Genre in 2021', fontsize=16, pad=20)
plt.xlim(0, 35)

plt.tight_layout()
plt.show()