
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
books_sold = [120, 150, 180, 140, 160, 200, 220, 210, 190, 170, 150, 130]

plt.figure(figsize=(16, 8))

# Plotting the line chart
plt.plot(months, books_sold, color="#FF6347", marker='o')

# Adding annotations for specific points
plt.annotate('Peak Sales', xy=('July', 220), xytext=('June', 230),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Post-Peak Drop', xy=('August', 210), xytext=('September', 230),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Book Sales in Bookstore Y')
plt.xlabel('Month')
plt.ylabel('Books Sold')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the chart
plt.show()