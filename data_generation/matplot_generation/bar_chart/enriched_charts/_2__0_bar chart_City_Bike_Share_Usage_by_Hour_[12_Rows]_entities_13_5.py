
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sunlight_hours = [150, 160, 180, 200, 220, 250, 260, 240, 220, 190, 160, 140]

# Colors for each bar
colors = ['#FFA07A', '#FF7F50', '#FF6347', '#FF4500', '#FF8C00', '#FFD700', '#FFDAB9', '#FFE4B5', '#EEE8AA', '#F0E68C', '#BDB76B', '#808000']

# Plotting the bar chart vertically
plt.figure(figsize=(10, 6))   # Change width and height of the chart
plt.bar(months, sunlight_hours, color=colors, edgecolor='black', width=0.6)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Sunlight Hours in a City', fontsize=15)
plt.ylabel('Sunlight Hours', fontsize=12)

# Setting the ylim to provide better clarity for sunlight hours values
plt.ylim(0, max(sunlight_hours) + 50)

# Display the chart
plt.tight_layout()
plt.show()