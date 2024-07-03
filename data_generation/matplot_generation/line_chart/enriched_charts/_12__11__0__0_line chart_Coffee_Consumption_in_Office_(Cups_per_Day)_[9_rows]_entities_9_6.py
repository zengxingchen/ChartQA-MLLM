
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
average_ratings = [7.2, 6.8, 7.5, 7.9, 8.1, 8.4, 8.3, 7.6, 7.2, 6.9, 7.0, 7.4]

plt.figure(figsize=(16, 10))  # Adjust width and height of the chart
plt.plot(months, average_ratings, marker='o', linestyle='-', color='#1abc9c')  # Specific hex color

# Annotation for the highest rating
plt.annotate('Highest Rating', xy=('June', 8.4), xytext=('August', 9.0),
             arrowprops=dict(facecolor='#c0392b', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Movie Rating')
plt.title('Average Monthly Movie Ratings in 2023')

# Showing the plot
plt.show()