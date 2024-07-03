
import matplotlib.pyplot as plt

# Data
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
reading_hours = [2.5, 3.0, 4.2, 3.8, 4.5, 5.0, 5.5, 6.2, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]
books_read = [1, 1, 2, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]

# Scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(weeks, reading_hours, color='#FF4500', label='Reading Hours')  # OrangeRed
plt.scatter(weeks, books_read, color='#1E90FF', label='Books Read')  # DodgerBlue

# Customize the plot
plt.title('Weekly Reading Hours and Books Read Over 20 Weeks', pad=20)
plt.xlabel('Week')
plt.ylabel('Count')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()