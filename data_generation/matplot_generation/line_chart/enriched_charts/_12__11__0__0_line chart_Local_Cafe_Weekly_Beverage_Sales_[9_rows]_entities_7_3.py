
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [1500, 1300, 1700, 2200, 2100, 2400, 2700, 2600, 2500, 2300, 2000, 1800]

plt.figure(figsize=(14, 8))

# Plotting the line chart
plt.plot(months, sales, color="#2E8B57", marker='o')

# Adding annotations for specific points
plt.annotate('Spring Surge', xy=('April', 2200), xytext=('March', 2400),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Summer High', xy=('July', 2700), xytext=('June', 2900),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Winter Drop', xy=('December', 1800), xytext=('November', 2100),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Sales Growth for Organic Food Store', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales ($)')

# Show the chart
plt.show()