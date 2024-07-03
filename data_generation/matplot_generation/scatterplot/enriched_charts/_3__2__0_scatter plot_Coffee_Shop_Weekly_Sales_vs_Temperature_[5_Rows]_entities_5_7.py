
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number_of_students = [120, 130, 125, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
number_of_graduates = [10, 15, 12, 18, 20, 22, 25, 30, 28, 35, 32, 38, 40, 42, 45, 48, 50, 52, 55, 58]

# Scatter plot
plt.figure(figsize=(14, 8))  # Width:14, Height:8
plt.scatter(days, number_of_students, color='#32CD32', label='Number of Students')  # Lime Green
plt.scatter(days, number_of_graduates, color='#FF1493', label='Number of Graduates')  # Deep Pink

# Customize the plot
plt.title('Student Performance Over 20 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Number of Students')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()