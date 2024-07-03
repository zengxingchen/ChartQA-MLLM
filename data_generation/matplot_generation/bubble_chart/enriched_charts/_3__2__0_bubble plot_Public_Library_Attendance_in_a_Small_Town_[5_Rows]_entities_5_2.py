
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['Science Fiction', 'Science Fiction', 'Drama', 'Drama', 'Action', 'Action', 'Comedy', 'Comedy', 
                 'Romance', 'Romance', 'Thriller', 'Thriller', 'Horror', 'Horror', 'Documentary', 'Documentary', 
                 'Animation', 'Animation', 'Fantasy', 'Fantasy'],
    'Movie': ['Movie A', 'Movie B', 'Movie A', 'Movie B', 'Movie A', 'Movie B', 'Movie A', 'Movie B', 
              'Movie A', 'Movie B', 'Movie A', 'Movie B', 'Movie A', 'Movie B', 'Movie A', 'Movie B', 
              'Movie A', 'Movie B', 'Movie A', 'Movie B'],
    'Box Office Revenue': [1200000, 1500000, 1000000, 2000000, 1800000, 2200000, 1600000, 1900000, 
                           1400000, 1700000, 1300000, 1600000, 1100000, 1400000, 900000, 1200000, 
                           1900000, 2100000, 1700000, 2000000],
    'Audience Rating': [85, 88, 90, 92, 75, 80, 70, 73, 78, 82, 88, 91, 65, 68, 95, 97, 83, 86, 89, 93],
    'Reviews Count': [300, 400, 500, 800, 450, 600, 350, 420, 310, 390, 280, 370, 260, 330, 200, 290, 500, 570, 450, 520]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(18, 12))
scatter = ax.scatter(x='Box Office Revenue', y='Audience Rating', s=df['Reviews Count']*10, 
                     alpha=0.6, c=['#FF5733', '#33FF57', '#3357FF', '#FF33D4', '#33FFF6', '#F633FF', '#FF8333', '#33FF83', 
                                   '#8333FF', '#3357FF', '#57FF33', '#FFD333', '#FF5733', '#33FF57', '#3357FF', '#FF33D4', 
                                   '#33FFF6', '#F633FF', '#FF8333', '#33FF83'], data=df)

ax.set_title('Movie Ratings and Revenue by Review Count', fontsize=20)
ax.set_xlabel('Box Office Revenue (in USD)', fontsize=14)
ax.set_ylabel('Audience Rating (out of 100)', fontsize=14)
plt.grid(True)

for area in [200, 400, 600, 800]: 
    plt.scatter([], [], c='grey', alpha=0.5, s=area, label=f'{area/10} Reviews Count')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Reviews Count', loc='upper right')

plt.tight_layout()
plt.show()