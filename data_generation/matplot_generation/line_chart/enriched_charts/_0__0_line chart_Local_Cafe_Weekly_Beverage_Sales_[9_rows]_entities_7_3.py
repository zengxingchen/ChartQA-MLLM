
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [100, 120, 150, 180, 210, 230, 260, 240, 220, 200, 170, 140]

plt.figure(figsize=(14, 8))

# Plotting the line chart
plt.plot(months, sales, color="#1f77b4", marker='s')

# Adding annotations for specific points
plt.annotate('Summer peak', xy=('July', 260), xytext=('June', 280),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Year-end dip', xy=('December', 140), xytext=('November', 160),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Sales Data for Product Y')
plt.xlabel('Month')
plt.ylabel('Sales (in units)')

# Show the chart
plt.show()