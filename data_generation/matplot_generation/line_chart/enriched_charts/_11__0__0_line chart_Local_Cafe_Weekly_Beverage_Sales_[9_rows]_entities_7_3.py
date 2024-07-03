
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
subscribers = [1200, 1400, 1600, 1800, 2200, 2500, 2800, 3000, 2700, 2400, 2100, 1800]

plt.figure(figsize=(16, 10))

# Plotting the line chart
plt.plot(months, subscribers, color="#ff5733", marker='o')

# Adding annotations for specific points
plt.annotate('Spring Growth', xy=('April', 1800), xytext=('March', 2000),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Summer Peak', xy=('August', 3000), xytext=('July', 3200),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Year-end Decline', xy=('December', 1800), xytext=('November', 2000),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Subscriber Growth for Tech Newsletter', pad=20)
plt.xlabel('Month')
plt.ylabel('Subscribers')

# Show the chart
plt.show()