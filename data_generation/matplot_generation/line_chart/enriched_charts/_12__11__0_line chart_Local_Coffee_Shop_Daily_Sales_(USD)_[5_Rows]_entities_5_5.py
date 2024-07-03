
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [32, 35, 42, 50, 60, 70, 75, 73, 65, 55, 45, 37]

# Plotting the line chart
plt.figure(figsize=(16, 8))
plt.plot(months, temperatures, marker='o', linestyle='--', color='#1f77b4', linewidth=2.5)

# Adding title and labels
plt.title('Average Monthly Temperature in City XYZ', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°F)', fontsize=14)

# Adding an annotation for the highest temperature
highest_temp_index = temperatures.index(max(temperatures))
highest_temp_month = months[highest_temp_index]
plt.annotate('Highest Temperature', xy=(highest_temp_index, max(temperatures)), xytext=(highest_temp_index, max(temperatures) + 5),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(30, 80)
plt.show()