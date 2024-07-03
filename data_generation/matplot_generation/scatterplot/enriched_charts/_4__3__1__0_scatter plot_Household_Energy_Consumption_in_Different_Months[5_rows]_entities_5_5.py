
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
step_count = [7000, 8500, 6000, 9000, 7500, 11000, 9500, 12000, 10000, 13000, 10500, 14000, 11500, 15000, 12500, 13500, 14500, 15500, 16000, 17000, 16500, 17500, 18000, 18500, 19000, 19500, 20000, 20500, 21000, 21500]
calorie_burn = [250, 300, 230, 320, 280, 350, 340, 400, 360, 420, 380, 450, 390, 460, 410, 430, 470, 480, 500, 520, 510, 530, 540, 550, 560, 570, 580, 590, 600, 610]

# Create a scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(days, step_count, c="#FF5733", label="Step Count")
plt.scatter(days, calorie_burn, c="#33FFCE", label="Calorie Burn")

# Customize the chart
plt.title("Daily Step Count and Calorie Burn Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Value")
plt.legend(loc='upper left')
plt.grid(True)

# Show the scatterplot
plt.show()