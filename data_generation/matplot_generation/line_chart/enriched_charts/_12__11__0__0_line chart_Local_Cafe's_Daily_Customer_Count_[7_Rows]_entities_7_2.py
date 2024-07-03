
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall_levels = [78, 85, 65, 92, 110, 98, 130, 120, 105, 95, 88, 102]

# Create the plot
plt.figure(figsize=(16, 8))
plt.plot(months, rainfall_levels, marker='s', linestyle='-', color='#4B0082')

# Annotate the highest and lowest rainfall level points
plt.annotate('Highest\n130 mm', xy=('July', 130), xytext=('August', 135),
             arrowprops=dict(facecolor='#00FF00', shrink=0.05), color='#00FF00')
plt.annotate('Lowest\n65 mm', xy=('March', 65), xytext=('April', 60),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), color='#FF6347')

# Title and labels
plt.title('Monthly Rainfall Levels in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Rainfall Level (mm)')

# Customize the grid
plt.grid(True, which='both', linestyle=':', linewidth=0.6)

# Show the plot
plt.show()