
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [20000, 22000, 25000, 27000, 30000, 32000, 34000, 36000, 38000, 40000, 42000, 45000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))  # Changed figure size

# Plotting the horizontal bar chart
ax.barh(months, sales, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#7f7f7e'], height=0.6)  # Changed colors, and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Sales in USD')
ax.set_title('Monthly Sales Data')
ax.set_xlim([0, 50000])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()