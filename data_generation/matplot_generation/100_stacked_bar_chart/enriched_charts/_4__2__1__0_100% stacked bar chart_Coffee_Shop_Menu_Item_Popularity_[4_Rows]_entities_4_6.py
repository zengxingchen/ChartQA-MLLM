
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['Children', 'Teens', 'Young Adults', 'Adults', 'Seniors']
books_read = np.array([10, 25, 30, 40, 20])
articles_read = np.array([15, 35, 40, 30, 25])
magazines_read = np.array([5, 20, 15, 10, 8])
blogs_read = np.array([20, 30, 50, 35, 15])
research_papers_read = np.array([2, 10, 20, 25, 10])

# Normalize data to 100%
total = books_read + articles_read + magazines_read + blogs_read + research_papers_read
books_read = books_read / total * 100
articles_read = articles_read / total * 100
magazines_read = magazines_read / total * 100
blogs_read = blogs_read / total * 100
research_papers_read = research_papers_read / total * 100

# Stack data
ind = np.arange(len(age_groups))
width = 0.8  # Width of the bars

# Plot
fig, ax = plt.subplots(figsize=(8, 10))

p1 = ax.bar(ind, books_read, width, color='#FF6347')
p2 = ax.bar(ind, articles_read, width, bottom=books_read, color='#4682B4')
p3 = ax.bar(ind, magazines_read, width, bottom=books_read+articles_read, color='#32CD32')
p4 = ax.bar(ind, blogs_read, width, bottom=books_read+articles_read+magazines_read, color='#FFD700')
p5 = ax.bar(ind, research_papers_read, width, bottom=books_read+articles_read+magazines_read+blogs_read, color='#6A5ACD')

ax.set_ylabel('Percentage')
ax.set_title('Reading Habits by Age Group', pad=20)
ax.set_xticks(ind)
ax.set_xticklabels(age_groups)
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Books', 'Articles', 'Magazines', 'Blogs', 'Research Papers'), bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()