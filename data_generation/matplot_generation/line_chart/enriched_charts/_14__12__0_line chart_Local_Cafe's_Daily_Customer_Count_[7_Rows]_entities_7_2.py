
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
concerts = [2, 3, 5, 4, 6, 9, 11, 12, 10, 8, 6, 4]

# Create the plot
plt.figure(figsize=(10, 8))
plt.plot(months, concerts, marker='o', linestyle='-', color='#FF5733')

# Annotate the highest and lowest points
plt.annotate('Highest\n12 concerts', xy=('August', 12), xytext=('September', 11),
             arrowprops=dict(facecolor='#C70039', shrink=0.05), color='#C70039')
plt.annotate('Lowest\n2 concerts', xy=('January', 2), xytext=('February', 3),
             arrowprops=dict(facecolor='#C70039', shrink=0.05), color='#C70039')

# Title and labels
plt.title('Monthly Number of Concerts in a City')
plt.xlabel('Month')
plt.ylabel('Number of Concerts')

# Customize the grid and invert y-axis
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().invert_yaxis()

# Show the plot
plt.show()