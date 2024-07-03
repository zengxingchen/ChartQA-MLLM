
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
steps = [5000, 7000, 6000, 8000, 7500, 9000, 9500, 10000, 11000, 12000, 11500, 10500, 8500, 7500, 7000, 6500, 7000, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 9500, 8500]
calories_burned = [200, 280, 240, 320, 300, 360, 380, 400, 440, 480, 460, 420, 340, 300, 280, 260, 280, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 380, 340]

# Create a scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(days, steps, c="#2E8B57", label="Steps Walked")
plt.scatter(days, calories_burned, c="#8A2BE2", label="Calories Burned")

# Customize the chart
plt.title("Daily Steps and Calories Burned", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Count/Calories")
plt.legend(loc='upper left')
plt.grid(True)

# Show the scatterplot
plt.show()