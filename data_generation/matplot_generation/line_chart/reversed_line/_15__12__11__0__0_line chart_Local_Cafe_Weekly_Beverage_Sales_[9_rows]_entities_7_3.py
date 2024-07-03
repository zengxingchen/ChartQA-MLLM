
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
visitors = [10000, 9500, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 13000, 12500, 12000]

plt.figure(figsize=(16, 9))

# Plotting the line chart
plt.plot(months, visitors, color="#FF5733", marker='o')

# Adding annotations for specific points
plt.annotate('Spring Increase', xy=('April', 11000), xytext=('March', 11500),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Summer Peak', xy=('August', 13000), xytext=('July', 13500),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Winter Decrease', xy=('December', 12000), xytext=('November', 12500),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Visitors to National Park', pad=20)
plt.xlabel('Month')
plt.ylabel('Visitors')
plt.gca().invert_yaxis()

# Show the chart
plt.show()