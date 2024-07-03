
import matplotlib.pyplot as plt

# Data points for distance traveled (in miles) vs fuel consumption (in gallons)
distance_traveled = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
fuel_consumption = [1.2, 2.1, 2.8, 3.6, 4.5, 5.3, 6.1, 7.0, 7.8, 8.6, 9.5, 10.3, 11.0, 11.8, 12.5, 13.3, 14.0, 14.8, 15.6, 16.3]

# Creating the scatter plot
plt.figure(figsize=(14, 7))  # Modify width and height of the chart
plt.scatter(distance_traveled, fuel_consumption, color='#1F77B4')  # Change to an RGB color code

# Adding chart labels and title
plt.title('Impact of Distance Traveled on Fuel Consumption', pad=20)
plt.xlabel('Distance Traveled (Miles)')
plt.ylabel('Fuel Consumption (Gallons)')

# Show the figure
plt.show()