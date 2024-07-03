
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = [i for i in range(1, 32)]
distance_run = [3.2, 5.0, 2.5, 6.1, 4.2, 5.3, 7.4, 4.5, 8.0, 6.2, 7.1, 9.0, 5.4, 10.2, 8.1, 7.3, 9.1, 6.0, 11.0, 8.3, 9.0, 10.5, 12.0, 11.3, 13.1, 10.0, 12.5, 14.0, 11.2, 13.2, 15.0]
calories_burned = [250, 350, 200, 400, 320, 360, 500, 330, 550, 410, 480, 600, 370, 650, 560, 490, 580, 420, 700, 570, 600, 680, 750, 720, 800, 670, 780, 850, 710, 820, 900]

# Create the scatterplot
plt.figure(figsize=(14, 10))  # Change width and height of the chart reasonably
plt.scatter(distance_run, calories_burned, color='#1E90FF')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Distance Run (km)')
plt.ylabel('Calories Burned')
plt.title('Distance Run vs Calories Burned')

# Display the scatterplot
plt.show()