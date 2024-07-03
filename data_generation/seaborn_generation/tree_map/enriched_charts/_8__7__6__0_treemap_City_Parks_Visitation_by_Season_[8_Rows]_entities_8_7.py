
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Topic': ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Thriller', 'Horror', 'Biography', 'History', 'Science', 'Self-Help', 'Travel', 'Humor', 'Health', 'Religion', 'Education', 'Adventure', 'Poetry', 'Drama', 'Classics', 'Children', 'Comics', 'Cooking', 'Art'],
    'Market Share': [12, 10, 9, 8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
}

df = pd.DataFrame(data)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#2E8B57', '#DAA520', '#D2691E', '#87CEEB', '#FF69B4', '#8B0000', '#00FF7F', '#9400D3', '#CD5C5C', '#4B0082', '#00CED1', '#FF1493', '#008080', '#BDB76B', '#FA8072', '#7FFF00', '#FF7F50']

plt.figure(figsize=(28, 14))
squarify.plot(sizes=df['Market Share'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Market Share of Book Genres in 2023', fontsize=26, pad=20)

plt.axis('off')

plt.show()