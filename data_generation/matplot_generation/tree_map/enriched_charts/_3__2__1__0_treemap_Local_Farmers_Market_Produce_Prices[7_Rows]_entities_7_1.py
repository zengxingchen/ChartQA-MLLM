
import matplotlib.pyplot as plt
import squarify

genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Horror', 'Thriller',
          'Historical Fiction', 'Non-Fiction', 'Biography', 'Self-Help', 'Graphic Novels', 'Other']
market_share = [12.8, 15.7, 10.5, 13.9, 7.4, 9.6, 8.1, 14.2, 3.7, 2.9, 1.2, 0.1]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#bcbd22', '#ff6347']

plt.figure(figsize=(14, 10))
squarify.plot(sizes=market_share, label=genres, color=colors, alpha=0.8)

plt.title('Popularity of Book Genres in 2023', fontsize=18, pad=20)
plt.axis('off')

plt.show()