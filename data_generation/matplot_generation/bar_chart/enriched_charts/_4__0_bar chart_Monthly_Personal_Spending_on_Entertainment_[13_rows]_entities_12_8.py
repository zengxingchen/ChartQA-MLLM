
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [50000, 62000, 57000, 68000, 72000, 75000, 80000, 78000, 69000, 71000, 66000, 73000]

# Colors for each bar
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#7FFF00', '#32CD32', '#00FF7F', '#4682B4', '#4169E1', '#6A5ACD', '#8A2BE2', '#DA70D6', '#FF69B4']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
plt.bar(months, revenue, color=colors, width=0.6)

# Modify the ticks, labels, and title
plt.ylabel('Monthly Revenue (USD)')
plt.title('Monthly Revenue for the Year 2023')
plt.ylim(45000, 85000)  # Setting y-axis limits

# Display the plot
plt.show()