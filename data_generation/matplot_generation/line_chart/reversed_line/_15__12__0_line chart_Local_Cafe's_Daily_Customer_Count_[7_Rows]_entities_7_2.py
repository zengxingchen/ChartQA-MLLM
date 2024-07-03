
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [50, 45, 55, 60, 70, 85, 90, 88, 78, 65, 55, 50]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, revenue, marker='o', linestyle='-', color='#2A9D8F')

# Annotate the highest and lowest revenue points
plt.annotate('Highest\n$90k', xy=('July', 90), xytext=('August', 85),
             arrowprops=dict(facecolor='#E76F51', shrink=0.05), color='#E76F51')
plt.annotate('Lowest\n$45k', xy=('February', 45), xytext=('March', 50),
             arrowprops=dict(facecolor='#E76F51', shrink=0.05), color='#E76F51')

# Title and labels
plt.title('Monthly Revenue of a Small Business (in $1000)', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue (in $1000)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Invert Y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()