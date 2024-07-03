
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
caloric_intake = [2200, 2150, 2300, 2350, 2400, 2500, 2550, 2600, 2450, 2350, 2250, 2400]

# Colors for each bar
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#f7d358', '#e59866', '#f0b27a', '#af7ac5']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.barh(months, caloric_intake, color=colors, edgecolor='black', height=0.6)  # Change height for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Caloric Intake in a City', fontsize=18)
plt.xlabel('Average Caloric Intake (kcal)', fontsize=14)

# Setting the xlim to provide better clarity for caloric intake values
plt.xlim(0, max(caloric_intake) + 200)

# Display the chart
plt.tight_layout()
plt.show()