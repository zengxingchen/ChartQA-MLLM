
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [23, 26, 35, 47, 59, 70, 76, 74, 66, 54, 42, 30]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(months, temperatures, marker='o', linestyle='-', color='#0077B6')

# Annotate the highest and lowest temperature points
plt.annotate('Highest\n76°F', xy=('July', 76), xytext=('August', 72),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05), color='#FF5733')
plt.annotate('Lowest\n23°F', xy=('January', 23), xytext=('February', 27),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05), color='#FF5733')

# Title and labels
plt.title('Average Monthly Temperature in Chicago (Degrees Fahrenheit)')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°F)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()