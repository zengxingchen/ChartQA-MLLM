
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
daily_steps = [10000, 12000, 11500, 13000, 14000, 12500, 13500, 14500, 15000, 16000, 15500, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500, 21000, 21500, 22000, 22500, 23000, 23500, 24000, 24500, 25000, 25500]
calorie_intake = [2000, 2200, 2100, 2300, 2500, 2200, 2400, 2600, 2700, 2800, 2750, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700]

# Create a scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(days, daily_steps, c="#4682B4", label="Daily Steps")
plt.scatter(days, calorie_intake, c="#8B0000", label="Calorie Intake")

# Customize the chart
plt.title("Daily Steps and Calorie Intake Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Count")
plt.legend(loc='upper left')
plt.grid(True)

# Show the scatterplot
plt.show()