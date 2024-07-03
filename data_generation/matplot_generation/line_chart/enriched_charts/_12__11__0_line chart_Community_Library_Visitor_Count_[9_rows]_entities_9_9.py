
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_readings = [30, 28, 35, 40, 50, 65, 75, 85, 70, 55, 45, 35]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, average_readings, marker='o', linestyle='-', color='#1f77b4')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, reading in enumerate(average_readings):
    plt.annotate(str(reading), xy=(months[i], reading), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Reading Progress', pad=20)
plt.xlabel('Month')
plt.ylabel('Reading Time (hours)')

# Show the plot
plt.show()