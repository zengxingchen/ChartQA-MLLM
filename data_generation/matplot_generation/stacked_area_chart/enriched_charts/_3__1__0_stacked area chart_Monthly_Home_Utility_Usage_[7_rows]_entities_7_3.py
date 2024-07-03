
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
concerts = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230])
theater = np.array([110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220])
movies = np.array([140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])
exhibitions = np.array([130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
festivals = np.array([90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])

# Stacking the data
events = np.vstack([concerts, theater, movies, exhibitions, festivals])

# Plot
fig, ax = plt.subplots(figsize=(16, 8))
ax.stackplot(months, events, colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFC133'])
ax.set_title('Monthly Attendance in Entertainment Events in 2023', fontsize=20, fontweight='bold', loc='center')
ax.set_ylabel('Attendance (Thousands)')

# Adding annotation on the chart for the maximum movie attendance
max_movies_index = np.argmax(movies)
ax.annotate('Max Movies', xy=(max_movies_index, movies[max_movies_index]), xytext=(max_movies_index, movies[max_movies_index] + 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

# Adding a legend
ax.legend(['Concerts', 'Theater', 'Movies', 'Exhibitions', 'Festivals'], loc='upper left')

plt.tight_layout()
plt.show()