
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Under 18', '18-25', '26-35', '36-50', 'Over 50']
books = [15, 30, 25, 20, 10]
music = [25, 20, 20, 25, 15]
movies = [20, 25, 30, 20, 15]
art = [25, 20, 15, 20, 20]
theater = [15, 15, 10, 15, 25]

# Plot settings
barWidth = 0.6
fig, ax = plt.subplots(figsize=(10, 8))

# Stack the bars
p1 = ax.bar(labels, books, color='#FF5733', edgecolor='white', width=barWidth, label='Books')
p2 = ax.bar(labels, music, bottom=books, color='#33FF57', edgecolor='white', width=barWidth, label='Music')
p3 = ax.bar(labels, movies, bottom=np.add(books, music), color='#3357FF', edgecolor='white', width=barWidth, label='Movies')
p4 = ax.bar(labels, art, bottom=np.add(books, np.add(music, movies)), color='#F4C300', edgecolor='white', width=barWidth, label='Art')
p5 = ax.bar(labels, theater, bottom=np.add(books, np.add(music, np.add(movies, art))), color='#A569BD', edgecolor='white', width=barWidth, label='Theater')

# Add legend and labels
ax.set_ylabel('Percentage of Interest')
ax.set_title('Interest in Different Cultural Activities by Age Group', pad=20)
ax.legend(loc='upper right')

# Display chart
plt.show()