
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
stress_levels = [45, 50, 55, 60, 65, 70, 75, 80, 70, 65, 60, 55]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, stress_levels, marker='o', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest stress level points
plt.annotate('Highest\n80', xy=('August', 80), xytext=('July', 85),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n45', xy=('January', 45), xytext=('February', 40),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Monthly Average Stress Levels in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Stress Level (0-100)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()