
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
books_read = np.array([5, 6, 7, 8, 7, 9, 10, 11, 12, 10, 11, 12])
movies_watched = np.array([3, 4, 5, 6, 7, 8, 9, 10, 8, 9, 7, 10])
workshops_attended = np.array([2, 3, 2, 3, 4, 5, 4, 5, 3, 4, 6, 5])
online_courses_completed = np.array([1, 2, 3, 3, 4, 3, 2, 4, 3, 5, 6, 4])
lectures_listened = np.array([4, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13])

education_data = np.vstack([books_read, movies_watched, workshops_attended, online_courses_completed, lectures_listened])

fig, ax = plt.subplots(figsize=(14, 7))
ax.stackplot(months, education_data, colors=['#FF5733', '#33C1FF', '#75FF33', '#FF33A1', '#B833FF'])
ax.set_title('Monthly Educational Activities for 2023', fontsize=18, fontweight='bold', loc='left')
ax.set_ylabel('Number of Activities')

max_books_index = np.argmax(books_read)
ax.annotate('Max Books Read', xy=(max_books_index, books_read[max_books_index]), xytext=(max_books_index, books_read[max_books_index] + 5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

ax.legend(['Books Read', 'Movies Watched', 'Workshops Attended', 'Online Courses Completed', 'Lectures Listened'], loc='upper left')

plt.tight_layout()
plt.show()