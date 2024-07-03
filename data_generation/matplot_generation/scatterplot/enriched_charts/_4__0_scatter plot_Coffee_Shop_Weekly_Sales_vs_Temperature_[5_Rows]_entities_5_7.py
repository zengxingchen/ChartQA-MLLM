
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
steps = [10000, 10500, 11000, 10800, 11500, 12000, 11800, 12500, 13000, 12800, 13500, 14000, 13800, 14500, 15000, 14800, 15500, 16000, 15800, 16500, 17000, 16800, 17500, 18000, 17800, 18500, 19000, 18800, 19500, 20000]
heart_rate = [60, 62, 63, 64, 66, 67, 65, 68, 70, 69, 71, 72, 70, 73, 74, 72, 75, 76, 74, 77, 78, 76, 79, 80, 78, 81, 82, 80, 83, 84]

# Scatter plot
plt.figure(figsize=(12, 8))  # Width:12, Height:8
plt.scatter(days, steps, color='#FF5733', label='Steps')  # Orange
plt.scatter(days, heart_rate, color='#3498DB', label='Heart Rate')  # Blue

# Customize the plot
plt.title('Health & Fitness Data Over 30 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Measurements')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()