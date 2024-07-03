
import matplotlib.pyplot as plt

# Monthly revenue data for a bookstore
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
revenue = [5000, 5500, 5800, 6000, 6200, 6500, 6700, 6800, 7000, 7200, 7500, 7700]

# Color scheme using specific color codes for each month
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78'
]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(months, revenue, color=colors, width=0.4)  # Bar color and band width

# Set the title and labels
plt.title('Monthly Bookstore Revenue', pad=20)
plt.ylabel('Revenue ($)')
plt.xlabel('Month')

# Set y-axis limits
plt.ylim(4800, 8000)

# Display the bar chart
plt.show()