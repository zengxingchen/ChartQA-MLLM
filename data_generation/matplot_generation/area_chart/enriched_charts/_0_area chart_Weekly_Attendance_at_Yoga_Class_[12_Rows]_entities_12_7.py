
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [2, 3, 6, 11, 16, 20, 23, 22, 18, 13, 7, 3]

# Figure Size
plt.figure(figsize=(12, 6))

# Plot area chart
plt.fill_between(months, temperatures, color='#76B947')

# Title and labels
plt.title('Average Monthly Temperatures in Fictional City')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Show grid
plt.grid(True)

# Show the plot
plt.show()