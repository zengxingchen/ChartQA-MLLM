
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
visitors = [3000, 2800, 2500, 2200, 2000, 1800, 1600, 1400, 1300, 1200, 1000, 800]

plt.figure(figsize=(14, 8))

# Plotting the line chart
plt.plot(months, visitors, color="#0073e6", marker='o')

# Adding annotations for specific points
plt.annotate('Spring Decline', xy=('April', 2200), xytext=('March', 2400),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Summer Low', xy=('August', 1400), xytext=('July', 1600),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Year-end Drop', xy=('December', 800), xytext=('November', 1000),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Visitor Decline at National Park', pad=20)
plt.xlabel('Month')
plt.ylabel('Visitors')
plt.gca().invert_yaxis()  # Inverting the y-axis

# Show the chart
plt.show()