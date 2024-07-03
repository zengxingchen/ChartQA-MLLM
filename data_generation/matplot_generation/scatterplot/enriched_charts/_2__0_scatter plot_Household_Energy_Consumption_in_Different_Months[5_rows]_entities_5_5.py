
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
calories_burned = [300, 350, 250, 400, 380, 420, 430, 390, 410, 450, 460, 440, 370, 360, 340, 330, 310, 290, 320, 410, 370, 390, 430, 450, 480, 490, 510, 450, 430, 400]
miles_run = [2, 2.5, 1.8, 3, 2.8, 3.2, 3.3, 3, 3.1, 3.5, 3.6, 3.4, 2.7, 2.6, 2.4, 2.3, 2.1, 1.9, 2.2, 3.1, 2.7, 3, 3.3, 3.5, 3.8, 3.9, 4.1, 3.5, 3.3, 3]

# Create a scatterplot
plt.figure(figsize=(14, 9))
plt.scatter(days, calories_burned, c="#1f77b4", label="Calories Burned")
plt.scatter(days, miles_run, c="#ff7f0e", label="Miles Run")

# Customize the chart
plt.title("Daily Exercise Tracking", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Calories/Miles")
plt.legend()
plt.grid(True)

# Show the scatterplot
plt.show()