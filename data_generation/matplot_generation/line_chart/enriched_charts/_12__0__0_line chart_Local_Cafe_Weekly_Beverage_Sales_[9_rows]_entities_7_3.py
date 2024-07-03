
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
visitors = [80, 85, 90, 120, 150, 180, 220, 210, 200, 160, 120, 100]

plt.figure(figsize=(16, 10))

# Plotting the line chart
plt.plot(months, visitors, color="#FF5733", marker='o')

# Adding annotations for specific points
plt.annotate('Summer Peak', xy=('July', 220), xytext=('June', 240),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Year-end Decline', xy=('December', 100), xytext=('November', 120),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Visitor Count for National Park')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Show the chart
plt.show()