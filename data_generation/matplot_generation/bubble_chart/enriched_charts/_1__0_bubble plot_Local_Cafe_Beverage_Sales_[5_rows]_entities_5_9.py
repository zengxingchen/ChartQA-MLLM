
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
books = [50, 60, 55, 65, 70, 75, 80]
ebooks = [20, 25, 30, 35, 40, 50, 55]
audiobooks = [10, 15, 20, 25, 30, 35, 45]
magazines = [30, 28, 26, 24, 22, 20, 18]
journals = [15, 18, 20, 22, 24, 26, 28]
blogs = [25, 30, 35, 40, 45, 50, 55]
podcasts = [5, 10, 15, 20, 25, 30, 35]

# Bubble sizes
bubble_scale = 100
book_sizes = np.array(books) * bubble_scale
ebook_sizes = np.array(ebooks) * bubble_scale
audiobook_sizes = np.array(audiobooks) * bubble_scale
magazine_sizes = np.array(magazines) * bubble_scale
journal_sizes = np.array(journals) * bubble_scale
blog_sizes = np.array(blogs) * bubble_scale
podcast_sizes = np.array(podcasts) * bubble_scale

fig, ax = plt.subplots(figsize=(16, 10))

# Create scatter points for each category
ax.scatter(years, books, s=book_sizes, color='#FF6347', alpha=0.6, label='Books')
ax.scatter(years, ebooks, s=ebook_sizes, color='#4682B4', alpha=0.6, label='E-Books')
ax.scatter(years, audiobooks, s=audiobook_sizes, color='#32CD32', alpha=0.6, label='Audiobooks')
ax.scatter(years, magazines, s=magazine_sizes, color='#FFD700', alpha=0.6, label='Magazines')
ax.scatter(years, journals, s=journal_sizes, color='#8A2BE2', alpha=0.6, label='Journals')
ax.scatter(years, blogs, s=blog_sizes, color='#FF4500', alpha=0.6, label='Blogs')
ax.scatter(years, podcasts, s=podcast_sizes, color='#1E90FF', alpha=0.6, label='Podcasts')

# Chart title and labels
ax.set_title('Reading and Listening Habits Over the Years', fontsize=20, pad=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number of Users (in millions)', fontsize=16)

# Legend
ax.legend(loc='upper left', title='Category')

plt.tight_layout()
plt.show()