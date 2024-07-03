
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
temperatures = [22, 24, 19, 29, 25, 21, 23, 26, 27, 30, 31, 20, 18, 28, 27, 26, 24,
                25, 27, 28, 22, 23, 24, 26, 27, 28, 28, 29, 30, 31]
ice_cream_sales = [87, 96, 76, 178, 130, 95, 123, 140, 170, 190, 200, 90, 70, 165,
                   150, 139, 110, 125, 147, 166, 89, 100, 107, 134, 148, 163, 161,
                   172, 180, 195]

# Create the scatterplot
plt.figure(figsize=(12, 8))  # Change width and height of the chart reasonably
plt.scatter(temperatures, ice_cream_sales, color='#FF5733')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Average Daily Temperature (°C)')
plt.ylabel('Ice Cream Sales (Units)')
plt.title('Ice Cream Sales vs Temperature')

# Display the scatterplot
plt.show()