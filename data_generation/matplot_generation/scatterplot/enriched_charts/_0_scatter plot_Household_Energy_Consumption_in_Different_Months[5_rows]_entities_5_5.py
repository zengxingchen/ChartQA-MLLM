
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
temperatures = [25, 28, 24, 26, 29, 30, 31, 32, 33, 35, 34, 33, 29,
                28, 27, 26, 22, 24, 26, 27, 28, 30, 32, 33, 34, 35, 36, 31, 29, 28]
sales = [75, 89, 65, 77, 95, 105, 110, 120, 130, 140, 135, 125, 100,
         95, 80, 70, 60, 65, 78, 85, 90, 108, 115, 120, 125, 130, 140, 112, 96, 85]

# Create a scatterplot
plt.figure(figsize=(12, 8))
plt.scatter(days, temperatures, c="#FF5733", label="Temperature (Celsius)")
plt.scatter(days, sales, c="#335BFF", label="Ice Cream Sales (Units)")

# Customize the chart
plt.title("Temperature Influence on Ice Cream Sales")
plt.xlabel("Day of the Month")
plt.ylabel("Temperature/Sales")
plt.legend()
plt.grid(True)

# Show the scatterplot
plt.show()