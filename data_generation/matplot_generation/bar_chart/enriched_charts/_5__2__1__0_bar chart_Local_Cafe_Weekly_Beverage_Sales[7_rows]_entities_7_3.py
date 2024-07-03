
import matplotlib.pyplot as plt

genres = ['Science Fiction', 'Romance', 'Mystery', 'Historical', 'Fantasy', 'Non-fiction', 'Biography', 'Thriller', 'Self-help', 'Children', 'Poetry', 'Graphic Novels']
number_of_books = [45, 60, 35, 20, 55, 25, 30, 40, 50, 15, 10, 22]

colors = ['#1E90FF', '#FF69B4', '#8B0000', '#FFD700', '#7FFF00', '#D2691E', '#FF4500', '#2E8B57', '#8A2BE2', '#00CED1', '#DA70D6', '#4682B4']

plt.figure(figsize=(10, 15))
plt.bar(genres, number_of_books, color=colors, edgecolor='black', width=0.6)

plt.ylabel('Number of Books', fontsize=12)
plt.xlabel('Genre', fontsize=12)
plt.title('Number of Books per Genre in 2023', fontsize=16, pad=20)
plt.ylim(5, 70)

plt.tight_layout()
plt.show()