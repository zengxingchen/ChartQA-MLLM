
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01", "2024-06-01",
         "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01", "2024-11-01", "2024-12-01"]
temperatures = [4, 6, 10, 14, 18, 22, 25, 24, 20, 15, 9, 5]

# Creating the line chart
plt.figure(figsize=(16, 8))

plt.plot(dates, temperatures, color="#1E90FF", marker='s')

# Annotating the highest and lowest temperatures
plt.annotate('Highest\n25°C', xy=("2024-07-01", 25), xytext=("2024-07-01", 27),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n4°C', xy=("2024-01-01", 4), xytext=("2024-01-01", 2),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Average Temperatures in 2024", fontsize=20, pad=30)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Average Temperature (°C)", fontsize=16)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.8, color='grey')

# Show the plot
plt.show()