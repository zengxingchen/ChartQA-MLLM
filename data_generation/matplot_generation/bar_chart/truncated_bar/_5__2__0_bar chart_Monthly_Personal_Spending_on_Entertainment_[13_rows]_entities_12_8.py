
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [30000, 32000, 31000, 36000, 34000, 38000, 40000, 42000, 39000, 37000, 38000, 40000]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF8C33', '#33A1FF', '#A133FF', '#FFA133', '#FF3333', '#33FF8C', '#8C33FF']

# Create a horizontal bar chart
plt.figure(figsize=(14, 9))
plt.barh(months, revenue, color=colors, height=0.6)

# Modify the ticks, labels, and title
plt.xlabel('Revenue ($)')
plt.title('Monthly Revenue Overview', pad=20)
plt.xlim(25000, 45000)

# Display the plot
plt.show()