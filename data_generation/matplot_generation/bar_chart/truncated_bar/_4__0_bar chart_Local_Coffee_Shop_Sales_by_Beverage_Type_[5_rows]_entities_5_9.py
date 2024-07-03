
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = [50000, 52000, 55000, 58000, 61000, 65000, 70000, 72000, 68000, 64000, 60000, 57000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))  # Changed figure size

# Plotting the vertical bar chart
ax.bar(months, visitors, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#ffb380', '#80b3ff', '#ccccff', '#e6b3b3'], width=0.7)  # Changed colors, and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Number of Visitors')
ax.set_title('Monthly Visitors to National Parks', pad=20)
ax.set_ylim([40000, 75000])  # Adjusted to start from 40000

# Display the plot
plt.tight_layout()
plt.show()