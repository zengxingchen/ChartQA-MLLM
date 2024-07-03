
import matplotlib.pyplot as plt

# Data points
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [150, 200, 180, 220, 210, 260, 230]

# Colors for each bar
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF1493', '#40E0D0']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
plt.bar(days, sales, color=colors, width=0.5)

# Modify the ticks, labels, and title
plt.ylabel('Sales (Units)')
plt.title('Weekly Sales Performance')
plt.ylim(140, 280)  # Setting y-axis limits starting from a specific value

# Display the plot
plt.show()