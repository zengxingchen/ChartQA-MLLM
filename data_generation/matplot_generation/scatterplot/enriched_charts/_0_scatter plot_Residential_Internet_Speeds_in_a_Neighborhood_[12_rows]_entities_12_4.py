
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [1, 3, 6, 12, 16, 20, 23, 22, 18, 13, 7, 2]
ice_cream_sales = [12, 14, 18, 22, 26, 30, 34, 33, 27, 21, 16, 13]

# Convert month names to numbers for plotting
month_numbers = [i+1 for i, _ in enumerate(months)]

# Scatter plot
plt.figure(figsize=(10, 5))  # Change the size of the plot
plt.scatter(month_numbers, average_temperature, c=['#3498db', '#e74c3c', '#2ecc71', '#f1c40f',
                                                   '#9b59b6', '#34495e', '#95a5a6', '#e67e22',
                                                   '#d35400', '#7f8c8d', '#2c3e50', '#1abc9c'],
            s=ice_cream_sales, alpha=0.6)  # Size corresponds to ice cream sales, improved color scheme

# Customize the axes
plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Temperature (Celsius)')
plt.title('Ice Cream Sales vs Average Temperature Per Month')
plt.xlim(0, 13)  # Set the limit to include all months

# Show the plot
plt.tight_layout()  # Adjust layout to fit the figure neatly
plt.show()