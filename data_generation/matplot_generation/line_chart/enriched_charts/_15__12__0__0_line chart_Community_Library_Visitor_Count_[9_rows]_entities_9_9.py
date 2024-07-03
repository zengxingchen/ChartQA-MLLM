
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [1500, 1800, 2200, 3000, 3500, 4000, 4200, 4100, 3800, 3500, 2000, 1700]

# Create a new figure with specific width and height
plt.figure(figsize=(14, 7))

# Plotting the line chart with a specific color scheme
plt.plot(months, revenue, marker='o', linestyle='-', color='#FF6347')  # Tomato color

# Assign annotations/labels to specific data points to provide additional information
for i, rev in enumerate(revenue):
    plt.annotate(str(rev), xy=(months[i], rev), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Revenue Trend', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()