
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
expenses = [2000, 1800, 2200, 2400, 2600, 2500, 2700, 2600, 2800, 3000, 2900, 3100]

plt.figure(figsize=(16, 10))

# Plotting the line chart
plt.plot(months, expenses, color="#ff5733", marker='o')

# Adding annotations for specific points
plt.annotate('End of year peak', xy=('December', 3100), xytext=('November', 3200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Mid-year high', xy=('July', 2700), xytext=('June', 2800),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Expenses Data for Household X')
plt.xlabel('Month')
plt.ylabel('Expenses (in $)')
plt.gca().invert_yaxis()

# Show the chart
plt.show()