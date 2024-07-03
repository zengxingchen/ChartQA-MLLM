
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
revenue = [300, 320, 280, 350, 370, 400, 450, 420, 410, 390, 370, 340]

plt.figure(figsize=(14, 8))

# Plotting the line chart
plt.plot(months, revenue, color="#1f77b4", marker='o')

# Adding annotations for specific points
plt.annotate('Mid-Year Peak', xy=('July', 450), xytext=('June', 470),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Year-end Decline', xy=('December', 340), xytext=('November', 360),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Revenue for Tech Company', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in $1000)', fontsize=12)
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the chart
plt.show()