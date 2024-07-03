
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [102, 95, 89, 110, 120, 135, 140, 128, 115, 105, 98, 90]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, rainfall, marker='o', linestyle='-', color='#8B0000')

# Annotate the highest and lowest rainfall points
plt.annotate('Highest\n140 mm', xy=('July', 140), xytext=('August', 145),
             arrowprops=dict(facecolor='#228B22', shrink=0.05), color='#228B22')
plt.annotate('Lowest\n89 mm', xy=('March', 89), xytext=('April', 95),
             arrowprops=dict(facecolor='#228B22', shrink=0.05), color='#228B22')

# Title and labels
plt.title('Monthly Rainfall in New York (Millimeters)', pad=20)
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()