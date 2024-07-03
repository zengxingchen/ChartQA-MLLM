
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
hours = [12, 15, 20, 25, 30, 35, 40, 38, 32, 28, 22, 18]

# Colors for each bar
colors = ['#3498DB', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8', '#A569BD', '#BB8FCE', '#D2B4DE', '#E8DAEF', '#F5B7B1', '#F1948A', '#EC7063']

# Plotting the bar chart vertically
plt.figure(figsize=(10, 6))
plt.bar(months, hours, color=colors, edgecolor='black', width=0.6)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Exercise Hours of a Fitness Enthusiast', fontsize=15, pad=20)
plt.ylabel('Exercise Hours', fontsize=12)

# Setting the ylim to truncate the y-axis
plt.ylim(10, max(hours) + 5)

# Display the chart
plt.tight_layout()
plt.show()