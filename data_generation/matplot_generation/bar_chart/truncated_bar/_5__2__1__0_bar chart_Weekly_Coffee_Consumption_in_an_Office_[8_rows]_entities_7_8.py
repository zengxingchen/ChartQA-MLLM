
import matplotlib.pyplot as plt

genres = ["Fantasy", "Science Fiction", "Mystery", "Romance", "Non-Fiction", "Horror", "Biography", "Thriller", "Historical Fiction", "Classics"]
books_sold = [150, 130, 100, 90, 120, 80, 110, 95, 105, 85]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(genres, books_sold, width=0.5, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

ax.set_title('Books Sold by Genre', fontsize=20)
ax.set_xlabel('Genre', fontsize=14)
ax.set_ylabel('Books Sold', fontsize=14)
ax.set_ylim(50, 160)

ax.xaxis.set_tick_params(labelsize=12, rotation=45)
ax.yaxis.set_tick_params(labelsize=12)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 3, f'{height}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()