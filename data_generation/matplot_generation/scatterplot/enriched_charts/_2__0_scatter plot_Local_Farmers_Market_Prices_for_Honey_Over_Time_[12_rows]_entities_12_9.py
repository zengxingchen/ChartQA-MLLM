
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
heart_rates = [72, 75, 70, 78, 74, 73, 76, 77, 79, 80, 82, 74, 73, 81, 83, 75, 78,
               77, 79, 82, 80, 85, 84, 86, 88, 87, 85, 89, 90, 91, 92]
calorie_burn = [250, 260, 240, 280, 265, 255, 275, 277, 285, 290, 295, 267, 260, 290,
                300, 270, 280, 278, 285, 295, 290, 305, 302, 310, 315, 312, 308,
                318, 320, 325, 330]

# Create the scatterplot
plt.figure(figsize=(14, 10))  # Change width and height of the chart reasonably
plt.scatter(heart_rates, calorie_burn, color='#1E90FF')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Average Daily Heart Rate (BPM)')
plt.ylabel('Daily Calorie Burn (kcal)')
plt.title('Daily Calorie Burn vs Heart Rate')

# Display the scatterplot
plt.show()