
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
ratings = [7.2, 6.8, 7.5, 7.9, 8.1, 8.4, 8.5, 8.3, 7.9, 7.6, 7.2, 6.9]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(months, ratings, marker='o', linestyle='-', color='#3498db')  # Specific hex color

# Annotation for the highest rating
plt.annotate('Highest Rating', xy=('July', 8.5), xytext=('September', 9.0),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Happiness Index')
plt.title('Monthly Happiness Index in 2023')

# Invert the y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()