
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
movies = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260])
books = np.array([180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
concerts = np.array([130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
theater = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310])
travel = np.array([170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280])

# Stacking the data
entertainment_data = np.vstack([movies, books, concerts, theater, travel])

# Plot
fig, ax = plt.subplots(figsize=(18, 9))  # Modified chart size
ax.stackplot(months, entertainment_data, colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD'])
ax.set_title('Monthly Entertainment Expenses in 2023', fontsize=20, fontweight='bold', loc='right')  # Changed title
ax.set_ylabel('Expenses (in million $)')
ax.set_xlabel('Month')

# Adding annotation on the chart for the maximum theater expenses
max_theater_index = np.argmax(theater)
ax.annotate('Peak Theater Expenses', xy=(max_theater_index, theater[max_theater_index]), xytext=(max_theater_index, theater[max_theater_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

# Adding legend
ax.legend(['Movies', 'Books', 'Concerts', 'Theater', 'Travel'], loc='upper left')

plt.tight_layout()
plt.show()