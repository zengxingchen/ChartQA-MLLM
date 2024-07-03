
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [50, 45, 60, 70, 80, 90, 85, 95, 75, 65, 55, 60]

# Create a new figure with specific width and height
plt.figure(figsize=(14, 7))

# Plotting the line chart with a specific color scheme
plt.plot(months, sales, marker='o', linestyle='-', color='#FF6347')  # Tomato color

# Assign annotations/labels to specific data points to provide additional information
for i, sale in enumerate(sales):
    plt.annotate(str(sale), xy=(months[i], sale), xytext=(0, 10), textcoords='offset points', ha='center')

# Modify the chart title and labels
plt.title('Monthly Sales Performance', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()