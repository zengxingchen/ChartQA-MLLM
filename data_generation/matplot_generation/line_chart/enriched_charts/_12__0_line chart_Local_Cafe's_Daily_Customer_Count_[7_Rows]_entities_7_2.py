
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [30, 32, 45, 55, 68, 77, 83, 81, 74, 61, 48, 35]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, temperatures, marker='o', linestyle='-', color='#1D3557')

# Annotate the highest and lowest temperature points
plt.annotate('Highest\n83°F', xy=('July', 83), xytext=('August', 79),
             arrowprops=dict(facecolor='#E63946', shrink=0.05), color='#E63946')
plt.annotate('Lowest\n30°F', xy=('January', 30), xytext=('February', 34),
             arrowprops=dict(facecolor='#E63946', shrink=0.05), color='#E63946')

# Title and labels
plt.title('Average Monthly Temperature in San Francisco (Degrees Fahrenheit)')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°F)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()