
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = list(range(1, 31))
steps_count = [4000, 6000, 8000, 7000, 5000, 10000, 9000, 11000, 9500, 10500, 11500, 8500, 12000, 12500, 13000,
               7000, 7500, 8000, 9500, 10000, 8500, 10500, 11000, 9500, 10000, 10500, 11500, 12000, 12500, 13000]
calorie_intake = [2000, 2200, 2500, 2300, 2100, 2600, 2400, 2700, 2550, 2750, 2800, 2450, 2900, 3000, 3100,
                  2350, 2400, 2500, 2600, 2650, 2500, 2750, 2800, 2600, 2700, 2750, 2900, 2950, 3050, 3100]

# Create the scatterplot
plt.figure(figsize=(14, 10))  # Change width and height of the chart reasonably
plt.scatter(steps_count, calorie_intake, color='#1E90FF')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Daily Steps Count')
plt.ylabel('Calorie Intake (kcal)')
plt.title('Calorie Intake vs Steps Count')

# Display the scatterplot
plt.show()