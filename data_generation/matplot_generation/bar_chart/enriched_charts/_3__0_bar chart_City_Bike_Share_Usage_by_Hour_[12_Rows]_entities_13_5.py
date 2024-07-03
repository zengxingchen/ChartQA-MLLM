
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [78, 62, 85, 92, 100, 120, 150, 140, 130, 110, 90, 80]

# Colors for each bar
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff7f0e', '#ffbb78', '#98df8a']

# Plotting the bar chart vertically
plt.figure(figsize=(10, 6))  # Change width and height of the chart
plt.bar(months, rainfall, color=colors, edgecolor='black', width=0.5)  # Change band width for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Rainfall in a City', fontsize=15)
plt.ylabel('Average Rainfall (mm)', fontsize=12)

# Setting the ylim to provide better clarity for rainfall values
plt.ylim(0, max(rainfall) + 20)

# Display the chart
plt.tight_layout()
plt.show()