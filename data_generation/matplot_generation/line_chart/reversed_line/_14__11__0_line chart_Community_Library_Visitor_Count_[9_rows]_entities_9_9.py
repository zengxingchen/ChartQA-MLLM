
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_humidity = [85, 82, 78, 75, 73, 71, 69, 72, 74, 77, 80, 83]

# Create a new figure with specific width and height
plt.figure(figsize=(12, 6))

# Plotting the line chart with a specific color scheme
plt.plot(months, average_humidity, marker='o', linestyle='-', color='#1f77b4')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, hum in enumerate(average_humidity):
    plt.annotate(str(hum), xy=(months[i], hum), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Average Humidity', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Humidity (%)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()