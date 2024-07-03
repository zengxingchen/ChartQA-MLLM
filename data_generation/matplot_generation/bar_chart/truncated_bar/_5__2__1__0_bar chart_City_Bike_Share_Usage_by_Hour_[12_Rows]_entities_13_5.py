
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = [500, 450, 600, 550, 750, 800, 820, 810, 780, 740, 700, 690]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FF8C33', '#33FFD7', '#8C33FF', '#FF3357', '#33FF8C', '#FF8C8C']

# Plotting the bar chart vertically
plt.figure(figsize=(10, 6))  # Change width and height of the chart
plt.bar(months, visitors, color=colors, edgecolor='black', width=0.5)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Monthly Museum Visitors', fontsize=16, pad=20)
plt.ylabel('Number of Visitors', fontsize=12)

# Setting the ylim to start from a specific value other than zero
plt.ylim(400, max(visitors) + 50)

# Display the chart
plt.tight_layout()
plt.show()