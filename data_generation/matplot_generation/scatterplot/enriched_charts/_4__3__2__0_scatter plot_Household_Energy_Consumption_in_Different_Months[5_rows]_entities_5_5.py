
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
calories_consumed = [2200, 2300, 2000, 2400, 2350, 2450, 2500, 2400, 2550, 2600, 2700, 2650, 2500, 2450, 2400, 2350, 2300, 2250, 2300, 2400, 2350, 2400, 2500, 2550, 2600, 2650, 2700, 2550, 2500, 2450]
calories_burned = [1800, 1750, 1850, 1900, 2000, 2100, 1950, 2050, 2200, 2150, 2250, 2300, 2100, 2000, 1950, 1900, 1850, 1800, 1900, 2000, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2100, 2050, 2000]

# Create a scatterplot
plt.figure(figsize=(14, 8))
plt.scatter(days, calories_consumed, c="#1f77b4", label="Calories Consumed")
plt.scatter(days, calories_burned, c="#ff7f0e", label="Calories Burned")

# Customize the chart
plt.title("Daily Calorie Intake and Burn", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Calories")
plt.legend(loc='upper right')
plt.grid(True)

# Show the scatterplot
plt.show()